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
import item


class Inventory:

    def __init__(self):
        self.list = []

        self.image = load_image('inventory.png')

    def draw(self):
        self.image.draw(400, 300)
        count = 0
        for o in self.list:
            x = count % 5
            print(x)
            y = count // 5
            print(y)
            if o == item.bunnia_0:
                item.bunnia_0_image.draw(200 + x * 100, get_canvas_height() - 220 - y * 100)
            elif o == item.soul_0:
                item.soul_0_image.draw(200 + x * 100, get_canvas_height() - 220 - y * 100)
            count += 1

    def update(self):
        self.list.clear()
        for game_object in game_world.all_objects():
            if type(game_object) == Character.Hero:
                for i in game_object.inventory:
                    self.list.append(i)
        print(self.list)



inventory = Inventory()


def enter():
    global inventory
    game_world.add_object(inventory, 1)
    pass


def exit():
    pop_object(1)
    pass


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_KEYDOWN:
            if event.key == SDLK_i:
                pop_state()
        elif event.type == SDL_KEYUP:
            pass


def update():
    for game_object in game_world.all_objects():
        if type(game_object) == Inventory:
            game_object.update()


def draw():
    clear_canvas()
    for game_object in game_world.all_objects():
        game_object.draw()

    update_canvas()
