from pico2d import *
import time

Character_State_Idle = 0
Character_State_Move = 1
Character_State_Attack = 2
Character_State_Attacked = 3
Character_State_Roll = 4
Character_Direction_Left = 0
Character_Direction_Up = 1
Character_Direction_Right = 2
Character_Direction_Down = 3

Window_Width, Window_Height = 800, 600


class Hero:
    def __init__(self):
        self.x = Window_Width // 2
        self.y = Window_Height // 2
        self.state = Character_State_Idle
        self.frame = 0
        self.direction = Character_Direction_Right
        self.image = load_image('izuna_cheking2.png')
        self.frameTime = time.time()
        self.isLeftButton = False
        self.isRightButton = False
        self.isDownButton = False
        self.isUpButton = False
        self.speed = 1

    def draw(self):
        if self.state == Character_State_Idle:

            if self.direction == Character_Direction_Left:
                self.image.clip_draw(43, 1195 - 231, 16, 32, self.x, self.y)
            elif self.direction == Character_Direction_Up:
                self.image.clip_draw(43, 1195 - 32, 16, 32, self.x, self.y)
            elif self.direction == Character_Direction_Right:
                self.image.clip_draw(62, 1195 - 99, 16, 32, self.x, self.y)
            elif self.direction == Character_Direction_Down:
                self.image.clip_draw(43, 1195 - 165, 16, 32, self.x, self.y)

        elif self.state == Character_State_Move:
            if self.direction == Character_Direction_Left:
                if self.frame == 0:
                    self.image.clip_draw(24, 1195-231, 16, 32, self.x, self.y)
                elif self.frame == 1:
                    self.image.clip_draw(43, 1195-231, 16, 32, self.x, self.y)
                elif self.frame == 2:
                    self.image.clip_draw(62, 1195-231, 16, 32, self.x, self.y)
                elif self.frame == 3:
                    self.image.clip_draw(82, 1195-231, 17, 32, self.x, self.y)
                elif self.frame == 4:
                    self.image.clip_draw(62, 1195-231, 16, 32, self.x, self.y)
                elif self.frame == 5:
                    self.image.clip_draw(43, 1195-231, 16, 32, self.x, self.y)
            elif self.direction == Character_Direction_Up:
                if self.frame == 0:
                    self.image.clip_draw(24, 1195-31, 16, 32, self.x, self.y)
                elif self.frame == 1:
                    self.image.clip_draw(43, 1195-31, 16, 32, self.x, self.y)
                elif self.frame == 2:
                    self.image.clip_draw(62, 1195-31, 16, 32, self.x, self.y)
                elif self.frame == 3:
                    self.image.clip_draw(81, 1195-31, 16, 32, self.x, self.y)
                elif self.frame == 4:
                    self.image.clip_draw(62, 1195-31, 16, 32, self.x, self.y)
                elif self.frame == 5:
                    self.image.clip_draw(43, 1195-31, 16, 32, self.x, self.y)
            elif self.direction == Character_Direction_Right:
                if self.frame == 0:
                    self.image.clip_draw(24, 1195-99, 16, 32, self.x, self.y)
                elif self.frame == 1:
                    self.image.clip_draw(43, 1195-99, 16, 32, self.x, self.y)
                elif self.frame == 2:
                    self.image.clip_draw(62, 1195-99, 16, 32, self.x, self.y)
                elif self.frame == 3:
                    self.image.clip_draw(81, 1195-99, 17, 32, self.x, self.y)
                elif self.frame == 4:
                    self.image.clip_draw(62, 1195-99, 16, 32, self.x, self.y)
                elif self.frame == 5:
                    self.image.clip_draw(43, 1195-99, 16, 32, self.x, self.y)
            elif self.direction == Character_Direction_Down:
                if self.frame == 0:
                    self.image.clip_draw(24, 1195-165, 16, 32, self.x, self.y)
                elif self.frame == 1:
                    self.image.clip_draw(43, 1195-165, 16, 32, self.x, self.y)
                elif self.frame == 2:
                    self.image.clip_draw(62, 1195-165, 17, 32, self.x, self.y)
                elif self.frame == 3:
                    self.image.clip_draw(82, 1195-165, 17, 32, self.x, self.y)
                elif self.frame == 4:
                    self.image.clip_draw(62, 1195-165, 17, 32, self.x, self.y)
                elif self.frame == 5:
                    self.image.clip_draw(43, 1195-165, 16, 32, self.x, self.y)
        elif self.state == Character_State_Attack:
            if self.direction == Character_Direction_Left:
                if self.frame == 0:
                    self.image.clip_draw(122, 1195-231, 20, 32, self.x, self.y)
                elif self.frame == 1:
                    self.image.clip_draw(145, 1195-231, 25, 32, self.x-5, self.y)
                elif self.frame == 2:
                    self.image.clip_draw(145, 1195-231, 25, 32, self.x-5, self.y)
                elif self.frame == 3:
                    self.image.clip_draw(145, 1195-231, 25, 32, self.x-5, self.y)
            if self.direction == Character_Direction_Up:
                if self.frame == 0:
                    self.image.clip_draw(119, 1195-33, 19, 32, self.x, self.y)
                elif self.frame == 1:
                    self.image.clip_draw(141, 1195-33, 23, 32, self.x+4, self.y)
                elif self.frame == 2:
                    self.image.clip_draw(141, 1195-33, 23, 32, self.x+4, self.y)
                elif self.frame == 3:
                    self.image.clip_draw(141, 1195-33, 23, 32, self.x+4, self.y)
            if self.direction == Character_Direction_Right:
                if self.frame == 0:
                    self.image.clip_draw(120, 1195-99, 21, 32, self.x, self.y)
                elif self.frame == 1:
                    self.image.clip_draw(144, 1195-99, 23, 32, self.x+4, self.y)
                elif self.frame == 2:
                    self.image.clip_draw(144, 1195-99, 23, 32, self.x+4, self.y)
                elif self.frame == 3:
                    self.image.clip_draw(144, 1195-99, 23, 32, self.x+4, self.y)
            if self.direction == Character_Direction_Down:
                if self.frame == 0:
                    self.image.clip_draw(124, 1195-165, 20, 32, self.x, self.y)
                elif self.frame == 1:
                    self.image.clip_draw(147, 1195-165, 20, 32, self.x, self.y)
                elif self.frame == 2:
                    self.image.clip_draw(147, 1195-165, 20, 32, self.x, self.y)
                elif self.frame == 3:
                    self.image.clip_draw(147, 1195-16, 20, 32, self.x, self.y)

    def BoundBoxCheck(self):
        return False

    def update(self):

        if not self.BoundBoxCheck():
            if self.state == Character_State_Move:
                if self.direction == Character_Direction_Left:
                    if self.x > 120:
                        self.x -= 2 * self.speed
                if self.direction == Character_Direction_Right:
                    if self.x < 700:
                        self.x += 2 * self.speed
                if self.direction == Character_Direction_Up:
                    if self.y < 500:
                        self.y += 2 * self.speed
                if self.direction == Character_Direction_Down:
                    if self.y > 100:
                        self.y -= 2 * self.speed

        nowTime = time.time()

        if nowTime - self.frameTime > 0.1:
            self.frameTime = time.time()
            if self.state == Character_State_Move or Character_State_Idle:
                self.frame = (self.frame + 1) % 6
            elif self.state == Character_State_Attack:
                self.frame += 1
                if self.frame >= 3:
                    if self.isLeftButton or self.isRightButton or self.isUpButton or self.isDownButton:
                        self.state = Character_State_Move
                    else:
                        self.state = Character_State_Idle

        if self.state != Character_State_Attack:
            if self.isLeftButton or self.isRightButton or self.isUpButton or self.isDownButton:
                self.state = Character_State_Move
                if self.isLeftButton:
                    self.direction = Character_Direction_Left
                elif self.isUpButton:
                    self.direction = Character_Direction_Up
                elif self.isDownButton:
                    self.direction = Character_Direction_Down
                elif self.isRightButton:
                    self.direction = Character_Direction_Right
            else:
                self.state = Character_State_Idle

