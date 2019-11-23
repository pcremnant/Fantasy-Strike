WINDOW_WIDTH, WINDOW_HEIGHT = 1024, 768

# for image struct
SUB_FRAME = 32
IMAGE_TYPE_SPRITE = 1
IMAGE_TYPE_FILES = 2

# for build objects
BUILD_MAP_SIZE_X, BUILD_MAP_SIZE_Y = 16, 12
BUILD_MAP_EDGE_X, BUILD_MAP_EDGE_Y = 6, 6

BUILD_TILE_WIDTH = WINDOW_WIDTH // (BUILD_MAP_SIZE_X + 2 * BUILD_MAP_EDGE_X)
BUILD_TILE_HEIGHT = WINDOW_HEIGHT // (BUILD_MAP_SIZE_Y + 2 * BUILD_MAP_EDGE_Y)
BUILD_TILE_START_X = BUILD_MAP_EDGE_X * BUILD_TILE_WIDTH
BUILD_TILE_START_Y = BUILD_MAP_EDGE_Y * BUILD_TILE_HEIGHT

BUILDING_TYPE_BASIC_WARRIOR = 1
BUILDING_TYPE_BASIC_TENT = 2


def change_coord_from_buildmap_to_screen(x, y):  # get building's tile position and then transform to window position
    return x * BUILD_TILE_WIDTH, y * BUILD_TILE_HEIGHT


def get_build_tile_position_x(current_position_x):
    build_tile_x = int(current_position_x / BUILD_TILE_WIDTH)
    return build_tile_x


def get_build_tile_position_y(current_position_y):
    build_tile_y = int(current_position_y / BUILD_TILE_HEIGHT)
    return build_tile_y


# for unit objects
UNIT_MAP_SIZE_X, UNIT_MAP_SIZE_Y = 20, 15
UNIT_MAP_EDGE_X, UNIT_MAP_EDGE_Y = 2, 2

UNIT_TILE_WIDTH = WINDOW_WIDTH // (UNIT_MAP_SIZE_X + 2 * UNIT_MAP_EDGE_X)
UNIT_TILE_HEIGHT = WINDOW_HEIGHT // (UNIT_MAP_SIZE_Y + 2 * UNIT_MAP_EDGE_Y)
UNIT_MAP_START_X = UNIT_MAP_EDGE_X * UNIT_TILE_WIDTH
UNIT_MAP_START_Y = UNIT_MAP_EDGE_Y * UNIT_TILE_HEIGHT
UNIT_MAP_END_X = UNIT_MAP_START_X + UNIT_MAP_SIZE_X * UNIT_TILE_WIDTH
UNIT_MAP_END_Y = UNIT_MAP_START_Y + UNIT_MAP_SIZE_Y * UNIT_TILE_HEIGHT


def change_coord_from_unitmap_to_screen(x, y):  # get unit object's tile position and then transform to window position
    return x * UNIT_TILE_WIDTH, y * UNIT_TILE_HEIGHT


def get_unit_tile_position_x(current_position_x):
    unit_tile_x = int(current_position_x / UNIT_TILE_WIDTH)
    return unit_tile_x


def get_unit_tile_position_y(current_position_y):
    unit_tile_y = int(current_position_y / UNIT_TILE_HEIGHT)
    return unit_tile_y


# for framework

HANDLE_EVENT_CHANGE_STATE = 1
HANDLE_EVENT_QUIT_STATE = -1
HANDLE_EVENT_NONE = 0
