import game.package.basic_module.building_map
from game.package.object.building import *
from game.package.basic_module.basic_define import *
from pico2d import *

BUILD_TABLE_POSITION = change_coord_from_building_map_to_screen(BUILD_MAP_SIZE_X + BUILD_MAP_EDGE_X, BUILD_MAP_EDGE_Y)


def get_window_position_for_build_table(x, y, w, h):
    return BUILD_TABLE_POSITION[0] + x * BUILD_TILE_WIDTH, BUILD_TABLE_POSITION[1] + y * BUILD_TILE_HEIGHT, \
           BUILD_TABLE_POSITION[0] + (x + w) * BUILD_TILE_WIDTH, BUILD_TABLE_POSITION[1] + (y + h) * BUILD_TILE_HEIGHT


BUILD_TABLE_WARRIOR = get_window_position_for_build_table(0, 3, 2, 2)
BUILD_TABLE_TENT = get_window_position_for_build_table(2, 3, 2, 2)
BUILD_TABLE_TIMBER = get_window_position_for_build_table(0, 7, 2, 2)
BUILD_TABLE_QUARRY = get_window_position_for_build_table(2, 7, 2, 2)


# checking mouse point in object's collision box
def point_in_box(object_coord, mx, my):
    if object_coord[0] <= mx <= object_coord[2] and object_coord[1] <= my <= object_coord[3]:
        return True
    else:
        return False


# --------------------------------------------------------------------------------------

# manage all of build object
class BuildingManager:
    def __init__(self):
        self.buildings = []  # object list
        self.build_map = game.package.basic_module.building_map.Build_Map()  # map of build objects
        self.mouse_x = 400  # current mouse position
        self.mouse_y = 300
        self.mouse_clicked_x = None  # mouse position when clicked
        self.mouse_clicked_y = None
        self.build_tech = Build_Table()  # class for buy or select build object

        self.select_object = None  # object that is selected
        pass

    # build selected object on build map
    def build_object(self, selected_object, current_resource):
        if selected_object is None:
            return  # return nothing
        elif current_resource.wood >= selected_object.require_resource.wood and current_resource.stone >= selected_object.require_resource.stone:
            if self.build_map.check_is_buildable(self.mouse_x, self.mouse_y, selected_object.size_x,
                                                 selected_object.size_y):
                current_resource.wood -= selected_object.require_resource.wood
                current_resource.stone -= selected_object.require_resource.stone
                self.build_map.build_object(self.mouse_x, self.mouse_y, selected_object.size_x, selected_object.size_y)
                self.buildings.append(selected_object)
        else:
            selected_object = None

    def get_mouse_position(self, x, y):
        self.mouse_x = x
        self.mouse_y = y

    def get_clicked_mouse_position(self, x, y, current_resource):
        self.mouse_clicked_x = x
        self.mouse_clicked_y = y
        selected_object = self.select_object
        self.build_object(selected_object, current_resource)
        self.select_object = self.build_tech.select_object(self.mouse_clicked_x, self.mouse_clicked_y)

    def draw(self):
        if self.select_object is None:
            pass  # do nothing
        elif self.build_map.show_is_buildable(self.mouse_x, self.mouse_y, self.select_object.size_x,
                                              self.select_object.size_y):
            self.select_object.build_object_on_tile(self.mouse_x, self.mouse_y)
            self.select_object.draw()

        # tmp code : draw build map ------------------------------------
        draw_building_map()
        # --------------------------------------------------------------
        if self.buildings:
            for obj in self.buildings:
                obj.draw()

        self.build_tech.draw()  # draw build objects on right side

    def get_additional_resource(self):
        wood = 0
        stone = 0
        for build in self.buildings:
            if build.type == BUILDING_TYPE_TIMBER:
                wood += 1
            elif build.type == BUILDING_TYPE_QUARRY:
                stone += 1

        return wood, stone


# Build_Table has all of build objects
# build manager selects object in Build_Table
class Build_Table:
    def __init__(self):
        self.table_image = load_image("resource/UI/build_table.png")
        self.position = change_coord_from_building_map_to_screen(BUILD_MAP_SIZE_X + BUILD_MAP_EDGE_X,
                                                                 BUILD_MAP_EDGE_Y + 2)
        self.table = [[], []]
        self.layer = 0  # build layer will be added

        # position of build objects
        self.object_coord = [BUILD_TABLE_WARRIOR, BUILD_TABLE_TENT, BUILD_TABLE_TIMBER, BUILD_TABLE_QUARRY]
        self.table[self.layer].append(Building_WarriorStone(self.object_coord[0][2],
                                                            (self.object_coord[0][1] + self.object_coord[0][3]) / 2,
                                                            True))
        self.table[self.layer].append(Building_Tent(self.object_coord[1][2],
                                                    (self.object_coord[1][1] + self.object_coord[1][3]) / 2, True))

        self.table[self.layer].append(Building_Timber(self.object_coord[2][2],
                                                      (self.object_coord[2][1] + self.object_coord[2][3]) / 2, True))

        self.table[self.layer].append(Building_Quarry(self.object_coord[3][2],
                                                      (self.object_coord[3][1] + self.object_coord[3][3]) / 2, True))

        pass

    def select_object(self, mx, my):
        count = 0
        for o in self.object_coord:
            if point_in_box(o, mx, my):
                if count == 0:
                    return Building_WarriorStone(mx, my)
                elif count == 1:
                    return Building_Tent(mx, my)
                elif count == 2:
                    return Building_Timber(mx, my)
                elif count == 3:
                    return Building_Quarry(mx, my)
            else:
                count += 1

        return None

    def select_layer(self):
        pass

    def draw(self):
        self.table_image.draw(self.position[0] + BUILD_MAP_EDGE_X * BUILD_TILE_WIDTH / 2,
                              self.position[1] + (BUILD_MAP_EDGE_Y + 1) * BUILD_TILE_HEIGHT / 2,
                              (BUILD_MAP_EDGE_X + 0.8) * BUILD_TILE_WIDTH, (BUILD_MAP_EDGE_Y + 5) * BUILD_TILE_HEIGHT)
        for obj in self.table[self.layer]:
            obj.draw()
