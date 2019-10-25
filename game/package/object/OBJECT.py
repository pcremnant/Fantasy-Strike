from ..struct import STRUCT
from ..define import DEFINE

# 뭐가 있어야 될까..? 유닛 클래스
# 1. 좌표값
# 2. 이미지 / 애니메이션 관련
# 3. 스테이터스
# 4. 인공지능

# 건설 맵 크기를 몇으로 할까??
# 가로 26칸
# 세로 12칸
# tile_size = Window_Width/32 Window_Height/16 -> 나머지 칸들은 UI가 들어 갈 칸


class Obj:

    def __init__(self, sizeX, sizeY, imgPath):
        self.posObject = None
        self.imgObject = STRUCT.SImage(imgPath)
        self.nSizeX = sizeX
        self.nSizeY = sizeY

    def SetObjectImage(self, maxFrame, imgWidth, imgHeight):
        self.imgObject.SetImageFrame(maxFrame, imgWidth, imgHeight)

    def DrawObject(self):
        pass

    def SetPosition(self, x, y):
        self.posObject = STRUCT.SPosition(x, y)
        self.imgObject.SetPosition(x, y)