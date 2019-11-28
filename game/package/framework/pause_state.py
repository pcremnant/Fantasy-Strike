from ..framework import game_framework
from ..basic_module.basic_define import *
from ..basic_module import basic_struct
from pico2d import *

name = "battle_state"

PAUSE_STATE_PAUSE = [WINDOW_WIDTH // 2, WINDOW_HEIGHT - 100, 500, 130]
PAUSE_STATE_RESUME = [WINDOW_WIDTH // 2, WINDOW_HEIGHT - 400, 500, 130]
PAUSE_STATE_QUIT = [WINDOW_WIDTH // 2, WINDOW_HEIGHT - 600, 500, 130]


# position / width / height / image
class Menu:
    def __init__(self, x, y, w, h, image_path):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.image = basic_struct.Image(image_path, IMAGE_TYPE_SPRITE)
        self.image.set_image_frame(1, self.width, self.height)
        self.is_selected = False

    def draw(self):
        if self.is_selected:
            self.image.draw_image(self.x, self.y)
            self.image.image.clip_draw(0, 0, self.width, self.height, self.x, self.y, self.width + 100,
                                       self.height + 20)
            # draw_rectangle(self.x - self.width / 2, self.y - self.height / 2, self.x + self.width / 2,
            #                self.y + self.height / 2)
        else:
            self.image.draw_image(self.x, self.y)

    def check_in_box(self, x, y):
        if self.x - self.width / 2 <= x <= self.x + self.width / 2 and \
                self.y - self.height / 2 <= y <= self.y + self.height / 2:
            self.is_selected = True
        else:
            self.is_selected = False


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
                if event.key == SDLK_ESCAPE:
                    return HANDLE_EVENT_QUIT_STATE
                elif event.key == SDLK_SPACE:
                    return HANDLE_EVENT_EXIT_PAUSE

            elif event.type == SDL_MOUSEBUTTONDOWN:
                index = 0
                for m in self.menu:
                    if m.is_selected:
                        break
                    index += 1
                if index == 1:
                    return HANDLE_EVENT_EXIT_PAUSE
                elif index == 2:
                    return HANDLE_EVENT_QUIT_STATE

                pass
            elif event.type == SDL_MOUSEMOTION:
                self.mouse_x = event.x
                self.mouse_y = WINDOW_HEIGHT - event.y
                for m in self.menu:
                    m.check_in_box(self.mouse_x, self.mouse_y)
            return HANDLE_EVENT_NONE

        pass

    def enter(self):
        self.mouse_x = 0
        self.mouse_y = 0
        self.background_image = basic_struct.Image("resource/background/pause_state.png", IMAGE_TYPE_SPRITE)
        self.background_image.set_image_frame(1, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.menu.append(Menu(*PAUSE_STATE_PAUSE, 'resource/UI/pause.png'))
        self.menu.append(Menu(*PAUSE_STATE_RESUME, 'resource/UI/pause_resume.png'))
        self.menu.append(Menu(*PAUSE_STATE_QUIT, 'resource/UI/pause_quit.png'))
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
