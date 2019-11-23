from game.package.basic_module import basic_struct

FRAME_MODE_NONE = -1


# parent class
class Object:

    def __init__(self, size_x, size_y):
        self.position = None
        self.image_class = None
        self.size_x = size_x
        self.size_y = size_y
        self.type = None

    def set_object_frame(self, frame_mode, max_frame, image_width, image_height):
        if frame_mode == FRAME_MODE_NONE:
            self.image_class.set_image_frame(max_frame, image_width, image_height)
        else:
            self.image_class[frame_mode].set_image_frame(max_frame, image_width, image_height)

    def draw(self):
        pass

    def set_object_position(self, x, y):
        self.position = basic_struct.Position(x, y)
