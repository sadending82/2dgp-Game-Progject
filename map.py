from pico2d import *

Door_None = 0
Door_Normal = 1
Door_Boss = 2


class FirstDungeonMap:
    def __init__(self):
        self.image = load_image('dungeon1_base.png')
        self.door_left_image = load_image('normal_door_left.png')
        self.door_right_image = load_image('normal_door_right.png')
        self.door_up_image = load_image('normal_door_up.png')
        self.door_down_image = load_image('normal_door_down.png')
        self.UpDoor = Door_None
        self.LeftDoor = Door_None
        self.DownDoor = Door_None
        self.RightDoor = Door_None
        self.BoundBox = {
            'wall': [[0, 600 - 518, 0 + 350, 600], [450, 600 - 518, 450 + 350, 600], [718, 600 - 350 - 168, 800, 350],
                     [0, 600 - 350 - 168, 82, 350], [0, 600 - 167 - 83, 82, 600 - 83], [0, 600 - 60, 350, 600],
                     [450, 600 - 60, 800, 600], [718, 600 - 250, 800, 600]],
            'door': [[0, 600 - 350, 82, 600 - 250], [350, 600 - 82, 600, 450],
                     [717, 600 - 350, 800, 600 - 250], [350, 0, 450, 600 - 518]],
            'door_open': [[0, 600 - 350, 60, 600 - 250], [350, 600 - 60, 600, 450],
                          [740, 600 - 350, 800, 600 - 250], [350, 0, 450, 600 - 540]]}
