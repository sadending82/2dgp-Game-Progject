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
        self.is_door_open = False
        self.up_door = isUpDoor
        self.left_door = isLeftDoor
        self.down_door = isRightDoor
        self.right_door = isDownDoor
        self.bound_box = {
            'wall': [[0, 0, 0 + 350, 82], [450, 0, 450 + 350, 600 - 518], [718, 82, 800, 250],
                     [0, 82, 82, 250], [0, 350, 82, 540], [0, 540, 350, 600],
                     [450, 540, 800, 600], [718, 350, 800, 540]],
            'door': [[0, 250, 82, 350], [350, 540, 450, 600],
                     [717, 250, 800, 350], [350, 0, 450, 82]]
        }

    def update(self):
        pass

    def get_bb(self, category, num):
        return self.bound_box[category][num][0], self.bound_box[category][num][1],\
               self.bound_box[category][num][2], self.bound_box[category][num][3]

    def draw(self):
        self.image.draw(Window_Width // 2, Window_Height // 2, Window_Width, Window_Height)
        if not self.is_door_open:
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

        for i in range(8):
            draw_rectangle(*self.get_bb('wall', i))

        for i in range(4):
            draw_rectangle(*self.get_bb('door', i))



