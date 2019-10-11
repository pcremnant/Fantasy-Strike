import pico2d
import CBasicDefines as DEFINE


class SPosition:

    def __init__(self, x, y):
        self.PosX = x
        self.PosY = y
        pass

    def SetPosition(self, x, y):
        self.PosX = x
        self.PosY = y

    def MovePosition(self, x, y):
        self.PosX += x
        self.PosY -= y

    def GetPositionX(self):
        return self.PosX

    def GetPositionY(self):
        return self.PosY


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

    def MovePosition(self, x, y):  # 이미지 위치 이동
        self.posImagePosition.MovePosition(x, y)

    def SetPosition(self, x, y):
        self.posImagePosition.PosX, self.posImagePosition.PosY = x, y

    def SetImageFrame(self, maxFrame, imgWidth, imgHeight):  # 이미지 초기 세팅
        self.nMaxFrame = maxFrame  # 최대 프레임
        self.nImageWidth = imgWidth  # 한 프레임의 너비
        self.nImageHeight = imgHeight  # 한 프레임의 높이


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
        nY = int((y - self.nTileStartY) / self.nTileHeight + 0.5)
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
        return self.nTileWidth

    def GetStartX(self):
        return self.nTileStartY

    def GetStartY(self):
        return self.nTileStartY


class SBuild_Map:

    def __init__(self, nSX, nSY, nTW, nTH):
        self.mapBuild = [[0 for x in range(DEFINE.BUILD_MAP_SIZE_Y)] for y in range(DEFINE.BUILD_MAP_SIZE_X)]
        self.nStartX = nSX
        self.nStartY = nSY
        self.nTileWidth = nTW
        self.nTileHeight = nTH
        for i in range(DEFINE.BUILD_MAP_SIZE_Y):
            for j in range(DEFINE.BUILD_MAP_SIZE_Y):
                self.mapBuild[i][j] = True

    # 해당 위치가 건설 가능한 곳인지 체크
    def CheckBuildable(self, x, y):
        if x >= DEFINE.BUILD_MAP_SIZE_X:
            return False
        elif y >= DEFINE.BUILD_MAP_SIZE_Y:
            return False
        return self.mapBuild[y][x]

    def tmpDrawTable(self):
        for y in range(DEFINE.BUILD_MAP_SIZE_Y - 1):
            for x in range(DEFINE.BUILD_MAP_SIZE_X - 1):
                pico2d.draw_rectangle(self.nStartX + x*self.nTileWidth, self.nStartY + y*self.nTileHeight,
                                      self.nStartX + (x+1)*self.nTileWidth, self.nStartY + (y+1)*self.nTileHeight)