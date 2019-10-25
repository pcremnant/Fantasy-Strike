from pico2d import *
from struct import Struct as STRUCT
from ..define import DEFINE


class main_state:
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

    def Enter(self):
        pass

    def UseFramework(self):
        self.bRunning = True

    def Exit(self):
        self.bRunning = False

    def Draw(self):
        self.imgBackground.DrawImage()

    def Update(self):
        if self.bRunning:
            return self.nFrameworkType
        else:
            return self.nNextFrameworkType
