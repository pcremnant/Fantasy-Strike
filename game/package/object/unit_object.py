from game.package.object.object import *
from game.package.basic_module.basic_struct import *

# tmp code : unit define module will be added ----------------------------------------------
UNIT_FRAME_MOVE_UP = 0
UNIT_FRAME_MOVE_DOWN = 1
UNIT_FRAME_MOVE_RIGHT = 2
UNIT_FRAME_MOVE_LEFT = 3

IMAGE_UNIT_FRAME_SIZE = 4


# ------------------------------------------------------------------------------------------

class Object_Unit(Object):
    def __init__(self, x, y, size_x, size_y, image_path, image_type):
        super().__init__(size_x, size_y)
        self.class_object_image = [[], []]          # image list [frame_mode][frame]
        self.object_frame_mode = None
        
        for frame_mode in range(IMAGE_UNIT_FRAME_SIZE):
            self.class_object_image.append(frame_mode)
            self.class_object_image[frame_mode] = Image(image_path[frame_mode], image_type[frame_mode])
        pass

    def set_frame_mode(self, action):
        # self.class_object_image.set_frame_mode(action)
        self.class_object_image.nCurFrame = 0


# tmp code
class Object_Unit_Warrior(Object_Unit):
    def __init__(self, size_x, size_y):
        super().__init__(size_x, size_y)
        pass
