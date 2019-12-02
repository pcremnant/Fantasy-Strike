from game.package.manager.building_manager import *
from ..framework import game_framework
from ..framework import build_state
from ..framework import battle_state
from ..framework import pause_state
from ..framework import states


class Game_State:
    def __init__(self):
        self.build_state = build_state.Build_State()
        self.battle_state = battle_state.Battle_State()
        self.pause_state = pause_state.Pause_State()
        self.current_state = self.build_state
        self.is_pause_state = False
        self.font = load_font('tmp.ttf', 36)
        self.current_resource = None
        self.image_wood = basic_struct.Image('resource/UI/ui_resource_wood.png', IMAGE_TYPE_SPRITE)
        self.image_stone = basic_struct.Image('resource/UI/ui_resource_stone.png', IMAGE_TYPE_SPRITE)
        self.image_wood.set_image_frame(1, 64, 64)
        self.image_stone.set_image_frame(1, 64, 64)

    def handle_events(self):
        get_event = None
        if self.is_pause_state:
            get_event = self.pause_state.handle_events()
        else:
            get_event = self.current_state.handle_events()
        #
        if get_event == HANDLE_EVENT_NONE:
            pass
        elif get_event == HANDLE_EVENT_CHANGE_STATE:
            if self.current_state == self.battle_state:
                self.current_state = self.build_state
            elif self.current_state == self.build_state:
                self.current_state = self.battle_state
        elif get_event == HANDLE_EVENT_QUIT_STATE:
            game_framework.change_state(states.MainState)
        elif get_event == HANDLE_EVENT_ENTER_PAUSE:
            self.is_pause_state = True
        elif get_event == HANDLE_EVENT_EXIT_PAUSE:
            self.is_pause_state = False

        pass

    def enter(self):
        self.battle_state.enter()
        self.build_state.enter()
        self.pause_state.enter()
        self.current_state = self.build_state
        self.is_pause_state = False
        pass

    def exit(self):
        self.build_state.exit()
        self.battle_state.exit()
        self.pause_state.exit()
        pass

    def draw(self):
        self.current_state.draw()
        if self.is_pause_state:
            self.pause_state.draw()
        self.image_wood.image.clip_draw(0, 0, 64, 64, WINDOW_WIDTH / 2 + 300, WINDOW_HEIGHT - 50, 32, 32)
        self.image_stone.image.clip_draw(0, 0, 64, 64, WINDOW_WIDTH / 2 + 400, WINDOW_HEIGHT - 50, 32, 32)
        basic_struct.ui.write(25, WINDOW_WIDTH / 2 + 320, WINDOW_HEIGHT - 50, '%(wood)d',
                              {'wood': self.build_state.current_resource.wood}, (0, 0, 0))
        basic_struct.ui.write(25, WINDOW_WIDTH / 2 + 420, WINDOW_HEIGHT - 50, '%(stone)d',
                              {'stone': self.build_state.current_resource.stone}, (0, 0, 0))

    def pause(self):
        pass

    def resume(self):
        pass

    def update(self):
        if self.is_pause_state:
            self.pause_state.update()
        else:
            self.build_state.update()
            self.battle_state.update()

            if self.battle_state.unit_manager.winner == 'player':
                states.ResultState.winner = 'victory'
                game_framework.change_state(states.ResultState)
            elif self.battle_state.unit_manager.winner == 'enemy':
                states.ResultState.winner = 'defeat'
                game_framework.change_state(states.ResultState)
            elif self.battle_state.unit_manager.winner == 'draw':
                states.ResultState.winner = 'draw'
                game_framework.change_state(states.ResultState)

        pass
