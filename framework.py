from pico2d import *
import CObjects as OBJECT
import CBasicDefines as DEFINE
import CStruct as STRUCT

open_canvas(DEFINE.WINDOW_WIDTH, DEFINE.WINDOW_HEIGHT)

nMouseX = 300
nMouseY = 400


def handle_events():
    global running
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
            nMouseX = event.x
            nMouseY = DEFINE.WINDOW_HEIGHT - event.y
    pass


build = OBJECT.Obj_Build(400, 300, "64x64_tile.png")
build.SetObjectImage(1, 64, 64)

buildMap = STRUCT.SBuild_Map(OBJECT.cBuildMap.GetStartX(), OBJECT.cBuildMap.GetStartY(),
                             OBJECT.cBuildMap.GetTileWidth(), OBJECT.cBuildMap.GetTileHeight())

running = True

while running:
    clear_canvas()

    buildMap.tmpDrawTable()
    build.BuildObject(nMouseX, nMouseY)
    build.DrawObject()

    update_canvas()

    handle_events()
    delay(0.1)
