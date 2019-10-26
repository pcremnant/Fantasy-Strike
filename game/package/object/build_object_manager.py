from ..struct import STRUCT
from ..define import DEFINE

build_coord = STRUCT.SBuild_Coord(DEFINE.WINDOW_WIDTH, DEFINE.WINDOW_HEIGHT)


class build_object_manager:
    def __init__(self):
        self.objects = None
        self.build_map = STRUCT.SBuild_Map(build_coord.GetStartX(), build_coord.GetStartY(),
                                           build_coord.GetTileWidth(), build_coord.GetTileHeight())
        pass

    def build_object(self, obj):
        if self.build_map.CheckBuildable(obj.posObject.x, obj.posObject.y, obj.sizeX, obj.sizeY):
            self.build_map.BuildObject(obj.posObject.x, obj.posObject.y, obj.sizeX, obj.sizeY)
            if self.objects:
                self.objects += [obj]
            else:
                self.objects = [obj]
            self.trees[-1].SetObjectImage(1, 64, 64)
            self.trees[-1].BuildObject(self.nClickedMouseX, self.nClickedMouseY)
