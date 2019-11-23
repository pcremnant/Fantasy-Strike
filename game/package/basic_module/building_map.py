from game.package.basic_module.basic_define import BUILD_MAP_SIZE_X, BUILD_MAP_SIZE_Y, BUILD_TILE_START_X, \
    BUILD_TILE_WIDTH, BUILD_TILE_START_Y, BUILD_TILE_HEIGHT, IMAGE_TYPE_SPRITE
from game.package.basic_module.basic_struct import Image


class Build_Map:

    def __init__(self):
        self.build_map = [[0 for x in range(BUILD_MAP_SIZE_X)] for y in range(BUILD_MAP_SIZE_Y)]
        self.init_build_map()

    def init_build_map(self):
        for y in range(BUILD_MAP_SIZE_Y):
            for x in range(BUILD_MAP_SIZE_X):
                self.build_map[y][x] = True

    def check_is_buildable(self, x, y, size_x, size_y):
        tile_x = int((x - BUILD_TILE_START_X) / BUILD_TILE_WIDTH)
        tile_y = int((y - BUILD_TILE_START_Y) / BUILD_TILE_HEIGHT)

        if tile_x - size_x / 2 < 0:
            return False
        if tile_y - size_y / 2 < 0:
            return False

        for coord_y in range(int(tile_y - size_y / 2 + 0.5), int(tile_y + size_y / 2 + 0.5), 1):
            for coord_x in range(int(tile_x - size_x / 2 + 0.5), int(tile_x + size_x / 2 + 0.5), 1):
                if coord_x >= BUILD_MAP_SIZE_X - 1 or coord_x < 0:
                    return False
                elif coord_y >= BUILD_MAP_SIZE_Y - 1 or coord_y < 0:
                    return False
                elif not self.build_map[coord_y][coord_x]:
                    return False

        return True

    # tmp code : draw build map table ---------------------------------------------------

    # ------------------------------------------------------------------------------------

    def build_object(self, x, y, size_x, size_y):
        if not self.check_is_buildable(x, y, size_x, size_y):
            return False

        tile_x = int((x - BUILD_TILE_START_X) / BUILD_TILE_WIDTH)
        tile_y = int((y - BUILD_TILE_START_Y) / BUILD_TILE_HEIGHT)

        for coord_y in range(int(tile_y - size_y / 2 + 0.5), int(tile_y + size_y / 2 + 0.5), 1):
            for coord_x in range(int(tile_x - size_x / 2 + 0.5), int(tile_x + size_x / 2 + 0.5), 1):
                if coord_x >= BUILD_MAP_SIZE_X - 1 or coord_x < 0:
                    return False
                elif coord_y >= BUILD_MAP_SIZE_Y - 1 or coord_y < 0:
                    return False
                else:
                    self.build_map[coord_y][coord_x] = False

        return True

    def show_is_buildable(self, x, y, size_x, size_y):
        tile_x = int((x - BUILD_TILE_START_X) / BUILD_TILE_WIDTH)
        tile_y = int((y - BUILD_TILE_START_Y) / BUILD_TILE_HEIGHT)

        if tile_x >= BUILD_MAP_SIZE_X - 1 or tile_y >= BUILD_MAP_SIZE_Y - 1:
            return False
        elif tile_x <= 0 or tile_y <= 0:
            return False
        elif self.check_is_buildable(x, y, size_x, size_y):
            imgTile = Image("resource/UI/tile_g.png", IMAGE_TYPE_SPRITE)
            imgTile.set_image_frame(1, 64, 64)
            imgTile.draw_on_map(tile_x * BUILD_TILE_WIDTH + BUILD_TILE_START_X,
                                tile_y * BUILD_TILE_HEIGHT + BUILD_TILE_START_Y,
                                BUILD_TILE_WIDTH, BUILD_TILE_HEIGHT, size_x, size_y)
        else:
            imgTile = Image("resource/UI/tile_r.png", IMAGE_TYPE_SPRITE)
            imgTile.set_image_frame(1, 64, 64)
            imgTile.draw_on_map(tile_x * BUILD_TILE_WIDTH + BUILD_TILE_START_X,
                                tile_y * BUILD_TILE_HEIGHT + BUILD_TILE_START_Y,
                                BUILD_TILE_WIDTH, BUILD_TILE_HEIGHT, size_x, size_y)

        return True
