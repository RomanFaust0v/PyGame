import random
from ground import Platform
from pygame import sprite

def generateLevel(w_h, w_w, p_h, p_w):
    stepper = {
        "wallCount": 200,
        "padding": 2,
        'x': int(w_w//p_w//2),
        'y': int(w_h//p_h//2),
    }
    def levelRow():
        return ["#"]* int(w_w//p_w)

    level = [levelRow() for _ in range(w_h//p_h)]

    while stepper['wallCount'] >= 0:
        x = stepper['x']
        y = stepper['y']

        if level[y][x] == "#":
            level[y][x] = " "
            stepper['wallCount'] -= 1
        roll = random.randint(1, 4)

        if roll == 1 and x > stepper['padding']:
            stepper['x'] -= 1
        if roll == 2 and x < w_w//p_w- 1 - stepper['padding']:
            stepper['x'] += 1
        if roll == 3 and y > stepper['padding']:
            stepper['y'] -= 1
        if roll == 4 and y < w_h//p_h - 1 - stepper['padding']:
            stepper['y'] += 1

    platform_group = sprite.Group()
    for i,row in enumerate(level):
        for j,wall in enumerate(row):
            if wall == "#":
                platform = Platform(j*p_w, i*p_h, p_h, p_w)
                platform_group.add(platform)
    return platform_group, level
