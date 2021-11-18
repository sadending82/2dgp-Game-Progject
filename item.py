from pico2d import *

bunnia_0 = 0
soul_0 = 1

bunnia_0_image = load_image('bunnia_0.png')
soul_0_image = load_image('Soul_0.png')

bunnia_0_small_image = load_image('bunnia_0_small.png')
soul_0_small_image = load_image('Soul_0_small.png')


class item:
    def __init__(self, code, x, y):
        self.item_code = code
        self.x = x
        self.y = y
        self.bound_box = [self.x - 8, self.y - 8, self.x + 8, self.y + 8]

    def get_bb(self):
        return self.bound_box[0], self.bound_box[1], self.bound_box[2], self.bound_box[3]

    def draw(self):
        if self.item_code == 0:
            bunnia_0_small_image.draw(self.x, self.y)
        elif self.item_code == 1:
            soul_0_small_image.draw(self.x, self.y)

        draw_rectangle(self.bound_box[0], self.bound_box[1], self.bound_box[2], self.bound_box[3])


    def update(self):
        pass