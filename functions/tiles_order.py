import math


class TileClass:
    _types = {
        'Bailarina': {
            'colors': ['#ede9e5',
                       '#d1a971',
                       '#004851',
                       '#76442e',
                       '#7d9e9e',
                       '#964933'],
            'face_width': 16.2,
            'numVertices': 3
            }
        }

    def __init__(self, tile):
        self.colors = self._types[tile]['colors']
        self.face_width = self._types[tile]['face_width']
        self.numVertices = self._types[tile]['numVertices']
        self.type = tile

    def get_radius(self):
        radius = math.sin(360 / self.numVertices) * self.face_width
        return radius

    def get_height(self):
        if self.type == 'Bailarina':
            height = (self.face_width ** 2 - (
                    self.face_width / 2.0) ** 2) ** 0.5
        else:
            height = None
        return height

    def get_area(self):
        if self.type == 'Bailarina':
            area = ((3 ** 0.5) / 4) * (self.face_width ** 2)
        else:
            area = None
        return area


class Wall:
    def __init__(self, height, width):
        self.height = height
        self.width = width

    def get_area(self):
        area = self.height * self.width
        return area


class Order:
    def __init__(self, wall, tileclass):
        self.wall = wall
        self.tile = tileclass
        self.colors_share = dict((color, 1) for color in self.tile.colors)
        qty_by_color = self.get_init_qty_by_color()
        self.qty_by_colors = dict(
                (color, qty_by_color) for color in self.tile.colors)

    def get_init_qty_by_color(self):
        wall_area = self.wall.get_area()
        tile_area = self.tile.get_area()
        qty_colors = len(self.tile.colors)
        qty = wall_area / tile_area
        return math.ceil(qty / qty_colors)

    def get_qty_tiles(self):
        return sum(self.qty_by_colors.values())

    def set_color_share(self, color, qty):
        self.colors_share[color] = qty
        self.update_qty_by_color()
        print(color, 'updated')
        for color in self.colors_share.keys():
            print(color, '-->', self.colors_share[color])

    def update_qty_by_color(self):
        total_share = sum(self.colors_share.values())
        total_tiles = self.get_qty_tiles()
        for color in self.tile.colors:
            share = self.colors_share[color] / total_share
            qty = math.ceil(total_tiles * share)
            self.qty_by_colors[color] = qty

    def get_tiles(self):
        tiles = []
        for color in self.qty_by_colors.keys():
            tiles.extend([color] * self.qty_by_colors[color])
        return tiles
