from game.package.basic_module import basic_struct

FRAME_MODE_NONE = -1


# parent class
class Object:

    def __init__(self, size_x, size_y):
        self.object_position = None
        self.class_object_image = None
        self.size_x = size_x
        self.size_y = size_y

    def set_object_frame(self, frame_mode, max_frame, image_width, image_height):
        if frame_mode == FRAME_MODE_NONE:
            self.class_object_image.set_image_frame(max_frame, image_width, image_height)
        else:
            self.class_object_image[frame_mode].set_image_frame(max_frame, image_width, image_height)

    def draw_object(self):
        pass

    def set_object_position(self, x, y):
        self.object_position = basic_struct.Position(x, y)
