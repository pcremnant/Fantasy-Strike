from game.package.object.build_object import *
from pico2d import *

# tmp code : object list to show on right side -----------------------------------------
# this code will be moved to basic_module module of build object
pos = change_coord_from_build_to_screen(BUILD_MAP_SIZE_X + BUILD_MAP_EDGE_X, BUILD_MAP_EDGE_Y)

OBJECT_BASIC_WARRIOR = pos[0] + 1 * BUILD_TILE_WIDTH, pos[1] + 3 * BUILD_TILE_HEIGHT, \
                       pos[0] + 3 * BUILD_TILE_WIDTH - 1, pos[1] + 5 * BUILD_TILE_HEIGHT

OBJECT_BASIC_TENT = pos[0] + 3 * BUILD_TILE_WIDTH, pos[1] + 3 * BUILD_TILE_HEIGHT, \
                    pos[0] + 5 * BUILD_TILE_WIDTH - 1, pos[1] + 5 * BUILD_TILE_HEIGHT


# checking mouse point in object's collision box
def point_in_box(object_coord, mx, my):
    if object_coord[0] <= mx <= object_coord[2] and object_coord[1] <= my <= object_coord[3]:
        return True
    else:
        return False


# --------------------------------------------------------------------------------------

# manage all of build object
class Build_Object_Manager:
    def __init__(self):
        self.objects = []  # object list
        self.build_map = basic_struct.Build_Map()  # map of build objects
        self.mouse_x = 400  # current mouse position
        self.mouse_y = 300
        self.mouse_clicked_x = None  # mouse position when clicked
        self.mouse_clicked_y = None
        self.build_tech = Build_Table()  # class for buy or select build object

        self.select_object = None  # object that is selected
        pass

    # build selected object on build map
    def build_object(self, selected_object):
        if selected_object is None:
            return  # return nothing
        if self.build_map.check_is_buildable(self.mouse_x, self.mouse_y, selected_object.size_x,
                                             selected_object.size_y):
            self.build_map.build_object(self.mouse_x, self.mouse_y, selected_object.size_x, selected_object.size_y)
            self.objects.append(selected_object)

    def get_mouse_position(self, x, y):
        self.mouse_x = x
        self.mouse_y = y

    def get_clicked_mouse_position(self, x, y):
        self.mouse_clicked_x = x
        self.mouse_clicked_y = y
        selected_object = self.select_object
        self.build_object(selected_object)
        self.select_object = self.build_tech.select_object(self.mouse_clicked_x, self.mouse_clicked_y)

    def draw(self):
        if self.select_object is None:
            pass  # do nothing
        elif self.build_map.build_pointer(self.mouse_x, self.mouse_y, self.select_object.size_x,
                                          self.select_object.size_y):
            self.select_object.build_object_on_tile(self.mouse_x, self.mouse_y)
            self.select_object.draw_object()

        # tmp code : draw build map ------------------------------------
        self.build_map.tmp_draw_table()
        # --------------------------------------------------------------

        if self.objects:
            for obj in self.objects:
                obj.draw_object()
        self.build_tech.draw()  # draw build objects on right side


# Build_Table has all of build objects
# build manager selects object in Build_Table
class Build_Table:
    def __init__(self):
        self.image = load_image("resource/UI/build_table.png")
        self.position = change_coord_from_build_to_screen(BUILD_MAP_SIZE_X + BUILD_MAP_EDGE_X, BUILD_MAP_EDGE_Y)
        self.table = [[], []]
        self.layer = 0  # build layer will be added

        # tmp code ------------------------------------------------------------------------------------------------
        self.object_coord = [OBJECT_BASIC_WARRIOR, OBJECT_BASIC_TENT]  # position of build objects
        self.table[self.layer].append(Object_Build_BasicWarrior(self.object_coord[0][2],
                                                                (self.object_coord[0][1] + self.object_coord[0][
                                                                    3]) / 2))
        self.table[self.layer].append(Object_Build_BasicTent(self.object_coord[1][2],
                                                             (self.object_coord[1][1] + self.object_coord[1][3]) / 2))
        # ----------------------------------------------------------------------------------------------------------
        pass

    def select_object(self, mx, my):
        count = 0
        for o in self.object_coord:
            if point_in_box(o, mx, my):
                if count == 0:
                    return Object_Build_BasicWarrior(mx, my)
                elif count == 1:
                    return Object_Build_BasicTent(mx, my)
            else:
                count += 1

        return None

    def select_layer(self):
        pass

    def draw(self):
        self.image.draw(self.position[0] + BUILD_MAP_EDGE_X * BUILD_TILE_WIDTH / 2,
                        self.position[1] + BUILD_MAP_EDGE_Y * BUILD_TILE_HEIGHT / 2,
                        BUILD_MAP_EDGE_X * BUILD_TILE_WIDTH, BUILD_MAP_EDGE_Y * BUILD_TILE_HEIGHT)
        for obj in self.table[self.layer]:
            obj.draw_object()

        # tmp code : draw collision box ---------------------------------------------------
        pico2d.draw_rectangle(self.object_coord[0][0], self.object_coord[0][1],
                              self.object_coord[0][2], self.object_coord[0][3])
        pico2d.draw_rectangle(self.object_coord[1][0], self.object_coord[1][1],
                              self.object_coord[1][2], self.object_coord[1][3])
        # --------------------------------------------------------------------------------
