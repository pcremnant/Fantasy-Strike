from .build_object import *
from pico2d import *

build_coord = STRUCT.SBuild_Coord()

pos = coord_position(BUILD_MAP_SIZE_X + BUILD_MAP_SIZE_X_EDGE, BUILD_MAP_SIZE_Y_EDGE)

OBJECT_TREE = ((pos[0], pos[1] + 4 * BUILD_TILE_HEIGHT),
               (pos[0] + 2 * BUILD_TILE_WIDTH - 1, pos[1] + 6 * BUILD_TILE_HEIGHT))
OBJECT_TMP = ((pos[0] + 2 * BUILD_TILE_WIDTH, pos[1] + 4 * BUILD_TILE_HEIGHT),
              (pos[0] + 4 * BUILD_TILE_WIDTH - 1, pos[1] + 6 * BUILD_TILE_HEIGHT))
OBJECT_TENT = ((pos[0] + 4 * BUILD_TILE_WIDTH, pos[1] + 4 * BUILD_TILE_HEIGHT),
               (pos[0] + 6 * BUILD_TILE_WIDTH - 1, pos[1] + 6 * BUILD_TILE_HEIGHT))


def point_in_box(object_coord, mx, my):
    if object_coord[0][0] <= mx <= object_coord[1][0] and object_coord[0][1] <= my <= object_coord[1][1]:
        return True
    else:
        return False


class build_object_manager:
    def __init__(self):
        self.objects = None
        self.build_map = STRUCT.SBuild_Map(build_coord.GetStartX(), build_coord.GetStartY(),
                                           build_coord.GetTileWidth(), build_coord.GetTileHeight())
        self.nMouseX = 400
        self.nMouseY = 300
        self.nClickedMouseX = None
        self.nClickedMouseY = None
        self.build_tech = build_tree()

        self.select_object = Obj_Build_Tent(self.nMouseX, self.nMouseY)
        pass

    def build_object(self, obj):
        if obj is None:
            return
        if self.build_map.CheckBuildable(obj.posObject.x, obj.posObject.y, obj.nSizeX, obj.nSizeY):
            self.build_map.BuildObject(obj.posObject.x, obj.posObject.y, obj.nSizeX, obj.nSizeY)
            if self.objects:
                self.objects += [obj]
            else:
                self.objects = [obj]

    def get_mouse_position(self, x, y):
        self.nMouseX = x
        self.nMouseY = y

    def get_clicked_mouse_position(self, x, y):
        self.nClickedMouseX = x
        self.nClickedMouseY = y
        # obj = Obj_Build_Tent(self.nClickedMouseX, self.nClickedMouseY)
        obj = self.select_object
        self.build_object(obj)
        self.select_object = self.build_tech.select_object(x, y)

    def draw_object(self):
        if self.select_object is None:
            pass
        elif self.build_map.BuildPointer(self.nMouseX, self.nMouseY, self.select_object.nSizeX,
                                         self.select_object.nSizeY):
            self.select_object.BuildObject(self.nMouseX, self.nMouseY)
            self.select_object.DrawObject()

        self.build_map.tmpDrawTable()
        if self.objects:
            for obj in self.objects:
                obj.DrawObject()
        self.build_tech.draw()


class build_tree:
    def __init__(self):
        self.image = load_image("tmpImage/tech_bg.png")
        self.pos = coord_position(BUILD_MAP_SIZE_X + BUILD_MAP_SIZE_X_EDGE, BUILD_MAP_SIZE_Y_EDGE)
        self.tech = [[], []]
        self.layer = 0
        self.tech[self.layer].append(Obj_Build_Tree(self.pos[0] + BUILD_TILE_WIDTH,
                                                    self.pos[1] + 5 * BUILD_TILE_HEIGHT))
        self.tech[self.layer].append(Obj_Build_tmp(self.pos[0] + 3 * BUILD_TILE_WIDTH,
                                                   self.pos[1] + 5 * BUILD_TILE_HEIGHT))
        self.tech[self.layer].append(Obj_Build_Tent(self.pos[0] + 5 * BUILD_TILE_WIDTH,
                                                    self.pos[1] + 5 * BUILD_TILE_HEIGHT))
        self.object_coord = [OBJECT_TREE, OBJECT_TMP, OBJECT_TENT]
        # 모든 종류의 건물들 레이어 별로 생성
        pass

    def select_object(self, mx, my):
        count = 0
        for o in self.object_coord:
            if point_in_box(o, mx, my):
                if count == 0:
                    return Obj_Build_Tree(mx, my)
                elif count == 1:
                    return Obj_Build_tmp(mx, my)
                elif count == 2:
                    return Obj_Build_Tent(mx, my)
            else:
                count += 1

        return None

    def select_layer(self):
        pass

    def draw(self):
        self.image.draw(self.pos[0] + BUILD_MAP_SIZE_X_EDGE * BUILD_TILE_WIDTH / 2,
                        self.pos[1] + BUILD_MAP_SIZE_Y_EDGE * BUILD_TILE_HEIGHT / 2,
                        BUILD_MAP_SIZE_X_EDGE * BUILD_TILE_WIDTH, BUILD_MAP_SIZE_Y_EDGE * BUILD_TILE_HEIGHT)
        for obj in self.tech[self.layer]:
            obj.DrawObject()

        pico2d.draw_rectangle(OBJECT_TREE[0][0], OBJECT_TREE[0][1], OBJECT_TREE[1][0], OBJECT_TREE[1][1])
        pico2d.draw_rectangle(OBJECT_TMP[0][0], OBJECT_TMP[0][1], OBJECT_TMP[1][0], OBJECT_TMP[1][1])
        pico2d.draw_rectangle(OBJECT_TENT[0][0], OBJECT_TENT[0][1], OBJECT_TENT[1][0], OBJECT_TENT[1][1])
