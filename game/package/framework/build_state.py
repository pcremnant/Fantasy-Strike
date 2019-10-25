from pico2d import *
from ..struct import STRUCT
from ..define import DEFINE
from ..object import OBJECT
from ..framework import game_framework

name = "build_state"


class build_state:
    def __init__(self):
        self.nClickedMouseX = 0
        self.nClickedMouseY = 0
        self.nMouseX = 0
        self.nMouseY = 0
        self.imgBackground = None

        self.build = None

        self.buildMap = STRUCT.SBuild_Map(OBJECT.cBuildMap.GetStartX(), OBJECT.cBuildMap.GetStartY(),
                                          OBJECT.cBuildMap.GetTileWidth(), OBJECT.cBuildMap.GetTileHeight())

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
        self.build = OBJECT.Obj_Build(400, 300, 2, 2, "tmpImage/tree_A.png")
        self.build.SetObjectImage(1, 64, 64)

        pass

    def exit(self):
        pass

    def draw(self):
        self.imgBackground.DrawImage()
        self.buildMap.BuildPointer(self.nMouseX, self.nMouseY, 2, 2)
        self.build.DrawObject()
        self.buildMap.tmpDrawTable()

    def pause(self):
        pass

    def resume(self):
        pass

    def update(self):
        if self.buildMap.CheckBuildable(self.nClickedMouseX, self.nClickedMouseY, 2, 2):
            self.buildMap.InitTable()
            self.buildMap.BuildObject(self.nClickedMouseX, self.nClickedMouseY, 2, 2)
            self.build.BuildObject(self.nClickedMouseX, self.nClickedMouseY)


BuildState = build_state()