from pico2d import *
import Character
import Monster
import time
from game_framework import *

Window_Width = 800
Window_Height = 600
izuna = None
MonsterStack = None
base_dungeon = None


def enter():
    global izuna, MonsterStack, base_dungeon
    izuna = Character.Hero()
    izuna.state = Character.Character_State_Idle
    MonsterStack = [Monster.Bunnia() for n in range(0, 4)]
    base_dungeon = load_image('dungeon1_base.png')


def exit():
    global izuna, base_dungeon
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






