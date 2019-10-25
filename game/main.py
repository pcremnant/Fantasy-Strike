from pico2d import *
from game.package.framework import game_framework
from game.package.framework import main_state
from game.package.define import DEFINE

open_canvas(DEFINE.WINDOW_WIDTH, DEFINE.WINDOW_HEIGHT)
game_framework.run(main_state.MainState)
close_canvas()
