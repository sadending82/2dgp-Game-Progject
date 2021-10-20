from pico2d import *
import Character
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
            if event.key == SDLK_ESCAPE:
                Program_Running = False
            elif event.key == SDLK_LEFT:
                izuna.isLeftButton = True
            elif event.key == SDLK_RIGHT:
                izuna.isRightButton = True
            elif event.key == SDLK_UP:
                izuna.isUpButton = True
            elif event.key == SDLK_DOWN:
                izuna.isDownButton = True
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                izuna.isLeftButton = False
            elif event.key == SDLK_RIGHT:
                izuna.isRightButton = False
            elif event.key == SDLK_UP:
                izuna.isUpButton = False
            elif event.key == SDLK_DOWN:
                izuna.isDownButton = False


def update():

    izuna.Move()
    izuna.Set_Hero_New()

    handle_events()

def draw():
    clear_canvas()
    base_dungeon.draw(Window_Width // 2, Window_Height // 2, Window_Width, Window_Height)
    izuna.Draw_Character()
    update_canvas()






