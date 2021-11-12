# layer 0 : Background
# layer 1 : Main

objects = [[],[]]


def add_object(o, layer):
    objects[layer].append(o)


def add_objects(l, layer):
    objects[layer] += l


def remove_object(o):
    for i in range(len(objects)):
        if o in objects[i]:
            objects[i].remove(o)
            del o
            break


def clear():
    for o in all_objects():
        del o
    for l in objects:
        l.clear()


def is_in_objects(object_class):
    for i in range(2):
        for j in objects[i]:
            if type(object_class) == type(j):
                return True
    return False


def return_object(object_class):
    for i in range(2):
        for j in objects[i]:
            if type(object_class) == type(j):
                return j


def sort_objects(layer):
    sort_list = []
    count = 0
    for i in objects[layer]:
        sort_list.append((i.y, count))
        count += 1

    sort_list.sort(key=lambda x: x[0])

    new_obj = list(range(len(objects[layer])))
    count = 0
    for i in sort_list:
        new_obj[count] = objects[layer][i[1]]
        count += 1

    new_obj.reverse()

    objects[layer].clear()

    for i in new_obj:
        objects[layer].append(i)






def all_objects():
    for i in range(len(objects)):
        for o in objects[i]:
            yield o

