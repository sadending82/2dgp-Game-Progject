from pico2d import *
import Character
import Monster
from save_and_load import *
import time
from game_framework import *

Window_Width = get_canvas_width()
Window_Height = get_canvas_height()
izuna = None
MonsterStack = None
base_dungeon = None
isDoorOpen = False


def enter():
    global izuna, MonsterStack, base_dungeon
    izuna = Character.Hero()
    izuna.state = Character.Character_State_Idle
    MonsterStack = [Monster.Bunnia() for n in range(0, 4)]
    base_dungeon = load_image('dungeon1_base.png')


def exit():
    global izuna, base_dungeon
    save_data(izuna, 0)
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
    for i in MonsterStack:
        i.move()
        i.update()
    izuna.update()
    handle_events()

def draw():
    global izuna, MonsterStack, base_dungeon
    clear_canvas()
    base_dungeon.draw(Window_Width // 2, Window_Height // 2, Window_Width, Window_Height)
    for i in MonsterStack:
        if i.y > izuna.y:
            i.draw()
    izuna.draw()
    for i in MonsterStack:
        if i.y <= izuna.y:
            i.draw()

    update_canvas()






