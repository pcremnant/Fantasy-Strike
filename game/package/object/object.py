from ..struct import STRUCT


# 뭐가 있어야 될까..? 유닛 클래스
# 1. 좌표값
# 2. 이미지 / 애니메이션 관련
# 3. 스테이터스
# 4. 인공지능

# 건설 맵 크기를 몇으로 할까??
# 가로 26칸
# 세로 12칸
# tile_size = Window_Width/32 Window_Height/16 -> 나머지 칸들은 UI가 들어 갈 칸


class Object:

    def __init__(self, size_x, size_y, image_path, image_type):
        self.object_position = None
        self.class_object_image = STRUCT.Image(image_path, image_type)
        self.size_x = size_x
        self.size_y = size_y

    def set_object_frame(self, max_frame, image_width, image_height):
        self.class_object_image.set_image_frame(max_frame, image_width, image_height)

    def draw_object(self):
        pass

    def set_object_position(self, x, y):
        self.object_position = STRUCT.Position(x, y)
        self.class_object_image.set_position(x, y)
