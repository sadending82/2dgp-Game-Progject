# layer 0 : Background
# layer 1 : Main

objects = [[],[]]


def add_object(o, layer):
    objects[layer].append(o)


def add_objects(l, layer):
    objects[layer] += 1


def remove_object(o):
    for i in range(len(objects)):
        if o in objects[i]:
            objects[i].remove(o)
            del o
            break


def all_objects():
    for i in range(len(objects)):
        for o in objects[i]:
            yield o

