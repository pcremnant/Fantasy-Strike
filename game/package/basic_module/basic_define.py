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


def change_coord_from_build_to_screen(x, y):    # get build object's tile position and then transform to window position
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
UNIT_TILE_START_X = UNIT_MAP_EDGE_X * BUILD_TILE_WIDTH
UNIT_TILE_START_Y = UNIT_MAP_EDGE_Y * BUILD_TILE_HEIGHT
