from game.package.object.object import *
from game.package.basic_module.basic_struct import *
from pico2d import *

# tmp code : unit define module will be added ----------------------------------------------
UNIT_FRAME_MOVE_UP = 0
UNIT_FRAME_MOVE_DOWN = 1
UNIT_FRAME_MOVE_RIGHT = 2
UNIT_FRAME_MOVE_LEFT = 3

UNIT_FRAME_SIZE = 4


# ------------------------------------------------------------------------------------------

class Object_Unit(Object):
    def __init__(self, x, y, size_x, size_y):
        super().__init__(size_x, size_y)
        self.class_object_image = []  # image list [frame_mode]
        self.object_frame_mode = None
        self.object_position = basic_struct.Position(x, y)

        pass

    def draw(self):
        self.class_object_image[self.object_frame_mode].draw_image(self.object_position.x, self.object_position.y)


# tmp unit (for test)
class Object_Unit_Warrior(Object_Unit):
    def __init__(self, x, y):
        super().__init__(x, y, 2, 2)
        self.object_frame_mode = UNIT_FRAME_MOVE_RIGHT
        image_path_table = []
        image_type_table = []

        # test code
        if __name__ == '__main__':
            image_path_table.append([
                'warrior/move_top_1.png',
                'warrior/move_top_2.png',
                'warrior/move_top_3.png',
                'warrior/move_top_4.png'
            ])
            image_type_table.append(IMAGE_TYPE_FILES)

            image_path_table.append([
                'warrior/move_bottom_1.png',
                'warrior/move_bottom_2.png',
                'warrior/move_bottom_3.png',
                'warrior/move_bottom_4.png'
            ])
            image_type_table.append(IMAGE_TYPE_FILES)

            image_path_table.append([
                'warrior/move_right_1.png',
                'warrior/move_right_2.png',
                'warrior/move_right_3.png',
                'warrior/move_right_4.png'
            ])
            image_type_table.append(IMAGE_TYPE_FILES)

            image_path_table.append([
                'warrior/move_left_1.png',
                'warrior/move_left_2.png',
                'warrior/move_left_3.png',
                'warrior/move_left_4.png'
            ])
            image_type_table.append(IMAGE_TYPE_FILES)
        else:
            # set image sprites
            image_path_table.append([
                'resource/object/unit/warrior/move_top_1.png',
                'resource/object/unit/warrior/move_top_2.png',
                'resource/object/unit/warrior/move_top_3.png',
                'resource/object/unit/warrior/move_top_4.png'
            ])
            image_type_table.append(IMAGE_TYPE_FILES)

            image_path_table.append([
                'resource/object/unit/warrior/move_bottom_1.png',
                'resource/object/unit/warrior/move_bottom_2.png',
                'resource/object/unit/warrior/move_bottom_3.png',
                'resource/object/unit/warrior/move_bottom_4.png'
            ])
            image_type_table.append(IMAGE_TYPE_FILES)

            image_path_table.append([
                'resource/object/unit/warrior/move_right_1.png',
                'resource/object/unit/warrior/move_right_2.png',
                'resource/object/unit/warrior/move_right_3.png',
                'resource/object/unit/warrior/move_right_4.png'
            ])
            image_type_table.append(IMAGE_TYPE_FILES)

            image_path_table.append([
                'resource/object/unit/warrior/move_left_1.png',
                'resource/object/unit/warrior/move_left_2.png',
                'resource/object/unit/warrior/move_left_3.png',
                'resource/object/unit/warrior/move_left_4.png'
            ])
            image_type_table.append(IMAGE_TYPE_FILES)

        for frame_mode in range(UNIT_FRAME_SIZE):
            self.class_object_image.append(
                basic_struct.Image(image_path_table[frame_mode], image_type_table[frame_mode]))

        self.set_object_frame(UNIT_FRAME_MOVE_UP, 4, 64, 64)
        self.set_object_frame(UNIT_FRAME_MOVE_DOWN, 4, 64, 64)
        self.set_object_frame(UNIT_FRAME_MOVE_LEFT, 4, 64, 64)
        self.set_object_frame(UNIT_FRAME_MOVE_RIGHT, 4, 64, 64)

        pass


# check load image and frame
def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False


running = True

if __name__ == '__main__':
    print('s')
    open_canvas()
    warrior = Object_Unit_Warrior(400, 300)
    tmpV = 1
    while running:
        warrior.draw()
        warrior.object_position.move_position(0, -tmpV * 7 / SUB_FRAME)

        if warrior.object_position.y >= 600:
            tmpV = -1
            warrior.object_frame_mode = UNIT_FRAME_MOVE_DOWN
        elif warrior.object_position.y <= 0:
            tmpV = 1
            warrior.object_frame_mode = UNIT_FRAME_MOVE_UP
        update_canvas()
        clear_canvas()
        handle_events()
    close_canvas()
