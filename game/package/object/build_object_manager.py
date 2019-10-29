from .build_object import *

build_coord = STRUCT.SBuild_Coord(WINDOW_WIDTH, WINDOW_HEIGHT)


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
        pass

    def build_object(self, obj):
        self.build_tech.init_tree()
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
        obj = Obj_Build_tmp(self.nClickedMouseX, self.nClickedMouseY)
        self.build_object(obj)

    def draw_object(self):
        self.build_map.BuildPointer(self.nMouseX, self.nMouseY, 2, 2)
        self.build_map.tmpDrawTable()
        if self.objects:
            for obj in self.objects:
                obj.DrawObject()
        self.build_tech.draw()


class build_tree:
    def __init__(self):
        self.tech = [[], []]
        self.layer = 0
        # 모든 종류의 건물들 레이어 별로 생성
        pass

    def select_layer(self):
        pass

    def init_tree(self):
        self.tech[self.layer].append(Obj_Build_Tree(940, 100))
        self.tech[self.layer].append(Obj_Build_tmp(1000, 100))
        # self.tech += [self.layer, Obj_Build_Tree(700, 500)]
        # self.tech += [self.layer, Obj_Build_tmp(750, 500)]

    def draw(self):
        for obj in self.tech[self.layer]:
            obj.DrawObject()
