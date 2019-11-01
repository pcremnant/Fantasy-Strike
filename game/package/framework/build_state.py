from pico2d import *
from ..object.build_object_manager import *
from ..framework import game_framework
from ..framework import states

name = "build_state"


class Build_State:
    def __init__(self):
        self.mouse_clicked_x = 0
        self.mouse_clicked_y = 0
        self.mouse_x = 0
        self.mouse_y = 0
        self.build_manager = Build_Object_Manager()
        self.background_image = None

    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                game_framework.quit()
            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_ESCAPE:
                    game_framework.change_state(states.MainState)

            elif event.type == SDL_MOUSEBUTTONDOWN:
                self.mouse_clicked_x = event.x
                self.mouse_clicked_y = WINDOW_HEIGHT - event.y
                self.build_manager.get_clicked_mouse_position(self.mouse_clicked_x, self.mouse_clicked_y)

            elif event.type == SDL_MOUSEMOTION:
                self.mouse_x = event.x
                self.mouse_y = WINDOW_HEIGHT - event.y
                self.build_manager.get_mouse_position(self.mouse_x, self.mouse_y)

        pass

    def enter(self):
        self.mouse_clicked_x = 0
        self.mouse_clicked_y = 0
        self.mouse_x = 0
        self.mouse_y = 0
        self.build_manager = Build_Object_Manager()
        self.background_image = STRUCT.Image("tmpImage/battleback10.png", IMAGE_TYPE_SPRITE)
        self.background_image.set_image_frame(1, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.background_image.set_position(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        pass

    def exit(self):
        del self.build_manager
        pass

    def draw(self):
        self.background_image.draw_image()
        self.build_manager.draw_object()

    def pause(self):
        pass

    def resume(self):
        pass

    def update(self):
        pass



