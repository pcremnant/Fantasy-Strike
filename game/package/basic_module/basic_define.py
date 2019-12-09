import pico2d

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
BUILDING_TYPE_TIMBER = 3
BUILDING_TYPE_QUARRY = 4


def change_coord_from_building_map_to_screen(x, y):  # get building's tile position and then transform to window position
    return x * BUILD_TILE_WIDTH, y * BUILD_TILE_HEIGHT


def get_build_tile_position_x(current_position_x):
    build_tile_x = int(current_position_x / BUILD_TILE_WIDTH)
    return build_tile_x


def get_build_tile_position_y(current_position_y):
    build_tile_y = int(current_position_y / BUILD_TILE_HEIGHT)
    return build_tile_y


def draw_building_map():
    for y in range(0, BUILD_MAP_SIZE_Y - 1, 1):
        for x in range(0, BUILD_MAP_SIZE_X - 1, 1):
            pico2d.draw_rectangle(BUILD_TILE_START_X + x * BUILD_TILE_WIDTH,
                                  BUILD_TILE_START_Y + y * BUILD_TILE_HEIGHT,
                                  BUILD_TILE_START_X + (x + 1) * BUILD_TILE_WIDTH,
                                  BUILD_TILE_START_Y + (y + 1) * BUILD_TILE_HEIGHT)


# for unit objects
UNIT_MAP_SIZE_X, UNIT_MAP_SIZE_Y = 20, 15
UNIT_MAP_EDGE_X, UNIT_MAP_EDGE_Y = 2, 2

UNIT_TILE_WIDTH = WINDOW_WIDTH // (UNIT_MAP_SIZE_X + 2 * UNIT_MAP_EDGE_X)
UNIT_TILE_HEIGHT = WINDOW_HEIGHT // (UNIT_MAP_SIZE_Y + 2 * UNIT_MAP_EDGE_Y)
UNIT_MAP_START_X = UNIT_MAP_EDGE_X * UNIT_TILE_WIDTH
UNIT_MAP_START_Y = UNIT_MAP_EDGE_Y * UNIT_TILE_HEIGHT
UNIT_MAP_END_X = UNIT_MAP_START_X + UNIT_MAP_SIZE_X * UNIT_TILE_WIDTH
UNIT_MAP_END_Y = UNIT_MAP_START_Y + UNIT_MAP_SIZE_Y * UNIT_TILE_HEIGHT

UNIT_TEAM_PLAYER = 1
UNIT_TEAM_ENEMY = 2


def change_coord_from_unitmap_to_screen(x, y):  # get unit object's tile position and then transform to window position
    return x * UNIT_TILE_WIDTH, y * UNIT_TILE_HEIGHT


def get_unit_tile_position_x(current_position_x):
    unit_tile_x = int((current_position_x - UNIT_MAP_EDGE_X * UNIT_TILE_WIDTH) / UNIT_TILE_WIDTH)
    if unit_tile_x < 0:
        return 0
    elif unit_tile_x >= UNIT_MAP_SIZE_X - 1:
        return UNIT_MAP_SIZE_X - 1
    else:
        return unit_tile_x


def get_unit_tile_position_y(current_position_y):
    unit_tile_y = int((current_position_y - UNIT_MAP_EDGE_Y * UNIT_TILE_HEIGHT) / UNIT_TILE_HEIGHT)
    if unit_tile_y < 0:
        return 0
    elif unit_tile_y >= UNIT_MAP_SIZE_Y - 1:
        return UNIT_MAP_SIZE_Y - 1
    else:
        return unit_tile_y


def draw_unit_map():
    for y in range(0, UNIT_MAP_SIZE_Y, 1):
        for x in range(0, UNIT_MAP_SIZE_X, 1):
            pico2d.draw_rectangle(UNIT_MAP_START_X + x * UNIT_TILE_WIDTH,
                                  UNIT_MAP_START_Y + y * UNIT_TILE_HEIGHT,
                                  UNIT_MAP_START_X + (x + 1) * UNIT_TILE_WIDTH,
                                  UNIT_MAP_START_Y + (y + 1) * UNIT_TILE_HEIGHT)


# for framework

HANDLE_EVENT_CHANGE_STATE = 1
HANDLE_EVENT_QUIT_STATE = -1
HANDLE_EVENT_NONE = 0
HANDLE_EVENT_ENTER_PAUSE = 2
HANDLE_EVENT_EXIT_PAUSE = -2
TIMER_UNIT_CREATION = 20

BGM_INDEX_MAIN = 0
BGM_INDEX_GAME = 1

EFFECT_INDEX_SWORD_SWING = 0
EFFECT_INDEX_KNIFE_SWING = 1
EFFECT_INDEX_HAMMER_SWING = 2
EFFECT_INDEX_VICTORY = 3