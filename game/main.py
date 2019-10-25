# from pico2d import *
# from game.package.framework import FRAMEWORK
# from game.package.define import DEFINE
#
# open_canvas(DEFINE.WINDOW_WIDTH, DEFINE.WINDOW_HEIGHT)
#
# nFrameworkType = DEFINE.FRAMEWORK_TYPE_MAIN
#
# framework = [FRAMEWORK.CMain(DEFINE.FRAMEWORK_TYPE_MAIN, "tmpImage/tmpMain.png"),
#              FRAMEWORK.CBuild(DEFINE.FRAMEWORK_TYPE_BUILD, "tmpImage/battleback10.png"),
#              FRAMEWORK.CBattle(DEFINE.FRAMEWORK_TYPE_BATTLE, "tmpImage/battleback2.png")]
#
# framework[nFrameworkType].UseFramework()
#
# while framework[nFrameworkType].IsRunning():
#     clear_canvas()
#     framework[nFrameworkType].handle_events()
#     framework[nFrameworkType].DrawObjects()
#     tmpType = framework[nFrameworkType].Update()
#
#     if tmpType == DEFINE.FRAMEWORK_TYPE_QUIT:
#         break
#     elif tmpType != nFrameworkType:
#         framework[nFrameworkType].UnusedFramework()
#         framework[nFrameworkType].nNextFrameworkType = nFrameworkType
#         nFrameworkType = tmpType
#         framework[nFrameworkType].UseFramework()
#
#     update_canvas()
#     delay(0.001)
from pico2d import *
from game.package.framework import game_framework
from game.package.framework import main_state
from game.package.define import DEFINE

open_canvas(DEFINE.WINDOW_WIDTH, DEFINE.WINDOW_HEIGHT)
MainState = main_state.main_state()
game_framework.run(MainState)
close_canvas()
