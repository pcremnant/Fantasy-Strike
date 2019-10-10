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

    def __init__(self, x, y, imgPath):
        self.posObject = struct.SPosition(x, y)
        self.imgObject = struct.SImage(imgPath)
        self.imgObject.SetPosition(x, y)

    def SetObjectImage(self, maxFrame, imgWidth, imgHeight):
        self.imgObject.SetImageFrame(maxFrame, imgWidth, imgHeight)

    def DrawObject(self):
        self.imgObject.DrawImage()

    def SetPosition(self, x, y):
        self.posObject = struct.SPosition(x, y)
        self.imgObject.SetPosition(x, y)


class Obj_Build(Obj):
    global cBuildMap

    def __init__(self, x, y, imgPath):
        super().__init__(x, y, imgPath)
        # 필요한 자원 리소스들 추가
        self.nResource = 0  # 임시 자원 변수

    def BuildObject(self, x, y):
        self.SetPosition(cBuildMap.GetPositionX(x), cBuildMap.GetPositionY(y))
        # self.posObject.SetPosition(posMouse.posX - (posMouse.posX % 16), posMouse.posY - (posMouse.posY % 16))
        # 16픽셀 단위로 이동 가능하게 설정

# 마우스 포인터를 받아서 건물을 짓는다
