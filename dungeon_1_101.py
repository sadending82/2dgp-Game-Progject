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
    MonsterStack = [Monster.Bunnia() for n in range(0, 4)]
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
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_a:
                izuna.isLeftButton = False
            elif event.key == SDLK_d:
                izuna.isRightButton = False
            elif event.key == SDLK_w:
                izuna.isUpButton = False
            elif event.key == SDLK_s:
                izuna.isDownButton = False


def update():
    global izuna, MonsterStack
    for game_object in game_world.all_objects():
        game_object.update()
    game_world.sort_objects(1)
    handle_events()

def draw():
    global izuna, MonsterStack, base_dungeon
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()

    update_canvas()






