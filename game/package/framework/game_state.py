from game.package.manager.building_manager import *
from ..framework import game_framework
from ..framework import build_state
from ..framework import battle_state
from ..framework import states


class Game_State:
    def __init__(self):
        self.build_state = build_state.Build_State()
        self.battle_state = battle_state.Battle_State()
        self.current_state = self.build_state

    def handle_events(self):
        get_event = self.current_state.handle_events()
        if get_event == HANDLE_EVENT_NONE:
            pass
        elif get_event == HANDLE_EVENT_CHANGE_STATE:
            if self.current_state == self.battle_state:
                self.current_state = self.build_state
            elif self.current_state == self.build_state:
                self.current_state = self.battle_state
        elif get_event == HANDLE_EVENT_QUIT_STATE:
            game_framework.change_state(states.MainState)
        pass

    def enter(self):
        self.battle_state.enter()
        self.build_state.enter()
        pass

    def exit(self):
        self.build_state.exit()
        self.battle_state.exit()
        # del self.build_manager
        pass

    def draw(self):
        self.current_state.draw()
        # self.background_image.draw_image(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
        # self.building_manager.draw()

    def pause(self):
        pass

    def resume(self):
        pass

    def update(self):
        self.current_state.update()
        pass
