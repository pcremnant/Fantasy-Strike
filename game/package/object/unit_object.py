from game.package.object.object import *


class Object_Unit(Object):
    def __init__(self, x, y, sizeX, sizeY, imgPath):
        super().__init__(sizeX, sizeY, imgPath)

    def SetFrameMode(self, action):
        self.class_object_image.set_frame_mode(action)
        self.class_object_image.nCurFrame = 0
