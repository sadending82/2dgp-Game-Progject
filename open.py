from pico2d import *
import Character

Window_Width, Window_Height = 800, 600


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




    pass


# 기본적인 초기화
open_canvas(Window_Width, Window_Height)
izuna = Character.Hero()
izuna.state = Character.Character_State_Idle
Program_Running = True

while Program_Running:

    clear_canvas()
    izuna.Draw_Character()


    update_canvas()

    izuna.Move()
    izuna.Set_Hero_New()
    delay(0.013)

    handle_events()

close_canvas()






