from pico2d import *

from ..define import DEFINE
from ..object import OBJECT
from ..struct import STRUCT


# ========================================= main Framework ========================================================
class CMain:
    def __init__(self, FrameworkType, BgPath):
        self.nFrameworkType = FrameworkType
        self.bRunning = False
        self.nClickedMouseX = 0
        self.nClickedMouseY = 0
        self.nMouseX = 0
        self.nMouseY = 0
        self.imgBackground = STRUCT.SImage(BgPath)
        self.imgBackground.SetImageFrame(1, DEFINE.WINDOW_WIDTH, DEFINE.WINDOW_HEIGHT)
        self.imgBackground.SetPosition(DEFINE.WINDOW_WIDTH / 2, DEFINE.WINDOW_HEIGHT / 2)
        self.nNextFrameworkType = FrameworkType

    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                self.bRunning = False
            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_ESCAPE:
                    self.bRunning = False
                    self.nNextFrameworkType = DEFINE.FRAMEWORK_TYPE_QUIT

            elif event.type == SDL_MOUSEBUTTONDOWN:
                self.nClickedMouseX = event.x
                self.nClickedMouseY = DEFINE.WINDOW_HEIGHT - event.y
                self.bRunning = False
                self.nNextFrameworkType = DEFINE.FRAMEWORK_TYPE_BUILD

            elif event.type == SDL_MOUSEMOTION:
                self.nMouseX = event.x
                self.nMouseY = DEFINE.WINDOW_HEIGHT - event.y
        pass

    def IsRunning(self):
        return self.bRunning

    def UseFramework(self):
        self.bRunning = True

    def UnusedFramework(self):
        self.bRunning = False

    def DrawObjects(self):
        self.imgBackground.DrawImage()

    def Update(self):
        if self.bRunning:
            return self.nFrameworkType
        else:
            return self.nNextFrameworkType


# ========================================= battle Framework ========================================================
class CBattle:
    def __init__(self, FrameworkType, BgPath):
        self.nFrameworkType = FrameworkType
        self.bRunning = False
        self.nClickedMouseX = 0
        self.nClickedMouseY = 0
        self.nMouseX = 0
        self.nMouseY = 0
        self.imgBackground = STRUCT.SImage(BgPath)
        self.imgBackground.SetImageFrame(1, DEFINE.WINDOW_WIDTH, DEFINE.WINDOW_HEIGHT)
        self.imgBackground.SetPosition(DEFINE.WINDOW_WIDTH / 2, DEFINE.WINDOW_HEIGHT / 2)

    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                self.bRunning = False
            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_ESCAPE:
                    self.bRunning = False

            elif event.type == SDL_MOUSEBUTTONDOWN:
                self.nClickedMouseX = event.x
                self.nClickedMouseY = DEFINE.WINDOW_HEIGHT - event.y
            elif event.type == SDL_MOUSEMOTION:
                self.nMouseX = event.x
                self.nMouseY = DEFINE.WINDOW_HEIGHT - event.y
        pass

    def IsRunning(self):
        return self.bRunning

    def UseFramework(self):
        self.bRunning = True

    def UnusedFramework(self):
        self.bRunning = False

    def DrawObjects(self):
        self.imgBackground.DrawImage()


# ========================================= build Framework ========================================================
class CBuild:
    def __init__(self, FrameworkType, BgPath):
        self.nFrameworkType = FrameworkType
        self.bRunning = False
        self.nClickedMouseX = 0
        self.nClickedMouseY = 0
        self.nMouseX = 0
        self.nMouseY = 0
        self.imgBackground = STRUCT.SImage(BgPath)
        self.imgBackground.SetImageFrame(1, DEFINE.WINDOW_WIDTH, DEFINE.WINDOW_HEIGHT)
        self.imgBackground.SetPosition(DEFINE.WINDOW_WIDTH / 2, DEFINE.WINDOW_HEIGHT / 2)
        self.nNextFrameworkType = FrameworkType

        self.build = OBJECT.Obj_Build(400, 300, 2, 2, "tmpImage/tree_A.png")
        self.build.SetObjectImage(1, 64, 64)

        self.buildMap = STRUCT.SBuild_Map(OBJECT.cBuildMap.GetStartX(), OBJECT.cBuildMap.GetStartY(),
                                          OBJECT.cBuildMap.GetTileWidth(), OBJECT.cBuildMap.GetTileHeight())

    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                self.bRunning = False
            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_ESCAPE:
                    self.bRunning = False
                    self.nNextFrameworkType = DEFINE.FRAMEWORK_TYPE_MAIN

            elif event.type == SDL_MOUSEBUTTONDOWN:
                nClickedMouseX = event.x
                nClickedMouseY = DEFINE.WINDOW_HEIGHT - event.y
                if self.buildMap.CheckBuildable(nClickedMouseX, nClickedMouseY, 2, 2):
                    self.buildMap.InitTable()
                    self.buildMap.BuildObject(nClickedMouseX, nClickedMouseY, 2, 2)
                    self.build.BuildObject(nClickedMouseX, nClickedMouseY)

            elif event.type == SDL_MOUSEMOTION:
                self.nMouseX = event.x
                self.nMouseY = DEFINE.WINDOW_HEIGHT - event.y
        pass

    def Update(self):
        if self.bRunning:
            return self.nFrameworkType
        else:
            return self.nNextFrameworkType

    def IsRunning(self):
        return self.bRunning

    def UseFramework(self):
        self.bRunning = True

    def UnusedFramework(self):
        self.bRunning = False

    def DrawObjects(self):
        self.imgBackground.DrawImage()
        self.buildMap.BuildPointer(self.nMouseX, self.nMouseY, 2, 2)
        self.build.DrawObject()
        self.buildMap.tmpDrawTable()
