from pico2d import *
from game.package.framework import game_framework
from game.package.define import DEFINE

open_canvas(DEFINE.WINDOW_WIDTH, DEFINE.WINDOW_HEIGHT)
from game.package.framework.states import *

game_framework.run(MainState)
close_canvas()
