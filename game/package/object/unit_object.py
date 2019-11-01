from game.package.object.object import *


class Object_Unit(Object):
    def __init__(self, x, y, size_x, size_y, image_path):
        super().__init__(size_x, size_y, image_path)

    def set_frame_mode(self, action):
        self.class_object_image.set_frame_mode(action)
        self.class_object_image.nCurFrame = 0
