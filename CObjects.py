from pico2d import *

# 뭐가 있어야 될까..? 유닛 클래스
# 1. 좌표값
# 2. 이미지 / 애니메이션 관련
# 3. 스테이터스
# 4. 인공지능

open_canvas(1024, 768)


# 건설 맵 크기를 몇으로 할까??
# 가로 26칸
# 세로 12칸
# tile_size = Window_Width/32 Window_Height/16 -> 나머지 칸들은 UI가 들어 갈 칸


class Struct_Build_Coord:

    def __init__(self, nWinWidth, nWinHeight):
        self.nTileWidth = nWinWidth / 32
        self.nTileHeight = nWinHeight / 16
        self.nTileStartX = 3*self.nTileWidth
        self.nTileStartY = 2*self.nTileHeight
        self.posCoord = Struct_Position(0, 0)

    def GetPosition(self):
        return (self.posCoord.PosX*self.nTileWidth + self.nTileStartX,
                self.posCoord.PosY*self.nTileHeight + self.nTileHeight)


class Struct_Position:

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


class Struct_Status_Unit:

    def __init__(self):
        self.nHp = 0
        self.nAttack = 0
        self.nSpeed = 0
        self.nDefend = 0
        self.nAttackRange = 0
        self.nAttackSpeed = 0
        # add more status
        pass


class Struct_Image:

    def __init__(self, position, imgPath):
        self.imgObjectImage = load_image(imgPath)  # 이미지 로딩
        self.nMaxFrame = 0  # 최대 프레임
        self.nCurFrame = 0  # 현재 프레임
        self.nFrameMode = 0  # 현재 이미지의 행동
        self.nImageWidth = 0  # 한 프레임의 너비
        self.nImageHeight = 0  # 한 프레임의 높이
        self.posImagePosition = position  # 이미지의 화면상 위치
        self.bIsDraw = True  # 이미지 렌더링 여부

    def DrawImage(self):  # 이미지 렌더링
        if self.bIsDraw:
            self.imgObjectImage.clip_draw(self.nCurFrame * self.nImageWidth, self.nFrameMode * self.nImageHeight,
                                          self.nImageWidth, self.nImageHeight, self.posImagePosition.PosX,
                                          self.posImagePosition.PosY)
            self.nCurFrame += 1
            self.nCurFrame = self.nCurFrame % self.nMaxFrame

    def MovePosition(self, x, y):  # 이미지 위치 이동
        self.posImagePosition.MovePosition(x, y)

    def SetImageFrame(self, maxFrame, imgWidth, imgHeight):  # 이미지 초기 세팅
        self.nMaxFrame = maxFrame  # 최대 프레임
        self.nImageWidth = imgWidth  # 한 프레임의 너비
        self.nImageHeight = imgHeight  # 한 프레임의 높이


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_M
    pass


class Obj:

    def __init__(self, x, y, imgPath):
        self.posObject = Struct_Position(x, y)
        self.imgObject = Struct_Image(self.posObject, imgPath)

    def SetObjectImage(self, maxFrame, imgWidth, imgHeight):
        self.imgObject.SetImageFrame(maxFrame, imgWidth, imgHeight)

    def DrawObject(self):
        self.imgObject.DrawImage()


class Obj_Build(Obj):

    def __init__(self, x, y, imgPath):
        super().__init__(x, y, imgPath)
        # 필요한 자원 리소스들 추가
        self.nResource = 0  # 임시 자원 변수

    def BuildObject(self, posMouse):
        self.posObject.SetPosition(posMouse.posX - (posMouse.posX % 16), posMouse.posY - (posMouse.posY % 16))
        # 16픽셀 단위로 이동 가능하게 설정

    def SetObjectImage(self, maxFrame, imgWidth, imgHeight):
        self.imgObject.SetImageFrame(maxFrame, imgWidth, imgHeight)


# 마우스 포인터를 받아서 건물을 짓는다


build = Obj_Build(400, 300, "64x64_tile.png")
build.SetObjectImage(1, 64, 64)

running = True

while running:
    clear_canvas()

    build.DrawObject()

    update_canvas()

    handle_events()
    delay(0.1)
