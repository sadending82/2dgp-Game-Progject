from pico2d import *
import Character
import Monster
import game_world
import map
from save_and_load import *
import time
from game_framework import *
from game_world import *

Window_Width = get_canvas_width()
Window_Height = get_canvas_height()
izuna = None
MonsterStack = []
base_dungeon = None
MonsterCount = 0

is_attack = False
is_attack_delay = False


def enter():
    global izuna, MonsterStack, base_dungeon, MonsterCount
    if not is_in_objects(Character.Hero):
        izuna = Character.Hero()
        izuna.state = Character.Character_State_Idle
    else:
        izuna = return_object(Character.Hero)
    MonsterStack = []
    for i in range(2):
        MonsterStack.append(Monster.Bunnia())
    for i in range(1):
        MonsterStack.append(Monster.Soul())
    base_dungeon = map.FirstDungeonMap(map.Door_None, map.Door_Normal, map.Door_Normal, map.Door_None)
    MonsterCount = len(MonsterStack)
    add_object(izuna, 1)
    for i in MonsterStack:
        add_object(i, 1)
    add_object(base_dungeon, 0)


def exit():
    global izuna, base_dungeon
    game_world.clear()
    del (izuna)
    del (base_dungeon)
    del (MonsterStack)


def handle_events():
    global Program_Running
    global izuna
    global is_attack
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_a:
                izuna.isLeftButton = True
            elif event.key == SDLK_d:
                izuna.isRightButton = True
            elif event.key == SDLK_w:
                izuna.isUpButton = True
            elif event.key == SDLK_s:
                izuna.isDownButton = True
            elif event.key == SDLK_j:
                izuna.state = Character.Character_State_Attack
                izuna.frame = 0
                izuna.frameTime = time.time()
                is_attack = True
            elif event.key == SDLK_TAB:
                save_data(izuna, izuna.direction)
            elif event.key == SDLK_t:
                izuna = load_data()
            elif event.key == SDLK_y:
                if base_dungeon.is_door_open:
                    base_dungeon.is_door_open = False
                else:
                    base_dungeon.is_door_open = True
            elif event.key == SDLK_ESCAPE:
                quit()
            elif event.key == SDLK_LSHIFT:
                izuna.speed = 2
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_a:
                izuna.isLeftButton = False
            elif event.key == SDLK_d:
                izuna.isRightButton = False
            elif event.key == SDLK_w:
                izuna.isUpButton = False
            elif event.key == SDLK_s:
                izuna.isDownButton = False
            elif event.key == SDLK_LSHIFT:
                izuna.speed = 1


def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b:
        return False
    if right_a < left_b:
        return False
    if top_a < bottom_b:
        return False
    if bottom_a > top_b:
        return False

    return True


def collide_with_map(a, wall, category, count):
    check_list = []
    for i in range(count):
        left_a, bottom_a, right_a, top_a = a.get_bb()
        left_wall, bottom_wall, right_wall, top_wall = wall.get_bb(category, i)
        if left_a <= right_wall:
            if right_a >= left_wall:
                if top_a >= bottom_wall:
                    if bottom_a <= top_wall:
                        check_list.append(True)
                        continue
        check_list.append(False)

    for is_in_true in check_list:
        if is_in_true:
            return True

    return False


def collide_with_attack(chara, b):
    left_a, bottom_a, right_a, top_a = chara.get_attack_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b:
        return False
    if right_a < left_b:
        return False
    if top_a < bottom_b:
        return False
    if bottom_a > top_b:
        return False

    return True


def update():
    global izuna, MonsterStack
    global is_attack, is_attack_delay

    count = 0
    for monster in MonsterStack:
        if collide(izuna, monster):
            if not izuna.is_invincible:
                izuna.Hp -= monster.damage
                izuna.attacked(monster.damage)

        if collide_with_attack(izuna, monster):
            if is_attack:
                if not is_attack_delay:
                    is_attack_delay = True
                    monster.Hp -= izuna.damage
                    print(monster.Hp)

        if monster.Hp <= 0:
            game_world.remove_object(monster)
            monster.dead()
            count += 1

    if izuna.state != Character.Character_State_Attack:
        is_attack = False
        is_attack_delay = False

    for game_object in game_world.all_objects():
        game_object.update()
    game_world.sort_objects(1)

    if collide_with_map(izuna, base_dungeon, 'wall', 8):
        if izuna.direction == Character.Character_Direction_Left:
            izuna.x += 2 * izuna.speed
        if izuna.direction == Character.Character_Direction_Right:
            izuna.x -= 2 * izuna.speed
        if izuna.direction == Character.Character_Direction_Up:
            izuna.y -= 2 * izuna.speed
        if izuna.direction == Character.Character_Direction_Down:
            izuna.y += 2 * izuna.speed

    if not base_dungeon.is_door_open:
        if collide_with_map(izuna, base_dungeon, 'door_up', 1) or collide_with_map(izuna, base_dungeon, 'door_left', 1) \
                or collide_with_map(izuna, base_dungeon, 'door_right', 1) or \
                collide_with_map(izuna, base_dungeon, 'door_down', 1):
            if izuna.direction == Character.Character_Direction_Left:
                izuna.x += 2 * izuna.speed
            if izuna.direction == Character.Character_Direction_Right:
                izuna.x -= 2 * izuna.speed
            if izuna.direction == Character.Character_Direction_Up:
                izuna.y -= 2 * izuna.speed
            if izuna.direction == Character.Character_Direction_Down:
                izuna.y += 2 * izuna.speed
    else:
        if collide_with_map(izuna, base_dungeon, 'door_left', 1) or collide_with_map(izuna, base_dungeon, 'door_down',
                                                                                     1):
            print('left_door')
            if izuna.direction == Character.Character_Direction_Left:
                izuna.x += 2 * izuna.speed
            if izuna.direction == Character.Character_Direction_Right:
                izuna.x -= 2 * izuna.speed
            if izuna.direction == Character.Character_Direction_Up:
                izuna.y -= 2 * izuna.speed
            if izuna.direction == Character.Character_Direction_Down:
                izuna.y += 2 * izuna.speed
        if collide_with_map(izuna, base_dungeon, 'door_up', 1):
            print('up_door')
        if collide_with_map(izuna, base_dungeon, 'door_right', 1):
            print('right_door')

    if MonsterCount - count <= 0:
        base_dungeon.is_door_open = True

    delay(0.005)
    handle_events()


def draw():
    global izuna, MonsterStack, base_dungeon
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()

    update_canvas()






