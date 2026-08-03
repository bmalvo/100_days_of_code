import random

def random_color():
    r = round(random.random(), 3)
    g = round(random.random(), 3)
    b = round(random.random(), 3)
    return r, g, b
