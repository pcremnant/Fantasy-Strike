import pico2d
from game.package.basic_module.basic_define import *


class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        pass

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def move_position(self, x, y):
        self.x += x
        self.y -= y


class Status:

    def __init__(self, max_hp, move_speed, attack_power, attack_speed, attack_range):
        self.max_hp = max_hp
        self.current_hp = self.max_hp
        self.move_speed = move_speed
        self.attack_power = attack_power
        self.attack_speed = attack_speed
        self.attack_range = attack_range
        # add more status
        pass


class Image:

    def __init__(self, imgPath, imgType):
        self.image_type = imgType
        if imgType == IMAGE_TYPE_SPRITE:
            self.image = pico2d.load_image(imgPath)
        elif imgType == IMAGE_TYPE_FILES:
            self.image = []
            for path in imgPath:
                self.image.append(pico2d.load_image(path))
        self.max_frame = 0
        self.current_frame = 0
        self.mode_frame = 0
        self.image_width = 0
        self.image_height = 0
        self.is_draw = True

    def draw_image(self, x, y):
        if self.is_draw:
            if self.image_type == IMAGE_TYPE_SPRITE:
                self.image.clip_draw((self.current_frame // SUB_FRAME) * self.image_width,
                                     self.mode_frame * self.image_height,
                                     self.image_width, self.image_height, x, y)
            elif self.image_type == IMAGE_TYPE_FILES:
                self.image[self.current_frame // SUB_FRAME].clip_draw(0, 0,
                                                                      self.image_width, self.image_height, x, y)
            # self.current_frame += 1
            # self.current_frame = self.current_frame % self.max_frame
            self.current_frame += 1
            if self.current_frame / SUB_FRAME >= self.max_frame:
                self.current_frame = 0

    def draw_on_map(self, x, y, map_width, map_height, size_x, size_y):
        if self.is_draw:
            addW = map_width
            addH = map_height
            if size_x % 2 == 0:
                addW = 0
            if size_y % 2 == 0:
                addH = 0
            if self.image_type == IMAGE_TYPE_SPRITE:
                self.image.clip_draw((self.current_frame // SUB_FRAME) * self.image_width,
                                     self.mode_frame * self.image_height,
                                     self.image_width, self.image_height,
                                     x + addW / 2, y + addH / 2, map_width * size_x, map_height * size_y)
            elif self.image_type == IMAGE_TYPE_FILES:
                self.image[self.current_frame // SUB_FRAME].clip_draw(0, 0, self.image_width, self.image_height,
                                                                      x + addW / 2, y + addH / 2,
                                                                      map_width * size_x, map_height * size_y)
            self.current_frame += 1
            if self.current_frame / SUB_FRAME >= self.max_frame:
                self.current_frame = 0

    def set_image_frame(self, maxFrame, imgWidth, imgHeight):  # 이미지 초기 세팅
        self.max_frame = maxFrame  # 최대 프레임
        self.image_width = imgWidth  # 한 프레임의 너비
        self.image_height = imgHeight  # 한 프레임의 높이

    def set_frame_mode(self, action):
        if action < 0:
            return False
        self.mode_frame = action


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
    def tmp_draw_table(self):
        for y in range(0, BUILD_MAP_SIZE_Y - 1, 1):
            for x in range(0, BUILD_MAP_SIZE_X - 1, 1):
                pico2d.draw_rectangle(BUILD_TILE_START_X + x * BUILD_TILE_WIDTH,
                                      BUILD_TILE_START_Y + y * BUILD_TILE_HEIGHT,
                                      BUILD_TILE_START_X + (x + 1) * BUILD_TILE_WIDTH,
                                      BUILD_TILE_START_Y + (y + 1) * BUILD_TILE_HEIGHT)

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

    def build_pointer(self, x, y, size_x, size_y):
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


class Unit_Map:

    def __init__(self):
        self.unit_map = [[0 for x in range(UNIT_MAP_SIZE_X)] for y in range(UNIT_MAP_SIZE_Y)]
        self.init_unit_map()

    def init_unit_map(self):
        for y in range(UNIT_MAP_SIZE_Y):
            for x in range(UNIT_MAP_SIZE_X):
                self.unit_map[y][x] = True

    def tmp_draw_table(self):
        for y in range(0, UNIT_MAP_SIZE_Y, 1):
            for x in range(0, UNIT_MAP_SIZE_X, 1):
                pico2d.draw_rectangle(UNIT_MAP_START_X + x * UNIT_TILE_WIDTH,
                                      UNIT_MAP_START_Y + y * UNIT_TILE_HEIGHT,
                                      UNIT_MAP_START_X + (x + 1) * UNIT_TILE_WIDTH,
                                      UNIT_MAP_START_Y + (y + 1) * UNIT_TILE_HEIGHT)
