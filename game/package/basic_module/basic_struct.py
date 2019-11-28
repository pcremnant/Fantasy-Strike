from game.package.basic_module.basic_define import *


class Position:

    def __init__(self, x, y):
        self.x = x
        self.y = y
        pass

    def set_position(self, x, y):
        self.x = x
        self.y = y

    def move_position(self, x, y):
        self.x += x
        self.y += y


class Status:

    def __init__(self, max_hp, move_speed, attack_power, attack_speed, attack_range):
        self.max_hp = max_hp
        self.current_hp = self.max_hp
        self.move_speed = move_speed
        self.attack_power = attack_power
        self.attack_speed = attack_speed
        self.attack_range = attack_range
        # add more status
        pass


class Image:

    def __init__(self, imgPath, imgType):
        self.image_type = imgType
        if imgType == IMAGE_TYPE_SPRITE:
            self.image = pico2d.load_image(imgPath)
        elif imgType == IMAGE_TYPE_FILES:
            self.image = []
            for path in imgPath:
                self.image.append(pico2d.load_image(path))
        self.max_frame = 0
        self.current_frame = 0
        self.mode_frame = 0
        self.image_width = 0
        self.image_height = 0
        self.is_draw = True

    def draw_image(self, x, y):
        if self.is_draw:
            if self.image_type == IMAGE_TYPE_SPRITE:
                self.image.clip_draw((self.current_frame // SUB_FRAME) * self.image_width,
                                     self.mode_frame * self.image_height,
                                     self.image_width, self.image_height, x, y)
            elif self.image_type == IMAGE_TYPE_FILES:
                self.image[self.current_frame // SUB_FRAME].clip_draw(0, 0,
                                                                      self.image_width, self.image_height, x, y)
            # self.current_frame += 1
            # self.current_frame = self.current_frame % self.max_frame
            self.current_frame += 1
            if self.current_frame / SUB_FRAME >= self.max_frame:
                self.current_frame = 0

    def draw_on_map(self, x, y, map_width, map_height, size_x, size_y):
        if self.is_draw:
            addW = map_width
            addH = map_height
            if size_x % 2 == 0:
                addW = 0
            if size_y % 2 == 0:
                addH = 0
            if self.image_type == IMAGE_TYPE_SPRITE:
                self.image.clip_draw((self.current_frame // SUB_FRAME) * self.image_width,
                                     self.mode_frame * self.image_height,
                                     self.image_width, self.image_height,
                                     x + addW / 2, y + addH / 2, map_width * size_x, map_height * size_y)
            elif self.image_type == IMAGE_TYPE_FILES:
                self.image[self.current_frame // SUB_FRAME].clip_draw(0, 0, self.image_width, self.image_height,
                                                                      x + addW / 2, y + addH / 2,
                                                                      map_width * size_x, map_height * size_y)
            self.current_frame += 1
            if self.current_frame / SUB_FRAME >= self.max_frame:
                self.current_frame = 0

    def set_image_frame(self, maxFrame, imgWidth, imgHeight):  # 이미지 초기 세팅
        self.max_frame = maxFrame  # 최대 프레임
        self.image_width = imgWidth  # 한 프레임의 너비
        self.image_height = imgHeight  # 한 프레임의 높이

    def set_frame_mode(self, action):
        if action < 0:
            return False
        self.mode_frame = action


class Menu:
    def __init__(self, x, y, w, h, image_path):
        self.x = x
        self.y = y
        self.width = w
        self.height = h
        self.image = Image(image_path, IMAGE_TYPE_SPRITE)
        self.image.set_image_frame(1, self.width, self.height)
        self.is_selected = False

    def draw(self):
        if self.is_selected:
            self.image.image.clip_draw(0, 0, self.width, self.height, self.x, self.y, self.width + 100,
                                       self.height + 20)
            # draw_rectangle(self.x - self.width / 2, self.y - self.height / 2, self.x + self.width / 2,
            #                self.y + self.height / 2)
        else:
            self.image.draw_image(self.x, self.y)

    def check_in_box(self, x, y):
        if self.x - self.width / 2 <= x <= self.x + self.width / 2 and \
                self.y - self.height / 2 <= y <= self.y + self.height / 2:
            self.is_selected = True
        else:
            self.is_selected = False
