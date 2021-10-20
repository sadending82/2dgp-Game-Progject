import game_framework
import pico2d

import main_state

Window_Width, Window_Height = 800, 600

pico2d.open_canvas(Window_Width, Window_Height)
game_framework.run(main_state)
pico2d.close_canvas()