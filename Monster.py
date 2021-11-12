from pico2d import *
import time
import random

Monster_State_Idle = 0
Monster_State_Move = 1
Monster_State_Attack = 2
Monster_State_Attacked = 3

Left = 0
Up = 1
Right = 2
Down = 3


class Bunnia:
    image = None
    def __init__(self):
        self.x = random.randint(81, 680)
        self.y = random.randint(81, 480)
        self.state = Monster_State_Idle
        self.frame = 0
        self.frameTime = time.time()
        self.direction = random.randint(0, 3)
        self.bound_box = [self.x, self.y, self.x+32, self.y+32]
        if Bunnia.image is None:
            Bunnia.image = load_image('Bunnia.png')



    def draw(self):
        if self.state == Monster_State_Idle:
            if self.direction == Left:
                self.image.clip_draw(1, 372 - 338, 32, 32, self.x, self.y)
            elif self.direction == Up:
                self.image.clip_draw(1, 372 - 239, 32, 32, self.x, self.y)
            elif self.direction == Right:
                self.image.clip_draw(1, 372 - 305, 32, 32, self.x, self.y)
            elif self.direction == Down:
                self.image.clip_draw(1, 372 - 371, 32, 32, self.x, self.y)
        elif self.state == Monster_State_Move:
            if self.direction == Left:
                if self.frame == 0:
                    self.image.clip_draw(33, 372 - 338, 32, 32, self.x, self.y)
                elif self.frame == 1:
                    self.image.clip_draw(66, 372 - 338, 32, 32, self.x, self.y)
                elif self.frame == 2:
                    self.image.clip_draw(99, 372 - 338, 32, 32, self.x, self.y)
                elif self.frame == 3:
                    self.image.clip_draw(99, 372 - 338, 32, 32, self.x, self.y)
                elif self.frame == 4:
                    self.image.clip_draw(66, 372 - 338, 32, 32, self.x, self.y)
                elif self.frame == 5:
                    self.image.clip_draw(33, 372 - 338, 32, 32, self.x, self.y)
            elif self.direction == Up:
                if self.frame == 0:
                    self.image.clip_draw(1, 372 - 239, 32, 32, self.x, self.y)
                elif self.frame == 1:
                    self.image.clip_draw(34, 372 - 239, 32, 32, self.x, self.y)
                elif self.frame == 2:
                    self.image.clip_draw(67, 372 - 239, 32, 32, self.x, self.y)
                elif self.frame == 3:
                    self.image.clip_draw(67, 372 - 239, 32, 32, self.x, self.y)
                elif self.frame == 4:
                    self.image.clip_draw(34, 372 - 239, 32, 32, self.x, self.y)
                elif self.frame == 5:
                    self.image.clip_draw(1, 372 - 239, 32, 32, self.x, self.y)
            elif self.direction == Right:
                if self.frame == 0:
                    self.image.clip_draw(1, 372 - 305, 32, 32, self.x, self.y)
                elif self.frame == 1:
                    self.image.clip_draw(34, 372 - 305, 32, 32, self.x, self.y)
                elif self.frame == 2:
                    self.image.clip_draw(67, 372 - 305, 32, 32, self.x, self.y)
                elif self.frame == 3:
                    self.image.clip_draw(67, 372 - 305, 32, 32, self.x, self.y)
                elif self.frame == 4:
                    self.image.clip_draw(34, 372 - 305, 32, 32, self.x, self.y)
                elif self.frame == 5:
                    self.image.clip_draw(1, 372 - 305, 32, 32, self.x, self.y)
            elif self.direction == Down:
                if self.frame == 0:
                    self.image.clip_draw(1, 372 - 371, 32, 32, self.x, self.y)
                elif self.frame == 1:
                    self.image.clip_draw(34, 372 - 371, 32, 32, self.x, self.y)
                elif self.frame == 2:
                    self.image.clip_draw(67, 372 - 371, 32, 32, self.x, self.y)
                elif self.frame == 3:
                    self.image.clip_draw(67, 372 - 371, 32, 32, self.x, self.y)
                elif self.frame == 4:
                    self.image.clip_draw(34, 372 - 371, 32, 32, self.x, self.y)
                elif self.frame == 5:
                    self.image.clip_draw(1, 372 - 371, 32, 32, self.x, self.y)

    def bound_box_check(self, map):
        pass

    def update(self):

        if self.state == Monster_State_Move:
            if 2 <= self.frame <= 3:
                if self.direction == Left:
                    if self.x >= 100:
                        self.x -= 3
                elif self.direction == Up:
                    if self.y <= 500:
                        self.y += 3
                elif self.direction == Right:
                    if self.x <= 700:
                        self.x += 3
                elif self.direction == Down:
                    if self.y >= 100:
                        self.y -= 3

        nowTime = time.time()

        if nowTime - self.frameTime > 0.1:
            self.frameTime = time.time()
            print(self.frame, self.state)
            if self.state == Monster_State_Move or self.state == Monster_State_Idle:
                self.frame = self.frame + 1
                if self.frame >= 5:
                    self.frame = 0
                    idle_or_move = random.randint(0, 1)
                    if idle_or_move == 0:
                        self.state = Monster_State_Idle
                    elif idle_or_move == 1:
                        self.state = Monster_State_Move
                        self.direction = random.randint(0, 3)



