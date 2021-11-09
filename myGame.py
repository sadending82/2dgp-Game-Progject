Window_Width, Window_Height = 800, 600
import pico2d
pico2d.open_canvas(Window_Width, Window_Height)

import game_framework
import dungeon_1_101


game_framework.run(dungeon_1_101)
pico2d.close_canvas()
