from pico2d import *
import Character
import Monster
import game_framework
import game_world
import map
from save_and_load import *
import time
from game_framework import *
from game_world import *
import dungeon_1_102
import inventory
import item
import server

Window_Width = get_canvas_width()
Window_Height = get_canvas_height()


is_attack = False
is_attack_delay = False


def enter():
    if not is_in_objects(Character.Hero):
        server.izuna = Character.Hero()
        server.izuna.state = Character.Character_State_Idle
    else:
        server.izuna = return_object(Character.Hero)
    MonsterStack = []
    for i in range(2):
        server.monster.append(Monster.Bunnia())
    for i in range(0):
        server.monster.append(Monster.Soul())
    server.map = map.FirstDungeonMap(map.Door_None, map.Door_Normal, map.Door_Normal, map.Door_None)
    MonsterCount = len(server.MonsterStack)
    add_object(server.izuna, 1)
    for i in server.monster:
        add_object(i, 1)
    add_object(server.map, 0)


def exit():
    global izuna, base_dungeon, MonsterStack
    game_world.clear()

    server.izuna = None
    server.map = None
    server.monster.clear()
    server.item.clear()


def handle_events():
    global Program_Running
    global izuna
    global is_attack
            elif event.key == SDLK_y:
                if base_dungeon.is_door_open:
                    base_dungeon.is_door_open = False
                else:
                    base_dungeon.is_door_open = True
            elif event.key == SDLK_i:
                game_framework.push_state(inventory)
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

def pause():
    pass

def resume():
    pass

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
    global izuna, MonsterStack, ItemStack
    global is_attack, is_attack_delay, ItemCount

    for i in ItemStack:
        if collide(izuna, i):
            izuna.inventory.append(i.item_code)
            game_world.remove_object(i)
            ItemStack.remove(i)
            ItemCount -= 1

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
            m_item = item.item(monster.code, monster.x, monster.y)
            ItemStack.append(m_item)
            ItemCount += 1
            game_world.add_object(ItemStack[ItemCount - 1], 1)
            monster.dead()
            count += 1

    if izuna.state != Character.Character_State_Attack:
        is_attack = False
        is_attack_delay = False

    for game_object in game_world.all_objects():
        game_object.update()
    game_world.sort_objects(1)

    if collide_with_map(izuna, base_dungeon, 'wall', 8) :
        if izuna.direction == Character.Character_Direction_Left:
            izuna.x += 2 * izuna.speed
        if izuna.direction == Character.Character_Direction_Right:
            izuna.x -= 2 * izuna.speed
        if izuna.direction == Character.Character_Direction_Up:
            izuna.y -= 2 * izuna.speed
        if izuna.direction == Character.Character_Direction_Down:
            izuna.y += 2 * izuna.speed

    if not base_dungeon.is_door_open:
        if collide_with_map(izuna, base_dungeon, 'door_up', 1) or collide_with_map(izuna, base_dungeon, 'door_left', 1)\
                or collide_with_map(izuna, base_dungeon, 'door_right', 1) or\
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
        if collide_with_map(izuna, base_dungeon, 'door_left', 1) or collide_with_map(izuna, base_dungeon, 'door_down', 1):
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
            izuna.x = 105
            save_data(izuna, 2)
            game_framework.change_state(dungeon_1_102)

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






