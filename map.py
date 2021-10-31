from pico2d import *

Door_None = 0
Door_Normal = 1
Door_Boss = 2

Window_Height, Window_Width = get_canvas_height(), get_canvas_width()

class FirstDungeonMap:
    def __init__(self, isLeftDoor, isUpDoor, isRightDoor, isDownDoor):
        self.image = load_image('dungeon1_base.png')
        self.door_left_image = load_image('normal_door_left.png')
        self.door_right_image = load_image('normal_door_right.png')
        self.door_up_image = load_image('normal_door_up.png')
        self.door_down_image = load_image('normal_door_down.png')
        self.open_door_left_image = load_image('normal_door_left_open.png')
        self.open_door_right_image = load_image('normal_door_right_open.png')
        self.open_door_up_image = load_image('normal_door_up_open.png')
        self.open_door_down_image = load_image('normal_door_down_open.png')
        self.up_door = isUpDoor
        self.left_door = isLeftDoor
        self.down_door = isRightDoor
        self.right_door = isDownDoor
        self.bound_box = {
            'wall': [[0, 600 - 518, 0 + 350, 600], [450, 600 - 518, 450 + 350, 600], [718, 600 - 350 - 168, 800, 350],
                     [0, 600 - 350 - 168, 82, 350], [0, 600 - 167 - 83, 82, 600 - 83], [0, 600 - 60, 350, 600],
                     [450, 600 - 60, 800, 600], [718, 600 - 250, 800, 600]],
            'door': [[0, 600 - 350, 82, 600 - 250], [350, 600 - 82, 600, 450],
                     [717, 600 - 350, 800, 600 - 250], [350, 0, 450, 600 - 518]],
            'door_open': [[0, 600 - 350, 60, 600 - 250], [350, 600 - 60, 600, 450],
                          [740, 600 - 350, 800, 600 - 250], [350, 0, 450, 600 - 540]]}

    def draw(self, isDoorOpen):
        self.image.draw(Window_Width // 2, Window_Height // 2, Window_Width, Window_Height)
        if not isDoorOpen:
            if self.left_door == Door_Normal or self.left_door == Door_Boss:
                self.door_left_image.draw(0 + (82 // 2), 250 + (105 // 2))
            if self.up_door == Door_Normal or self.up_door == Door_Boss:
                self.door_up_image.draw(350 + (102 // 2), 517 + (85 // 2))
            if self.right_door == Door_Normal or self.right_door == Door_Boss:
                self.door_right_image.draw(717 + (82 // 2), 250 + (105 // 2))
            if self.down_door == Door_Normal or self.down_door == Door_Boss:
                self.door_down_image.draw(350 + (102 // 2), 0 + (85 // 2) + 1)
        else:
            if self.left_door == Door_Normal or self.left_door == Door_Boss:
                self.open_door_left_image.draw(0 + (82 // 2), 250 + (105 // 2))
            if self.up_door == Door_Normal or self.up_door == Door_Boss:
                self.open_door_up_image.draw(350 + (102 // 2), 517 + (85 // 2))
            if self.right_door == Door_Normal or self.right_door == Door_Boss:
                self.open_door_right_image.draw(717 + (82 // 2), 250 + (105 // 2))
            if self.down_door == Door_Normal or self.down_door == Door_Boss:
                self.open_door_down_image.draw(350 + (102 // 2), 0 + (85 // 2) + 1)




