from pico2d import *
from game.package.framework import game_framework
from game.package.basic_module import basic_define

open_canvas(basic_define.WINDOW_WIDTH, basic_define.WINDOW_HEIGHT)
from game.package.framework.states import *

game_framework.run(MainState)
close_canvas()
