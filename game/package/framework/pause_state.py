from ..framework import game_framework
from ..basic_module.basic_define import *
from ..basic_module import basic_struct
from pico2d import *

name = "battle_state"


class Pause_State:
    def __init__(self):
        self.mouse_clicked_x = 0
        self.mouse_clicked_y = 0
        self.mouse_x = 0
        self.mouse_y = 0
        self.background_image = None

    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                game_framework.quit()
            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_ESCAPE:
                    return HANDLE_EVENT_QUIT_STATE
                elif event.key == SDLK_SPACE:
                    return HANDLE_EVENT_EXIT_PAUSE

            elif event.type == SDL_MOUSEBUTTONDOWN:
                self.mouse_clicked_x = event.x
                self.mouse_clicked_y = WINDOW_HEIGHT - event.y

            elif event.type == SDL_MOUSEMOTION:
                self.mouse_x = event.x
                self.mouse_y = WINDOW_HEIGHT - event.y
            return HANDLE_EVENT_NONE

        pass

    def enter(self):
        self.mouse_clicked_x = 0
        self.mouse_clicked_y = 0
        self.mouse_x = 0
        self.mouse_y = 0
        self.background_image = basic_struct.Image("resource/background/pause.png", IMAGE_TYPE_SPRITE)
        self.background_image.set_image_frame(1, WINDOW_WIDTH - 100, WINDOW_HEIGHT - 100)
        pass

    def exit(self):
        pass

    def draw(self):
        self.background_image.draw_image(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)

    def pause(self):
        pass

    def resume(self):
        pass

    def update(self):
        pass
