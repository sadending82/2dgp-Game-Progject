from pico2d import *
import Character
import time
from game_framework import *

Window_Width = 800
Window_Height = 600
izuna = None
base_dungeon = None


def enter():
    global izuna, base_dungeon
    izuna = Character.Hero()
    izuna.state = Character.Character_State_Idle
    base_dungeon = load_image('dungeon1_base.png')


def exit():
    global izuna, base_dungeon
    del(izuna)
    del(base_dungeon)


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
                print('input j ', izuna.state, izuna.frame)
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

    izuna.Move()
    print('Move ', izuna.state, izuna.frame)
    izuna.Set_Hero_New()
    print('SetHero ', izuna.state, izuna.frame)
    handle_events()
    if izuna.state == Character.Character_State_Attack:
        print('j', izuna.state)

def draw():
    clear_canvas()
    base_dungeon.draw(Window_Width // 2, Window_Height // 2, Window_Width, Window_Height)
    izuna.Draw_Character()
    update_canvas()






