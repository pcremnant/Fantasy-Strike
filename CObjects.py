from pico2d import *


# 뭐가 있어야 될까..? 유닛 클래스
# 1. 좌표값
# 2. 이미지 / 애니메이션 관련
# 3. 스테이터스
# 4. 인공지능

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

    def __init__(self):
        self.imgObjectImage
        self.nMaxFrame
        self.nCurFrame
        self.nImageWidth
        self.nImageHeight
        self.posImagePosition
        pass


class Obj_Player_Unit_Civil:

    def __init__(self, x, y):
        self.Obj_Position = struct_Position(x, y)  # position

        self.Obj_Image  # image of obj
        self.MaxFrame = 1
        self.CurFrame = 0
        self.nImageWidth = 1
        self.nImageHeight = 1
        self.posImagePosition = Struct_Position(0, 0)

        self.Obj_Status = Struct_Status_Unit()
        # Obj Status add

        pass
