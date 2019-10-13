import CStruct as struct
import CBasicDefines as DEFINE

# 뭐가 있어야 될까..? 유닛 클래스
# 1. 좌표값
# 2. 이미지 / 애니메이션 관련
# 3. 스테이터스
# 4. 인공지능

# 건설 맵 크기를 몇으로 할까??
# 가로 26칸
# 세로 12칸
# tile_size = Window_Width/32 Window_Height/16 -> 나머지 칸들은 UI가 들어 갈 칸

cBuildMap = struct.SBuild_Coord(DEFINE.WINDOW_WIDTH, DEFINE.WINDOW_HEIGHT)


class Obj:

    def __init__(self, x, y, sizeX, sizeY, imgPath):
        tmpX = cBuildMap.GetPositionX(x)
        tmpY = cBuildMap.GetPositionX(y)
        self.posObject = struct.SPosition(tmpX, tmpY)
        self.imgObject = struct.SImage(imgPath)
        self.imgObject.SetPosition(tmpX, tmpY)
        self.nSizeX = sizeX
        self.nSizeY = sizeY

    def SetObjectImage(self, maxFrame, imgWidth, imgHeight):
        self.imgObject.SetImageFrame(maxFrame, imgWidth, imgHeight)

    def DrawObject(self):
        self.imgObject.DrawImage_Scaled(cBuildMap.GetTileWidth(), cBuildMap.GetTileHeight(), self.nSizeX, self.nSizeY)

    def SetPosition(self, x, y):
        self.posObject = struct.SPosition(x, y)
        self.imgObject.SetPosition(x, y)


class Obj_Unit(Obj):
    def __init__(self, x, y, sizeX, sizeY, imgPath):
        super().__init__(x, y, sizeX, sizeY, imgPath)

    def SetFrameMode(self, framemode):
        self.imgObject.SetFrameMode(framemode)
        self.imgObject.nCurFrame = 0


class Obj_Build(Obj):
    global cBuildMap

    def __init__(self, x, y, sizeX, sizeY, imgPath):
        super().__init__(x, y, sizeX, sizeY, imgPath)
        # 필요한 자원 리소스들 추가
        self.nResource = 0  # 임시 자원 변수

    def BuildObject(self, x, y):
        self.SetPosition(cBuildMap.GetPositionX(x), cBuildMap.GetPositionY(y))
        # self.posObject.SetPosition(posMouse.posX - (posMouse.posX % 16), posMouse.posY - (posMouse.posY % 16))
        # 16픽셀 단위로 이동 가능하게 설정


class Obj_BuildPointer(Obj):
    global cBuildMap

    def __int__(self, x, y, sizeX, sizeY, imgPath):
        super().__init__(x, y, sizeX, sizeY, imgPath)

    def GetMousePosition(self, x, y):
        self.SetPosition(cBuildMap.GetPositionX(x), cBuildMap.GetPositionY(y))
# 마우스 포인터를 받아서 건물을 짓는다
