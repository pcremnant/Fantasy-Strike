from pico2d import *
import CObjects as OBJECT
import CBasicDefines as DEFINE
import CStruct as STRUCT
import CFramework as FRAMEWORK

open_canvas(DEFINE.WINDOW_WIDTH, DEFINE.WINDOW_HEIGHT)

nFrameworkType = DEFINE.FRAMEWORK_TYPE_MAIN

framework = [FRAMEWORK.CMain(DEFINE.FRAMEWORK_TYPE_MAIN, "tmpMain.png"),
             FRAMEWORK.CBuild(DEFINE.FRAMEWORK_TYPE_BUILD, "battleback10.png"),
             FRAMEWORK.CBattle(DEFINE.FRAMEWORK_TYPE_BATTLE, "battleback2.png")]

nMouseX = 0
nMouseY = 0
nClickedMouseX = 300
nClickedMouseY = 400

framework[nFrameworkType].UseFramework()

while framework[nFrameworkType].IsRunning():
    clear_canvas()
    framework[nFrameworkType].DrawObjects()

    tmpType = framework[nFrameworkType].Update()

    if tmpType == DEFINE.FRAMEWORK_TYPE_QUIT:
        break
    elif tmpType != nFrameworkType:
        framework[nFrameworkType].UnusedFramework()
        framework[nFrameworkType].nNextFrameworkType = nFrameworkType
        nFrameworkType = tmpType
        framework[nFrameworkType].UseFramework()



    update_canvas()
    delay(0.001)
