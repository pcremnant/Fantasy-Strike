from game.package.manager.building_manager import *
from ..framework import game_framework

name = "build_state"

GETTING_RESOURCE_TIME = 1000


class Build_State:
    def __init__(self):
        self.mouse_clicked_x = 0
        self.mouse_clicked_y = 0
        self.mouse_x = 0
        self.mouse_y = 0
        self.building_manager = BuildingManager()

        self.background_image = None

        self.current_resource = basic_struct.Resource()
        self.add_resource = basic_struct.Resource(2, 2)
        self.additional_resource = basic_struct.Resource(0, 0)

        self.is_given_resource = False

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
                self.building_manager.get_clicked_mouse_position(self.mouse_clicked_x, self.mouse_clicked_y,
                                                                 self.current_resource)

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
        if self.background_image is None:
            self.background_image = basic_struct.Image("resource/background/build_state.png", IMAGE_TYPE_SPRITE)
            self.background_image.set_image_frame(1, WINDOW_WIDTH, WINDOW_HEIGHT)

        pass

    def exit(self):
        del self.building_manager
        self.building_manager = None
        self.current_resource.wood = 0
        self.current_resource.stone = 0
        pass

    def draw(self):
        self.background_image.draw_image(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        self.building_manager.draw()

    def pause(self):
        pass

    def resume(self):
        pass

    def update(self):
        if stopwatch.get_timer() % 10 == 0:
            if not self.is_given_resource:
                self.additional_resource = basic_struct.Resource(*self.building_manager.get_additional_resource())
                self.current_resource.wood += self.add_resource.wood + self.additional_resource.wood
                self.current_resource.stone += self.add_resource.stone + self.additional_resource.stone
                self.is_given_resource = True
        else:
            self.is_given_resource = False
        pass
