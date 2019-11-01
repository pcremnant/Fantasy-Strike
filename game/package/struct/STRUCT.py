import pico2d
from ..define.DEFINE import *


class SPosition:

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


class SUnitStatus:

    def __init__(self):
        self.hp = 0
        self.attack_damage = 0
        self.move_speed = 0
        self.defence = 0
        self.attack_range = 0
        self.attack_speed = 0
        # add more status
        pass


class SImage:

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
        self.image_position = SPosition(0, 0)  # 이미지의 화면상 위치
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
                self.object_image.clip_draw(int(self.current_frame / FRAME_MOVE) * self.image_width,
                                            self.mode_frame * self.image_height,
                                            self.image_width, self.image_height,
                                            self.image_position.get_position_x() + addW / 2,
                                            self.image_position.get_position_y() + addH / 2,
                                            w * size_x, h * size_y)
            elif self.image_type == IMAGE_TYPE_FILES:
                self.object_image[self.current_frame // FRAME_MOVE].clip_draw(0, 0, self.image_width, self.image_height,
                                                                              self.image_position.get_position_x() + addW / 2,
                                                                              self.image_position.get_position_y() + addH / 2,
                                                                              w * size_x, h * size_y)
            self.current_frame += 1
            if self.current_frame / FRAME_MOVE >= self.max_frame:
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


class SBuild_Coord:

    def __init__(self):
        self.nTileWidth = BUILD_TILE_WIDTH
        self.nTileHeight = BUILD_TILE_HEIGHT
        self.nTileStartX = BUILD_MAP_SIZE_X_EDGE * BUILD_TILE_WIDTH
        self.nTileStartY = BUILD_MAP_SIZE_Y_EDGE * BUILD_TILE_HEIGHT

    def GetPositionX(self, x):
        nX = int((x - self.nTileStartX) / self.nTileWidth)
        return nX * self.nTileWidth + self.nTileStartX

    def GetPositionY(self, y):
        nY = int((y - self.nTileStartY) / self.nTileHeight)
        return nY * self.nTileHeight + self.nTileStartY

    def GetTileWidth(self):
        return self.nTileWidth

    def GetTileHeight(self):
        return self.nTileHeight

    def GetStartX(self):
        return self.nTileStartX

    def GetStartY(self):
        return self.nTileStartY


class SBuild_Map:

    def __init__(self, nSX, nSY, nTW, nTH):
        self.mapBuild = [[0 for x in range(BUILD_MAP_SIZE_X)] for y in range(BUILD_MAP_SIZE_Y)]
        self.nStartX = nSX
        self.nStartY = nSY
        self.nTileWidth = nTW
        self.nTileHeight = nTH
        for i in range(BUILD_MAP_SIZE_Y):
            for j in range(BUILD_MAP_SIZE_X):
                self.mapBuild[i][j] = True

    def InitTable(self):
        for i in range(BUILD_MAP_SIZE_Y):
            for j in range(BUILD_MAP_SIZE_X):
                self.mapBuild[i][j] = True

    # 해당 위치가 건설 가능한 곳인지 체크
    def CheckBuildable(self, x, y, sizeX, sizeY):
        nX = int((x - self.nStartX) / self.nTileWidth)
        nY = int((y - self.nStartY) / self.nTileHeight)

        if nX - sizeX / 2 < 0:
            return False
        if nY - sizeY / 2 < 0:
            return False

        for coordY in range(int(nY - sizeY / 2 + 0.5), int(nY + sizeY / 2 + 0.5), 1):
            for coordX in range(int(nX - sizeX / 2 + 0.5), int(nX + sizeX / 2 + 0.5), 1):
                if coordX >= BUILD_MAP_SIZE_X - 1 or coordX < 0:
                    return False
                elif coordY >= BUILD_MAP_SIZE_Y - 1 or coordY < 0:
                    return False
                elif not self.mapBuild[coordY][coordX]:
                    return False

        return True

    def tmpDrawTable(self):
        for y in range(0, BUILD_MAP_SIZE_Y - 1, 1):
            for x in range(0, BUILD_MAP_SIZE_X - 1, 1):
                pico2d.draw_rectangle(self.nStartX + x * self.nTileWidth, self.nStartY + y * self.nTileHeight,
                                      self.nStartX + (x + 1) * self.nTileWidth,
                                      self.nStartY + (y + 1) * self.nTileHeight)

    def BuildObject(self, x, y, sizeX, sizeY):
        if not self.CheckBuildable(x, y, sizeX, sizeY):
            return False

        nX = int((x - self.nStartX) / self.nTileWidth)
        nY = int((y - self.nStartY) / self.nTileHeight)

        for coordY in range(int(nY - sizeY / 2 + 0.5), int(nY + sizeY / 2 + 0.5), 1):
            for coordX in range(int(nX - sizeX / 2 + 0.5), int(nX + sizeX / 2 + 0.5), 1):
                if coordX >= BUILD_MAP_SIZE_X - 1 or coordX < 0:
                    return False
                elif coordY >= BUILD_MAP_SIZE_Y - 1 or coordY < 0:
                    return False
                else:
                    self.mapBuild[coordY][coordX] = False

        return True

    def BuildPointer(self, x, y, sizeX, sizeY):
        nX = int((x - self.nStartX) / self.nTileWidth)
        nY = int((y - self.nStartY) / self.nTileHeight)

        if nX >= BUILD_MAP_SIZE_X - 1 or nY >= BUILD_MAP_SIZE_Y - 1:
            return False
        elif nX <= 0 or nY <= 0:
            return False
        elif self.CheckBuildable(x, y, sizeX, sizeY):
            imgTile = SImage("tmpImage/tile_g.png", IMAGE_TYPE_SPRITE)
            imgTile.set_position(nX * self.nTileWidth + self.nStartX,
                                 nY * self.nTileHeight + self.nStartY)
            imgTile.set_image_frame(1, 64, 64)
            imgTile.draw_on_build_map(self.nTileWidth, self.nTileHeight, sizeX, sizeY)
        else:
            imgTile = SImage("tmpImage/tile_r.png", IMAGE_TYPE_SPRITE)
            imgTile.set_position(nX * self.nTileWidth + self.nStartX,
                                 nY * self.nTileHeight + self.nStartY)
            imgTile.set_image_frame(1, 64, 64)
            imgTile.draw_on_build_map(self.nTileWidth, self.nTileHeight, sizeX, sizeY)

        return True
