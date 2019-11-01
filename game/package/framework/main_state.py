from pico2d import *
from ..struct import STRUCT
from ..define.DEFINE import *
from ..framework import game_framework
from ..framework import states

name = "main_state"


class main_state:
    def __init__(self):
        self.nClickedMouseX = 0
        self.nClickedMouseY = 0
        self.nMouseX = 0
        self.nMouseY = 0
        self.imgBackground = None

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
                self.nClickedMouseY = WINDOW_HEIGHT - event.y

                game_framework.change_state(states.BuildState)

            elif event.type == SDL_MOUSEMOTION:
                self.nMouseX = event.x
                self.nMouseY = WINDOW_HEIGHT - event.y
        pass

    def enter(self):
        self.imgBackground = STRUCT.Image("tmpImage/tmpMain.png", IMAGE_TYPE_SPRITE)
        self.imgBackground.set_image_frame(1, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.imgBackground.set_position(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        pass

    def exit(self):
        pass

    def draw(self):
        self.imgBackground.draw_image()

    def pause(self):
        pass

    def resume(self):
        pass

    def update(self):
        pass

