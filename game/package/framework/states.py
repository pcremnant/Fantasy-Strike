from ..framework import build_state
from ..framework import main_state
from ..framework import battle_state

MainState = main_state.Main_State()
BuildState = build_state.Build_State()
BattleState = battle_state.Battle_State()


def get_building_manager():
    return BuildState.building_manager
