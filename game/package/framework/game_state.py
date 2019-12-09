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

        self.image_resource_board = basic_struct.Image("resource/UI/resource_board.png", IMAGE_TYPE_SPRITE)
        self.image_timer_board = basic_struct.Image("resource/UI/timer_board.png", IMAGE_TYPE_SPRITE)
        self.image_wood = basic_struct.Image('resource/UI/ui_resource_wood.png', IMAGE_TYPE_SPRITE)
        self.image_stone = basic_struct.Image('resource/UI/ui_resource_stone.png', IMAGE_TYPE_SPRITE)
        self.image_resource_board.set_image_frame(1, 256, 64)
        self.image_timer_board.set_image_frame(1, 128, 86)
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
        stopwatch.start_timer()
        stopwatch.end_timer()
        sound.play_bgm(BGM_INDEX_GAME)
        pass

    def exit(self):
        self.build_state.exit()
        self.battle_state.exit()
        self.pause_state.exit()
        sound.stop_bgm(BGM_INDEX_GAME)
        pass

    def draw(self):
        if self.is_pause_state:
            self.pause_state.draw()
        else:
            self.current_state.draw()

            # resource board
            self.image_resource_board.image.clip_draw(0, 0, 256, 64, WINDOW_WIDTH / 2 + 340, WINDOW_HEIGHT - 50, 300,
                                                      64)

            # wood resource
            wood_x = WINDOW_WIDTH / 2 + 220
            self.image_wood.image.clip_draw(0, 0, 64, 64, wood_x, WINDOW_HEIGHT - 50, 32, 32)
            basic_struct.ui.write(25, wood_x + 30, WINDOW_HEIGHT - 50, '%(wood)d',
                                  {'wood': self.build_state.current_resource.wood}, (0, 0, 0))
            basic_struct.ui.write(25, wood_x + 65, WINDOW_HEIGHT - 50, '(%(wood)d)',
                                  {'wood': self.build_state.additional_resource.wood + self.build_state.add_resource.wood}, (0, 150, 0))

            # stone resource
            stone_x = wood_x + 140
            self.image_stone.image.clip_draw(0, 0, 64, 64, stone_x, WINDOW_HEIGHT - 50, 32, 32)
            basic_struct.ui.write(25, stone_x + 30, WINDOW_HEIGHT - 50, '%(stone)d',
                                  {'stone': self.build_state.current_resource.stone}, (0, 0, 0))
            basic_struct.ui.write(25, stone_x + 65, WINDOW_HEIGHT - 50, '(%(stone)d)',
                                  {'stone': self.build_state.additional_resource.stone + self.build_state.add_resource.stone}, (0, 150, 0))

            # timer board
            self.image_timer_board.image.clip_draw(0, 0, 128, 86, WINDOW_WIDTH // 2, WINDOW_HEIGHT - 50, 120, 64)
            ui.write(36, WINDOW_WIDTH // 2 - 18, WINDOW_HEIGHT - 50, '%(timer)d',
                     {'timer': TIMER_UNIT_CREATION - int(stopwatch.get_timer())}, (0, 0, 0))

    def pause(self):
        pass

    def resume(self):
        pass

    def update(self):
        if self.is_pause_state:
            self.pause_state.update()
        else:
            stopwatch.end_timer()
            if TIMER_UNIT_CREATION - int(stopwatch.get_timer()) < 0:
                stopwatch.start_timer()
                stopwatch.end_timer()

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
