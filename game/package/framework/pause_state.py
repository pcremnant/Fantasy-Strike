from ..framework import game_framework
from ..basic_module.basic_define import *
from ..basic_module import basic_struct
from pico2d import *

name = "battle_state"

MENU_INDEX_PAUSE = 0
MENU_INDEX_RESUME = 1
MENU_INDEX_QUIT = 2

PAUSE_STATE_PAUSE = [WINDOW_WIDTH // 2, WINDOW_HEIGHT - 100, 500, 130, 'resource/UI/pause.png']
PAUSE_STATE_RESUME = [WINDOW_WIDTH // 2, WINDOW_HEIGHT - 400, 500, 130, 'resource/UI/pause_resume.png']
PAUSE_STATE_QUIT = [WINDOW_WIDTH // 2, WINDOW_HEIGHT - 600, 500, 130, 'resource/UI/pause_quit.png']


# position / width / height / image


class Pause_State:
    def __init__(self):
        self.mouse_x = 0
        self.mouse_y = 0
        self.background_image = None
        self.menu = []

    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                game_framework.quit()
            elif event.type == SDL_KEYDOWN:
                pass
                # if event.key == SDLK_ESCAPE:
                #     return HANDLE_EVENT_QUIT_STATE
                # elif event.key == SDLK_SPACE:
                #     return HANDLE_EVENT_EXIT_PAUSE

            elif event.type == SDL_MOUSEBUTTONDOWN:
                index = 0
                for m in self.menu:
                    if m.is_selected:
                        break
                    index += 1
                if index == MENU_INDEX_RESUME:
                    return HANDLE_EVENT_EXIT_PAUSE
                elif index == MENU_INDEX_QUIT:
                    return HANDLE_EVENT_QUIT_STATE

                pass
            elif event.type == SDL_MOUSEMOTION:
                self.mouse_x = event.x
                self.mouse_y = WINDOW_HEIGHT - event.y
                index = 0
                for m in self.menu:
                    if index != MENU_INDEX_PAUSE:
                        m.check_in_box(self.mouse_x, self.mouse_y)
                    index += 1
            return HANDLE_EVENT_NONE

        pass

    def enter(self):
        self.mouse_x = 0
        self.mouse_y = 0
        self.background_image = basic_struct.Image("resource/background/pause_state.png", IMAGE_TYPE_SPRITE)
        self.background_image.set_image_frame(1, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.menu.append(basic_struct.Menu(*PAUSE_STATE_PAUSE))
        self.menu.append(basic_struct.Menu(*PAUSE_STATE_RESUME))
        self.menu.append(basic_struct.Menu(*PAUSE_STATE_QUIT))
        pass

    def exit(self):
        pass

    def draw(self):
        self.background_image.draw_image(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        for m in self.menu:
            m.draw()

    def pause(self):
        pass

    def resume(self):
        pass

    def update(self):
        pass
