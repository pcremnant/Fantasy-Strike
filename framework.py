from pico2d import *
import CObjects as OBJECT
import CBasicDefines as DEFINE
import CStruct as STRUCT

open_canvas(DEFINE.WINDOW_WIDTH, DEFINE.WINDOW_HEIGHT)

nMouseX = 0
nMouseY = 0
nClickedMouseX = 300
nClickedMouseY = 400


def handle_events():
    global running
    global nClickedMouseX
    global nClickedMouseY
    global nMouseX
    global nMouseY

    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_ESCAPE:
                running = False
        elif event.type == SDL_MOUSEBUTTONDOWN:
            nClickedMouseX = event.x
            nClickedMouseY = DEFINE.WINDOW_HEIGHT - event.y
        elif event.type == SDL_MOUSEMOTION:
            nMouseX = event.x
            nMouseY = DEFINE.WINDOW_HEIGHT - event.y
            buildPointer.GetMousePosition(nMouseX, nMouseY)
    pass


build = OBJECT.Obj_Build(400, 300, 2, 2, "tree_A.png")
build.SetObjectImage(1, 64, 64)

buildPointer = OBJECT.Obj_BuildPointer(nMouseX, nMouseY, 2, 2, "tile_g.png")
buildPointer.SetObjectImage(1, 64, 64)

buildMap = STRUCT.SBuild_Map(OBJECT.cBuildMap.GetStartX(), OBJECT.cBuildMap.GetStartY(),
                             OBJECT.cBuildMap.GetTileWidth(), OBJECT.cBuildMap.GetTileHeight())

running = True

while running:
    clear_canvas()

    buildPointer.DrawObject()
    build.BuildObject(nClickedMouseX, nClickedMouseY)
    build.DrawObject()
    buildMap.tmpDrawTable()

    update_canvas()

    handle_events()
    delay(0.1)
