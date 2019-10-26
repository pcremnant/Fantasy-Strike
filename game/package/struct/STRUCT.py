import pico2d
from ..define.DEFINE import *


class SPosition:

    def __init__(self, nX, nY):
        self.x = nX
        self.y = nY
        pass

    def SetPosition(self, nX, nY):
        self.x = nX
        self.y = nY

    def MovePosition(self, nX, nY):
        self.x += nX
        self.y -= nY

    def GetPositionX(self):
        return self.x

    def GetPositionY(self):
        return self.y


class SUnitStatus:

    def __init__(self):
        self.nHp = 0
        self.nAttack = 0
        self.nSpeed = 0
        self.nDefend = 0
        self.nAttackRange = 0
        self.nAttackSpeed = 0
        # add more status
        pass


class SImage:

    def __init__(self, imgPath):
        self.imgObjectImage = pico2d.load_image(imgPath)  # 이미지 로딩
        self.nMaxFrame = 0  # 최대 프레임
        self.nCurFrame = 0  # 현재 프레임
        self.nFrameMode = 0  # 현재 이미지의 행동
        self.nImageWidth = 0  # 한 프레임의 너비
        self.nImageHeight = 0  # 한 프레임의 높이
        self.posImagePosition = SPosition(0, 0)  # 이미지의 화면상 위치
        self.bIsDraw = True  # 이미지 렌더링 여부

    def DrawImage(self):  # 이미지 렌더링
        if self.bIsDraw:
            self.imgObjectImage.clip_draw(self.nCurFrame * self.nImageWidth, self.nFrameMode * self.nImageHeight,
                                          self.nImageWidth, self.nImageHeight, self.posImagePosition.GetPositionX(),
                                          self.posImagePosition.GetPositionY())
            self.nCurFrame += 1
            self.nCurFrame = self.nCurFrame % self.nMaxFrame

    def DrawImage_Scaled(self, w, h, sizeX, sizeY):  # 이미지 렌더링
        if self.bIsDraw:
            addW = w
            addH = h
            if sizeX % 2 == 0:
                addW = 0
            if sizeY % 2 == 0:
                addH = 0
            self.imgObjectImage.clip_draw(int(self.nCurFrame / FRAME_MOVE) * self.nImageWidth,
                                          self.nFrameMode * self.nImageHeight,
                                          self.nImageWidth, self.nImageHeight,
                                          self.posImagePosition.GetPositionX() + addW / 2,
                                          self.posImagePosition.GetPositionY() + addH / 2,
                                          w * sizeX, h * sizeY)
            self.nCurFrame += 1
            if self.nCurFrame / FRAME_MOVE >= self.nMaxFrame:
                self.nCurFrame = 0

    def MovePosition(self, x, y):  # 이미지 위치 이동
        self.posImagePosition.MovePosition(x, y)

    def SetPosition(self, x, y):
        self.posImagePosition.PosX, self.posImagePosition.PosY = x, y

    def SetImageFrame(self, maxFrame, imgWidth, imgHeight):  # 이미지 초기 세팅
        self.nMaxFrame = maxFrame  # 최대 프레임
        self.nImageWidth = imgWidth  # 한 프레임의 너비
        self.nImageHeight = imgHeight  # 한 프레임의 높이

    def SetFrameMode(self, framemode):
        if framemode < 0:
            return False
        self.nFrameMode = framemode


class SBuild_Coord:

    def __init__(self, nWinWidth, nWinHeight):
        self.nTileWidth = int(nWinWidth / 32)
        self.nTileHeight = int(nWinHeight / 16)
        self.nTileStartX = int(3 * self.nTileWidth)
        self.nTileStartY = int(2 * self.nTileHeight)

    def GetPositionX(self, x):
        nX = int((x - self.nTileStartX) / self.nTileWidth)
        return nX * self.nTileWidth + self.nTileStartX

    def GetPositionY(self, y):
        nY = int((y - self.nTileStartY) / self.nTileHeight)
        return nY * self.nTileHeight + self.nTileStartY

    # 빌드 맵 한 칸의 사이즈를 정한다.
    def SetTileSize(self, nWinWidth, nWinHeight):
        self.nTileWidth = int(nWinWidth / 32)
        self.nTileHeight = int(nWinHeight / 16)
        self.nTileStartX = int(3 * self.nTileWidth)
        self.nTileStartY = int(2 * self.nTileHeight)

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

        bCheck = True

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

        if self.CheckBuildable(x, y, sizeX, sizeY):
            imgTile = SImage("tmpImage/tile_g.png")
            imgTile.SetPosition(nX * self.nTileWidth + self.nStartX,
                                nY * self.nTileHeight + self.nStartY)
            imgTile.SetImageFrame(1, 64, 64)
            imgTile.DrawImage_Scaled(self.nTileWidth, self.nTileHeight, sizeX, sizeY)
        else:
            imgTile = SImage("tmpImage/tile_r.png")
            imgTile.SetPosition(nX * self.nTileWidth + self.nStartX,
                                nY * self.nTileHeight + self.nStartY)
            imgTile.SetImageFrame(1, 64, 64)
            imgTile.DrawImage_Scaled(self.nTileWidth, self.nTileHeight, sizeX, sizeY)
