photo = 3072 * 4096 * 24
photos = photo * 150

def first_way(photos):
    speed = 4 * 1024 * 1024* 8
    return photos / speed


def second_way(photos):
    speed = 4 * 1024 * 1024 * 8
    data = photos / 2
    time = 150 * 0.1 + (data / speed)
    return time
print(first_way(photos))
print(second_way(photos))
print(first_way(photos) - second_way(photos))
#2 691185
