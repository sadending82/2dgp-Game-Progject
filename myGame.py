Window_Width, Window_Height = 800, 600
import pico2d
pico2d.open_canvas(Window_Width, Window_Height)

import game_framework
import main_state


game_framework.run(main_state)
pico2d.close_canvas()
