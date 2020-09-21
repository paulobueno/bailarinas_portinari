import math
from random import shuffle

import matplotlib.patches as mpatches
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection

from functions import tiles_order as to

bailarinas = to.TileClass('Bailarina')
parede = to.Wall(246, 96)
pedido = to.Order(parede, bailarinas)


def wall_preview(order):
    fig, ax = plt.subplots()
    tiles = order.get_tiles()
    face_width = order.tile.face_width
    numvertices = order.tile.numVertices
    radius = order.tile.get_radius()
    height = order.tile.get_height()
    qty_x_tiles = math.ceil(order.wall.width / face_width)
    qty_y_tiles = math.ceil(order.wall.height / height)
    patches = []

    for row in range(qty_y_tiles):
        for column in range(qty_x_tiles):
            x0 = face_width / 2
            y0 = height - radius
            polygon = mpatches.RegularPolygon(
                    (x0 + (face_width * column), y0 + (height * row)),
                    numvertices,
                    radius=radius,
                    orientation=0
                    )
            patches.append(polygon)

    for row in range(qty_y_tiles):
        for column in range(qty_x_tiles + 1):
            x0 = 0
            y0 = radius
            polygon = mpatches.RegularPolygon(
                    (x0 + (face_width * column), y0 + (height * row)),
                    numvertices,
                    radius=radius,
                    orientation=math.pi
                    )
            patches.append(polygon)

    covers = []
    for i in range(3):
        coord = [
            (-order.tile.face_width, 0),
            (order.wall.width, 0),
            (-order.tile.face_width, order.wall.height),
            ]
        rectangle = mpatches.Rectangle(coord[i], order.tile.face_width,
                                       order.wall.height)
        if i == 2:
            rectangle = mpatches.Rectangle(coord[i],
                                           order.tile.face_width * 2 +
                                           order.wall.width,
                                           order.tile.face_width * 2)

        covers.append(rectangle)

    collection = PatchCollection(patches)
    shuffle(tiles)
    collection.set_facecolor(tiles)
    ax.add_collection(collection)
    cover = PatchCollection(covers)
    cover.set_facecolor('#ffffff')
    ax.add_collection(cover)
    plt.axis('equal')
    plt.axis('off')
    plt.show()


wall_preview(pedido)
