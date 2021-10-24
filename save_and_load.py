import os
import Character
myFolder = os.getcwd() + '/SaveData.dat'

def load_data():
    try:
        with open(myFolder) as file:
            chara = Character.Hero()
            line = file.readline()
            chara.x = int(line)
            line = file.readline()
    except FileNotFoundError:
        return None
