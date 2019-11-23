from game.package.manager.building_manager import *
from ..framework import game_framework
from ..framework import states

name = "build_state"


class Build_State:
    def __init__(self):
        self.mouse_clicked_x = 0
        self.mouse_clicked_y = 0
        self.mouse_x = 0
        self.mouse_y = 0
        self.building_manager = BuildingManager()
        self.background_image = None

    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                game_framework.quit()
            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_ESCAPE:
                    return HANDLE_EVENT_QUIT_STATE
                elif event.key == SDLK_q:
                    return HANDLE_EVENT_CHANGE_STATE

            elif event.type == SDL_MOUSEBUTTONDOWN:
                self.mouse_clicked_x = event.x
                self.mouse_clicked_y = WINDOW_HEIGHT - event.y
                self.building_manager.get_clicked_mouse_position(self.mouse_clicked_x, self.mouse_clicked_y)

            elif event.type == SDL_MOUSEMOTION:
                self.mouse_x = event.x
                self.mouse_y = WINDOW_HEIGHT - event.y
                self.building_manager.get_mouse_position(self.mouse_x, self.mouse_y)

            return HANDLE_EVENT_NONE
        pass

    def enter(self):
        self.mouse_clicked_x = 0
        self.mouse_clicked_y = 0
        self.mouse_x = 0
        self.mouse_y = 0
        if self.building_manager is None:
            self.building_manager = BuildingManager()
        self.background_image = basic_struct.Image("resource/background/build_state.png", IMAGE_TYPE_SPRITE)
        self.background_image.set_image_frame(1, WINDOW_WIDTH, WINDOW_HEIGHT)
        pass

    def exit(self):
        del self.building_manager
        self.building_manager = None
        pass

    def draw(self):
        self.background_image.draw_image(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        self.building_manager.draw()

    def pause(self):
        pass

    def resume(self):
        pass

    def update(self):
        pass



