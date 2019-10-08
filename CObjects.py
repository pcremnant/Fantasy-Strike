from pico2d import *

# 뭐가 있어야 될까..? 유닛 클래스
# 1. 좌표값
# 2. 이미지 / 애니메이션 관련
# 3. 스테이터스
# 4. 인공지능

open_canvas()


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
        self.nMaxFrame = 4  # 최대 프레임
        self.nCurFrame = 0  # 현재 프레임
        self.nImageWidth = 16  # 한 프레임의 너비
        self.nImageHeight = 16  # 한 프레임의 높이
        self.posImagePosition = position  # 이미지의 화면상 위치
        self.bIsDraw = True  # 이미지 렌더링 여부

    def DrawImage(self):
        if self.bIsDraw:
            self.imgObjectImage.clip_draw(self.nCurFrame * self.nImageWidth, self.nImageHeight, self.nImageWidth,
                                          self.nImageHeight, self.posImagePosition.PosX, self.posImagePosition.PosY)
        self.nCurFrame += 1
        self.nCurFrame = self.nCurFrame % self.nMaxFrame


running = True


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False

    pass


class Obj_Player_Unit_Civil:

    def __init__(self, x, y):
        self.Obj_Position = Struct_Position(x, y)  # position

        self.Obj_Image = Struct_Image(self.Obj_Position, "jumblysprite.png")  # 오브젝트 이미지
        self.Obj_Status = Struct_Status_Unit()
        # Obj Status add

        pass

    def DrawObject(self):
        self.Obj_Image.DrawImage()


unit = Obj_Player_Unit_Civil(400, 300)

while running:
    clear_canvas()

    unit.DrawObject()

    update_canvas()

    handle_events()
    delay(0.1)
