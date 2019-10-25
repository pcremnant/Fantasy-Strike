from pico2d import *
from ..struct import STRUCT
from ..define import DEFINE
from ..object import build_object
from ..framework import game_framework

name = "build_state"


class build_state:
    def __init__(self):
        self.nClickedMouseX = 0
        self.nClickedMouseY = 0
        self.nMouseX = 0
        self.nMouseY = 0
        self.imgBackground = None

        self.trees = None

        self.buildMap = STRUCT.SBuild_Map(build_object.cBuildMap.GetStartX(), build_object.cBuildMap.GetStartY(),
                                          build_object.cBuildMap.GetTileWidth(), build_object.cBuildMap.GetTileHeight())

    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                game_framework.pop_state()
            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_ESCAPE:
                    game_framework.pop_state()

            elif event.type == SDL_MOUSEBUTTONDOWN:
                self.nClickedMouseX = event.x
                self.nClickedMouseY = DEFINE.WINDOW_HEIGHT - event.y

            elif event.type == SDL_MOUSEMOTION:
                self.nMouseX = event.x
                self.nMouseY = DEFINE.WINDOW_HEIGHT - event.y

        pass

    def enter(self):
        self.imgBackground = STRUCT.SImage("tmpImage/battleback10.png")
        self.imgBackground.SetImageFrame(1, DEFINE.WINDOW_WIDTH, DEFINE.WINDOW_HEIGHT)
        self.imgBackground.SetPosition(DEFINE.WINDOW_WIDTH / 2, DEFINE.WINDOW_HEIGHT / 2)
        self.trees = [build_object.Obj_Build(400, 300, 2, 2, "tmpImage/tree_A.png")]
        self.trees[-1].SetObjectImage(1, 64, 64)
        self.buildMap.BuildObject(self.nClickedMouseX, self.nClickedMouseY, 2, 2)

        pass

    def exit(self):
        pass

    def draw(self):
        self.imgBackground.DrawImage()
        self.buildMap.BuildPointer(self.nMouseX, self.nMouseY, 2, 2)
        for obj in self.trees:
            obj.DrawObject()
        self.buildMap.tmpDrawTable()

    def pause(self):
        pass

    def resume(self):
        pass

    def update(self):
        if self.buildMap.CheckBuildable(self.nClickedMouseX, self.nClickedMouseY, 2, 2):
            self.buildMap.BuildObject(self.nClickedMouseX, self.nClickedMouseY, 2, 2)
            self.trees += [build_object.Obj_Build(400, 300, 2, 2, "tmpImage/tree_A.png")]
            self.trees[-1].SetObjectImage(1, 64, 64)
            self.trees[-1].BuildObject(self.nClickedMouseX, self.nClickedMouseY)


BuildState = build_state()
