from game.package.object.object import *


class Obj_Unit(Obj):
    def __init__(self, x, y, sizeX, sizeY, imgPath):
        super().__init__(sizeX, sizeY, imgPath)

    def SetFrameMode(self, action):
        self.imgObject.set_frame_mode(action)
        self.imgObject.nCurFrame = 0
