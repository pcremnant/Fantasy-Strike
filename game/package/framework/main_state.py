from pico2d import *
from game.package.basic_module import basic_struct
from ..basic_module.basic_define import *
from ..framework import game_framework
from ..framework import states

name = "main_state"

MENU_INDEX_TITLE = 0
MENU_INDEX_START = 1
MENU_INDEX_EXIT = 2

MAIN_STATE_TITLE = [WINDOW_WIDTH // 2, WINDOW_HEIGHT - 150, 1024, 256, 'resource/UI/main_title.png']
MAIN_STATE_START = [WINDOW_WIDTH // 2, WINDOW_HEIGHT - 400, 310, 130, 'resource/UI/main_start.png']
MAIN_STATE_EXIT = [WINDOW_WIDTH // 2, WINDOW_HEIGHT - 600, 249, 100, 'resource/UI/main_exit.png']


class Main_State:
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
                    game_framework.quit()
            # tmp code : button for selection will be added --------------------------------------------
            elif event.type == SDL_MOUSEBUTTONDOWN:
                index = 0
                for m in self.menu:
                    if m.is_selected:
                        break
                    index += 1
                if index == MENU_INDEX_START:
                    game_framework.change_state(states.GameState)
                elif index == MENU_INDEX_EXIT:
                    game_framework.quit()

            # ------------------------------------------------------------------------------------------
            elif event.type == SDL_MOUSEMOTION:
                self.mouse_x = event.x
                self.mouse_y = WINDOW_HEIGHT - event.y
                index = 0
                for m in self.menu:
                    if index != MENU_INDEX_TITLE:
                        m.check_in_box(self.mouse_x, self.mouse_y)
                    index += 1
        pass

    def enter(self):
        if self.background_image is None:
            self.background_image = basic_struct.Image("resource/background/main_state.png", IMAGE_TYPE_SPRITE)
            self.background_image.set_image_frame(1, WINDOW_WIDTH, WINDOW_HEIGHT)
        if len(self.menu) == 0:
            self.menu.append(basic_struct.Menu(*MAIN_STATE_TITLE))
            self.menu.append(basic_struct.Menu(*MAIN_STATE_START))
            self.menu.append(basic_struct.Menu(*MAIN_STATE_EXIT))
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
