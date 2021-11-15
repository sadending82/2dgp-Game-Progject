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
MonsterStack = None
base_dungeon = None


def enter():
    global izuna, MonsterStack, base_dungeon
    if not is_in_objects(Character.Hero):
        izuna = Character.Hero()
        izuna.state = Character.Character_State_Idle
    else:
        izuna = return_object(Character.Hero)
    MonsterStack = []
    for i in range(4):
        MonsterStack.append(Monster.Bunnia())
    for i in range(4):
        MonsterStack.append(Monster.Soul())
    base_dungeon = map.FirstDungeonMap(map.Door_Normal, map.Door_Normal, map.Door_Normal, map.Door_Normal)

    add_object(izuna, 1)
    for i in MonsterStack:
        add_object(i, 1)
    add_object(base_dungeon, 0)


def exit():
    global izuna, base_dungeon
    game_world.clear()
    del(izuna)
    del(base_dungeon)
    del(MonsterStack)


def handle_events():
    global Program_Running
    global izuna
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
    for i in range(count):
        left_a, bottom_a, right_a, top_a = a.get_bb()
        left_wall, bottom_wall, right_wall, top_wall = wall.get_bb(category, count)

        if left_a > right_wall:
            return False
        if right_a < left_wall:
            return False
        if top_a < bottom_wall:
            return False
        if bottom_a > top_wall:
            return False

    return True


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

    print(True)
    return True



def update():
    global izuna, MonsterStack
    for game_object in game_world.all_objects():
        game_object.update()
    game_world.sort_objects(1)

    for monster in MonsterStack:
       if collide(izuna, monster):
           izuna.Hp -= monster.damage

    delay(0.005)
    handle_events()


def draw():
    global izuna, MonsterStack, base_dungeon
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()

    update_canvas()






