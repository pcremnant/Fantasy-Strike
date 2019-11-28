from ..framework import game_framework
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
                    return HANDLE_EVENT_ENTER_PAUSE
                elif event.key == SDLK_q:
                    return HANDLE_EVENT_CHANGE_STATE

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
        self.background_image = basic_struct.Image("resource/background/battle_state.png", IMAGE_TYPE_SPRITE)
        self.background_image.set_image_frame(1, WINDOW_WIDTH, WINDOW_HEIGHT)
        if self.unit_manager is None:
            self.unit_manager = UnitManager()
        pass

    def exit(self):
        del self.unit_manager
        self.unit_manager = None
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
        self.unit_manager.update()
        pass
