import pico2d
from game.package.basic_module.basic_define import *


class Position:

    def __init__(self, nX, nY):
        self.x = nX
        self.y = nY
        pass

    def set_position(self, nX, nY):
        self.x = nX
        self.y = nY

    def move_position(self, nX, nY):
        self.x += nX
        self.y -= nY

    def get_position_x(self):
        return self.x

    def get_position_y(self):
        return self.y

    def get_position(self):
        return self.x, self.y


class Unit_Status:

    def __init__(self):
        self.hp = 0
        self.attack_damage = 0
        self.move_speed = 0
        self.defence = 0
        self.attack_range = 0
        self.attack_speed = 0
        # add more status
        pass


class Image:

    def __init__(self, imgPath, imgType):
        self.image_type = imgType
        if imgType == IMAGE_TYPE_SPRITE:
            self.object_image = pico2d.load_image(imgPath)  # 이미지 로딩
        elif imgType == IMAGE_TYPE_FILES:
            self.object_image = []
            for path in imgPath:
                self.object_image.append(pico2d.load_image(path))
        self.max_frame = 0  # 최대 프레임
        self.current_frame = 0  # 현재 프레임
        self.mode_frame = 0  # 현재 이미지의 행동
        self.image_width = 0  # 한 프레임의 너비
        self.image_height = 0  # 한 프레임의 높이
        self.image_position = Position(0, 0)  # 이미지의 화면상 위치
        self.is_draw = True  # 이미지 렌더링 여부

    def draw_image(self):  # 이미지 렌더링
        if self.is_draw:
            if self.image_type == IMAGE_TYPE_SPRITE:
                self.object_image.clip_draw(self.current_frame * self.image_width, self.mode_frame * self.image_height,
                                            self.image_width, self.image_height, self.image_position.get_position_x(),
                                            self.image_position.get_position_y())
            elif self.image_type == IMAGE_TYPE_FILES:
                self.object_image[self.current_frame].clip_draw(self.image_width, self.image_height,
                                                                self.image_width, self.image_height,
                                                                self.image_position.get_position_x(),
                                                                self.image_position.get_position_y())
            self.current_frame += 1
            self.current_frame = self.current_frame % self.max_frame

    def draw_on_build_map(self, w, h, size_x, size_y):  # 이미지 렌더링
        if self.is_draw:
            addW = w
            addH = h
            if size_x % 2 == 0:
                addW = 0
            if size_y % 2 == 0:
                addH = 0
            if self.image_type == IMAGE_TYPE_SPRITE:
                self.object_image.clip_draw((self.current_frame // SUB_FRAME) * self.image_width,
                                            self.mode_frame * self.image_height,
                                            self.image_width, self.image_height,
                                            self.image_position.get_position_x() + addW / 2,
                                            self.image_position.get_position_y() + addH / 2,
                                            w * size_x, h * size_y)
            elif self.image_type == IMAGE_TYPE_FILES:
                self.object_image[self.current_frame // SUB_FRAME].clip_draw(0, 0, self.image_width, self.image_height,
                                                                              self.image_position.get_position_x() + addW / 2,
                                                                              self.image_position.get_position_y() + addH / 2,
                                                                              w * size_x, h * size_y)
            self.current_frame += 1
            if self.current_frame / SUB_FRAME >= self.max_frame:
                self.current_frame = 0

    def move_position(self, x, y):  # 이미지 위치 이동
        self.image_position.move_position(x, y)

    def set_position(self, x, y):
        self.image_position.x, self.image_position.y = x, y

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

    # 해당 위치가 건설 가능한 곳인지 체크
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
            imgTile = Image("tmpImage/tile_g.png", IMAGE_TYPE_SPRITE)
            imgTile.set_position(tile_x * BUILD_TILE_WIDTH + BUILD_TILE_START_X,
                                 tile_y * BUILD_TILE_HEIGHT + BUILD_TILE_START_Y)
            imgTile.set_image_frame(1, 64, 64)
            imgTile.draw_on_build_map(BUILD_TILE_WIDTH, BUILD_TILE_HEIGHT, size_x, size_y)
        else:
            imgTile = Image("tmpImage/tile_r.png", IMAGE_TYPE_SPRITE)
            imgTile.set_position(tile_x * BUILD_TILE_WIDTH + BUILD_TILE_START_X,
                                 tile_y * BUILD_TILE_HEIGHT + BUILD_TILE_START_Y)
            imgTile.set_image_frame(1, 64, 64)
            imgTile.draw_on_build_map(BUILD_TILE_WIDTH, BUILD_TILE_HEIGHT, size_x, size_y)

        return True
