from game.package.basic_module import basic_struct


# parent class
class Object:

    def __init__(self, size_x, size_y):
        self.object_position = None
        self.class_object_image = None
        self.size_x = size_x
        self.size_y = size_y

    def set_object_frame(self, max_frame, image_width, image_height):
        self.class_object_image.set_image_frame(max_frame, image_width, image_height)

    def draw_object(self):
        pass

    def set_object_position(self, x, y):
        self.object_position = basic_struct.Position(x, y)
        self.class_object_image.set_position(x, y)
