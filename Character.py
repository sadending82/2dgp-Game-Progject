from pico2d import *
import math
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

Window_Width, Window_Height = get_canvas_width(), get_canvas_height()


class Hero:
    def __init__(self):
        self.x = Window_Width // 2
        self.y = Window_Height // 2
        self.state = Character_State_Idle
        self.MaxHp = 100
        self.Hp = 100
        self.hp_bar = load_image('HP_Bar.png')
        self.hp_point = load_image('HP_Point.png')
        self.Gold = 0
        self.frame = 0
        self.damage = 1
        self.is_invincible = False
        self.invincible_timer = 0.0
        self.direction = Character_Direction_Right
        self.image = load_image('izuna_cheking2.png')
        self.punch_image = load_image('punch.png')
        self.frameTime = time.time()
        self.isLeftButton = False
        self.isRightButton = False
        self.isDownButton = False
        self.isUpButton = False
        self.bound_box = {
            'body': [self.x - 8, self.y - 16, self.x + 8, self.y + 16],
            'attack_left': [self.x - 24, self.y - 8, self.x - 8, self.y + 8],
            'attack_right': [self.x + 8, self.y - 8, self.x + 24, self.y + 8],
            'attack_up': [self.x - 8, self.y + 8, self.x + 8, self.y + 24],
            'attack_down': [self.x - 8, self.y - 24, self.x + 8, self.y - 8],
        }
        self.eff_bound_box = []
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
                    self.punch_image.clip_composite_draw(0, 0, 16, 16, math.radians(180), '',
                        (self.bound_box['attack_left'][0] + self.bound_box['attack_left'][2])//2,
                        (self.bound_box['attack_left'][1] + self.bound_box['attack_left'][3])//2)
                elif self.frame == 2:
                    self.image.clip_draw(145, 1195-231, 25, 32, self.x-5, self.y)
                    self.punch_image.clip_composite_draw(0, 0, 16, 16, math.radians(180), '',
                        (self.bound_box['attack_left'][0] + self.bound_box['attack_left'][2])//2,
                        (self.bound_box['attack_left'][1] + self.bound_box['attack_left'][3])//2)
                elif self.frame == 3:
                    self.image.clip_draw(145, 1195-231, 25, 32, self.x-5, self.y)
                    self.punch_image.clip_composite_draw(0, 0, 16, 16, math.radians(180), '',
                        (self.bound_box['attack_left'][0] + self.bound_box['attack_left'][2])//2,
                        (self.bound_box['attack_left'][1] + self.bound_box['attack_left'][3])//2)
            if self.direction == Character_Direction_Up:
                if self.frame == 0:
                    self.image.clip_draw(119, 1195-33, 19, 32, self.x, self.y)
                elif self.frame == 1:
                    self.punch_image.clip_composite_draw(0, 0, 16, 16, math.radians(90), '',
                        (self.bound_box['attack_up'][0] + self.bound_box['attack_up'][2])//2,
                        (self.bound_box['attack_up'][1] + self.bound_box['attack_up'][3])//2)
                    self.image.clip_draw(141, 1195-33, 23, 32, self.x+4, self.y)
                elif self.frame == 2:
                    self.punch_image.clip_composite_draw(0, 0, 16, 16, math.radians(90), '',
                        (self.bound_box['attack_up'][0] + self.bound_box['attack_up'][2])//2,
                        (self.bound_box['attack_up'][1] + self.bound_box['attack_up'][3])//2)
                    self.image.clip_draw(141, 1195-33, 23, 32, self.x+4, self.y)
                elif self.frame == 3:
                    self.punch_image.clip_composite_draw(0, 0, 16, 16, math.radians(90), '',
                        (self.bound_box['attack_up'][0] + self.bound_box['attack_up'][2])//2,
                        (self.bound_box['attack_up'][1] + self.bound_box['attack_up'][3])//2)
                    self.image.clip_draw(141, 1195-33, 23, 32, self.x+4, self.y)
            if self.direction == Character_Direction_Right:
                if self.frame == 0:
                    self.image.clip_draw(120, 1195-99, 21, 32, self.x, self.y)
                elif self.frame == 1:
                    self.image.clip_draw(144, 1195-99, 23, 32, self.x+4, self.y)
                    self.punch_image.clip_composite_draw(0, 0, 16, 16, math.radians(0), '',
                        (self.bound_box['attack_right'][0] + self.bound_box['attack_right'][2])//2,
                        (self.bound_box['attack_right'][1] + self.bound_box['attack_right'][3])//2)
                elif self.frame == 2:
                    self.image.clip_draw(144, 1195-99, 23, 32, self.x+4, self.y)
                    self.punch_image.clip_composite_draw(0, 0, 16, 16, math.radians(0), '',
                        (self.bound_box['attack_right'][0] + self.bound_box['attack_right'][2])//2,
                        (self.bound_box['attack_right'][1] + self.bound_box['attack_right'][3])//2)
                elif self.frame == 3:
                    self.image.clip_draw(144, 1195-99, 23, 32, self.x+4, self.y)
                    self.punch_image.clip_composite_draw(0, 0, 16, 16, math.radians(0), '',
                        (self.bound_box['attack_right'][0] + self.bound_box['attack_right'][2])//2,
                        (self.bound_box['attack_right'][1] + self.bound_box['attack_right'][3])//2)
            if self.direction == Character_Direction_Down:
                if self.frame == 0:
                    self.image.clip_draw(124, 1195-165, 20, 32, self.x, self.y)
                elif self.frame == 1:
                    self.image.clip_draw(147, 1195-165, 20, 32, self.x, self.y)
                    self.punch_image.clip_composite_draw(0, 0, 16, 16, math.radians(-90), '',
                        (self.bound_box['attack_down'][0] + self.bound_box['attack_down'][2])//2,
                        (self.bound_box['attack_down'][1] + self.bound_box['attack_down'][3])//2)
                elif self.frame == 2:
                    self.image.clip_draw(147, 1195-165, 20, 32, self.x, self.y)
                    self.punch_image.clip_composite_draw(0, 0, 16, 16, math.radians(-90), '',
                        (self.bound_box['attack_down'][0] + self.bound_box['attack_down'][2])//2,
                        (self.bound_box['attack_down'][1] + self.bound_box['attack_down'][3])//2)
                elif self.frame == 3:
                    self.image.clip_draw(147, 1195-16, 20, 32, self.x, self.y)
                    self.punch_image.clip_composite_draw(0, 0, 16, 16, math.radians(-90), '',
                        (self.bound_box['attack_down'][0] + self.bound_box['attack_down'][2])//2,
                        (self.bound_box['attack_down'][1] + self.bound_box['attack_down'][3])//2)
        # draw_rectangle(*self.get_bb())
        draw_rectangle(*self.get_attack_bb())
        self.hp_bar.draw(120, 580)
        cur_hp = int((150 * (1 - ((self.MaxHp - self.Hp)/self.MaxHp))))
        self.hp_point.clip_draw(0, 0, cur_hp, 30, 94 - (self.MaxHp - cur_hp)//2, 580)

    def get_bb(self):
        return self.bound_box['body'][0], self.bound_box['body'][1],\
               self.bound_box['body'][2], self.bound_box['body'][3]

    def get_attack_bb(self):
        if self.direction == Character_Direction_Left:
            return self.bound_box['attack_left'][0], self.bound_box['attack_left'][1], \
                   self.bound_box['attack_left'][2], self.bound_box['attack_left'][3]
        elif self.direction == Character_Direction_Right:
            return self.bound_box['attack_right'][0], self.bound_box['attack_right'][1], \
                   self.bound_box['attack_right'][2], self.bound_box['attack_right'][3]
        elif self.direction == Character_Direction_Up:
            return self.bound_box['attack_up'][0], self.bound_box['attack_up'][1], \
                   self.bound_box['attack_up'][2], self.bound_box['attack_up'][3]
        elif self.direction == Character_Direction_Down:
            return self.bound_box['attack_down'][0], self.bound_box['attack_down'][1], \
                   self.bound_box['attack_down'][2], self.bound_box['attack_down'][3]

    def attacked(self, damage):


    def update(self):

        if self.state == Character_State_Move:
            if self.direction == Character_Direction_Left:
                self.x -= 2 * self.speed
            if self.direction == Character_Direction_Right:
                self.x += 2 * self.speed
            if self.direction == Character_Direction_Up:
                self.y += 2 * self.speed
            if self.direction == Character_Direction_Down:
                self.y -= 2 * self.speed

        self.bound_box = {
            'body': [self.x - 8, self.y - 16, self.x + 8, self.y + 16],
            'attack_left': [self.x - 24, self.y - 8, self.x - 8, self.y + 8],
            'attack_right': [self.x + 8, self.y - 8, self.x + 24, self.y + 8],
            'attack_up': [self.x - 8, self.y + 8, self.x + 8, self.y + 24],
            'attack_down': [self.x - 8, self.y - 24, self.x + 8, self.y - 8],
        }

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

