from ..framework import game_framework
from ..framework import states
from pico2d import *
from game.package.manager.unit_manager import *

name = "battle_state"


class Battle_State:
    def __init__(self):
        self.mouse_clicked_x = 0
        self.mouse_clicked_y = 0
        self.mouse_x = 0
        self.mouse_y = 0

        self.unit_manager = UnitManager()
        # self.unit_map = basic_struct.Unit_Map() # tmp code : to test unit_map
        self.background_image = None

    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                game_framework.quit()
            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_ESCAPE:
                    game_framework.change_state(states.MainState)
                elif event.key == SDLK_q:
                    game_framework.change_state(states.BuildState)

            elif event.type == SDL_MOUSEBUTTONDOWN:
                self.mouse_clicked_x = event.x
                self.mouse_clicked_y = WINDOW_HEIGHT - event.y

            elif event.type == SDL_MOUSEMOTION:
                self.mouse_x = event.x
                self.mouse_y = WINDOW_HEIGHT - event.y

        pass

    def enter(self):
        self.mouse_clicked_x = 0
        self.mouse_clicked_y = 0
        self.mouse_x = 0
        self.mouse_y = 0
        self.background_image = basic_struct.Image("resource/background/battle_state.png", IMAGE_TYPE_SPRITE)
        self.background_image.set_image_frame(1, WINDOW_WIDTH, WINDOW_HEIGHT)
        pass

    def exit(self):
        pass

    def draw(self):
        self.background_image.draw_image(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        self.unit_manager.draw()
        # self.unit_map.tmp_draw_table()

    def pause(self):
        pass

    def resume(self):
        pass

    def update(self):
        pass
