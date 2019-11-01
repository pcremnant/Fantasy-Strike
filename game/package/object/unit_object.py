from game.package.object.object import *

# tmp code : unit define module will be added ----------------------------------------------
IMAGE_UNIT_FRAME_MOVE_UP = 0
IMAGE_UNIT_FRAME_MOVE_DOWN = 1
IMAGE_UNIT_FRAME_MOVE_RIGHT = 2
IMAGE_UNIT_FRAME_MOVE_LEFT = 3

IMAGE_UNIT_FRAME_SIZE = 4


# ------------------------------------------------------------------------------------------

class Object_Unit(Object):
    def __init__(self, x, y, size_x, size_y):
        super().__init__(size_x, size_y)

        self.class_object_image = [[], []]          # image list [frame_mode][frame]
        for number in range(IMAGE_UNIT_FRAME_SIZE):
            self.class_object_image.append(number)

        pass

    def set_frame_mode(self, action):
        # self.class_object_image.set_frame_mode(action)
        self.class_object_image.nCurFrame = 0


# tmp code
class Object_Unit_Warrior(Object_Unit):
    def __init__(self):
        pass
