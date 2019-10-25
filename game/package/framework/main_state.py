from pico2d import *
from ..struct import STRUCT
from ..define import DEFINE
from ..framework import game_framework

name = "main_state"


class main_state:
    def __init__(self):
        self.nClickedMouseX = 0
        self.nClickedMouseY = 0
        self.nMouseX = 0
        self.nMouseY = 0
        self.imgBackground = STRUCT.SImage("tmpImage/tmpMain.png")
        self.imgBackground.SetImageFrame(1, DEFINE.WINDOW_WIDTH, DEFINE.WINDOW_HEIGHT)
        self.imgBackground.SetPosition(DEFINE.WINDOW_WIDTH / 2, DEFINE.WINDOW_HEIGHT / 2)

    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                game_framework.quit()
            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_ESCAPE:
                    game_framework.quit()

            elif event.type == SDL_MOUSEBUTTONDOWN:
                self.nClickedMouseX = event.x
                self.nClickedMouseY = DEFINE.WINDOW_HEIGHT - event.y
                game_framework.push_state()

            elif event.type == SDL_MOUSEMOTION:
                self.nMouseX = event.x
                self.nMouseY = DEFINE.WINDOW_HEIGHT - event.y
        pass

    def enter(self):
        pass

    def exit(self):
        pass

    def draw(self):
        self.imgBackground.DrawImage()

    def pause(self):
        pass

    def resume(self):
        pass

    def update(self):
        pass
