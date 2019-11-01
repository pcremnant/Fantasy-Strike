from pico2d import *
from ..object.build_object_manager import *
from ..framework import game_framework
from ..framework import states

name = "build_state"


class build_state:
    def __init__(self):
        self.nClickedMouseX = 0
        self.nClickedMouseY = 0
        self.nMouseX = 0
        self.nMouseY = 0
        self.build_manager = build_object_manager()
        self.imgBackground = None

    def handle_events(self):
        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                game_framework.quit()
            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_ESCAPE:
                    game_framework.change_state(states.MainState)

            elif event.type == SDL_MOUSEBUTTONDOWN:
                self.nClickedMouseX = event.x
                self.nClickedMouseY = WINDOW_HEIGHT - event.y
                self.build_manager.get_clicked_mouse_position(self.nClickedMouseX, self.nClickedMouseY)

            elif event.type == SDL_MOUSEMOTION:
                self.nMouseX = event.x
                self.nMouseY = WINDOW_HEIGHT - event.y
                self.build_manager.get_mouse_position(self.nMouseX, self.nMouseY)

        pass

    def enter(self):
        self.nClickedMouseX = 0
        self.nClickedMouseY = 0
        self.nMouseX = 0
        self.nMouseY = 0
        self.build_manager = build_object_manager()
        self.imgBackground = STRUCT.SImage("tmpImage/battleback10.png", IMAGE_TYPE_SPRITE)
        self.imgBackground.set_image_frame(1, WINDOW_WIDTH, WINDOW_HEIGHT)
        self.imgBackground.set_position(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        pass

    def exit(self):
        del self.build_manager
        pass

    def draw(self):
        self.imgBackground.draw_image()
        self.build_manager.draw_object()

    def pause(self):
        pass

    def resume(self):
        pass

    def update(self):
        pass



