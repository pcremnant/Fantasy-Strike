from pico2d import *
from game.package.basic_module import basic_struct
from ..basic_module.basic_define import *
from ..framework import game_framework
from ..framework import states

name = "main_state"

MENU_INDEX_VICTORY = 0
MENU_INDEX_DEFEAT = 1
MENU_INDEX_DRAW = 2

RESULT_STATE_VICTORY = [WINDOW_WIDTH // 2, WINDOW_HEIGHT//2, 452, 166, 'resource/UI/result_victory.png']
RESULT_STATE_DEFEAT = [WINDOW_WIDTH // 2, WINDOW_HEIGHT//2, 387, 173, 'resource/UI/result_defeat.png']
RESULT_STATE_DRAW = [WINDOW_WIDTH // 2, WINDOW_HEIGHT//2, 310, 109, 'resource/UI/result_draw.png']


class Result_State:
    def __init__(self):
        self.mouse_x = 0
        self.mouse_y = 0
        self.background_image = None
        self.winner = None
        self.menu_victory = None
        self.menu_defeat = None
        self.menu_draw = None
        self.menu = None
        self.timer = 0

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
                pass
            # ------------------------------------------------------------------------------------------
            elif event.type == SDL_MOUSEMOTION:
                self.mouse_x = event.x
                self.mouse_y = WINDOW_HEIGHT - event.y
        pass

    def enter(self):
        self.timer = 0
        self.background_image = basic_struct.Image("resource/background/main_state.png", IMAGE_TYPE_SPRITE)
        self.background_image.set_image_frame(1, WINDOW_WIDTH, WINDOW_HEIGHT)
        if self.menu_victory is None:
            self.menu_victory = basic_struct.Menu(*RESULT_STATE_VICTORY)
        if self.menu_defeat is None:
            self.menu_defeat = basic_struct.Menu(*RESULT_STATE_DEFEAT)
        if self.menu_draw is None:
            self.menu_draw = basic_struct.Menu(*RESULT_STATE_DRAW)

        if self.winner == 'victory':
            self.menu = self.menu_victory
        elif self.winner == 'defeat':
            self.menu = self.menu_defeat
        elif self.winner == 'draw':
            self.menu = self.menu_draw
        pass

    def exit(self):
        self.menu = None
        pass

    def draw(self):
        if self.background_image is not None:
            self.background_image.draw_image(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        if self.menu is not None:
            self.menu.draw()

    def pause(self):
        pass

    def resume(self):
        pass

    def update(self):
        self.timer += 1
        if self.timer > 300:
            game_framework.change_state(states.MainState)
        pass
