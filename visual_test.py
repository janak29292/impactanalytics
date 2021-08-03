from random import randint

from rectangle import get_vertices

import matplotlib.pyplot as plt
import matplotlib.patches as patches


def random_rectangles(x):
    rand_list = []
    for i in range(randint(1, x)):
        a = randint(1, x - 1)
        b = randint(a + 1, x)
        h = randint(1, x)
        rand_list.append((a, b, h))
    return rand_list


def test(rects=None):
    if not rects:
        rects = random_rectangles(10)
    vertices = get_vertices(rects)
    print(rects)
    print(vertices)

    fig, ax = plt.subplots()

    ax.scatter(*zip(*vertices))

    for i in rects:
        ax.add_patch(patches.Rectangle((i[0], 0), i[1] - i[0], i[2], edgecolor='black', facecolor='none'))

    plt.show()


if __name__ == '__main__':
    test()
