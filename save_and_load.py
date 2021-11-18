import pathlib
import Character


def load_data():
    fileName = r"save_data.dat"
    fileObj = pathlib.Path(fileName)
    if pathlib.Path.is_file(fileObj):
        f = open('save_data.dat', 'r')
        Chara = Character.Hero()
        line = f.readline()
        Chara.x = int(line)
        line = f.readline()
        Chara.y = int(line)
        line = f.readline()
        Chara.state = int(line)
        line = f.readline()
        Chara.Hp = int(line)
        line = f.readline()
        Chara.Gold = int(line)
        line = f.readline()
        Chara.direction = int(line)
        line = f.readline()
        Chara.speed = int(line)
        line = f.readline()
        door = int(line)

        if door == 0:
            Chara.direction = Character.Character_Direction_Left
        elif door == 1:
            Chara.direction = Character.Character_Direction_Up
        elif door == 2:
            Chara.direction = Character.Character_Direction_Right
        elif door == 3:
            Chara.direction = Character.Character_Direction_Down

        while True:
            line = f.readline()
            if not line:
                break
            Chara.inventory.append(int(line))

    return Chara





def save_data(chara, door_num):
    f = open('save_data.dat', 'w')
    posx = str(chara.x)
    posy = str(chara.y)
    state = str(chara.state)
    Hp = str(chara.Hp)
    Gold = str(chara.Gold)
    direction = str(chara.direction)
    speed = str(chara.speed)
    door = str(door_num)

    f.write(posx+"\n")
    f.write(posy+"\n")
    f.write(state+"\n")
    f.write(Hp+"\n")
    f.write(Gold+"\n")
    f.write(direction+"\n")
    f.write(speed+"\n")
    f.write(door+"\n")
    for i in chara.inventory:
        item = str(i)
        f.write(item + "\n")
