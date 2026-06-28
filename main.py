import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "АОК"

SPEED_X = 5
SPEED_Y = 5

class Bar(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        if self.right > SCREEN_WIDTH:
            self.right = SCREEN_WIDTH
        if self.left < 0:
            self.left = 0

class Ball(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y

        if self.right > SCREEN_WIDTH or self.left < 0:
            self.change_x = -self.change_x

        if self.top > SCREEN_HEIGHT or self.bottom < 0:
            self.change_y = -self.change_y

class Gay(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

        # 1. Создаем контейнер для фигур
        self.shape_list = arcade.ShapeElementList()

        # Определяем цвета (RGB)
        color_top = (255, 255, 255)  # Белый
        color_mid = (0, 0, 255)  # Синий
        color_bottom = (255, 0, 0)  # Красный

        # Находим координату Y для середины экрана
        mid_y = height / 2

        # --- 2. НИЖНЯЯ ПОЛОВИНА ОKНА (От Красного к Синему) ---
        bottom_points = (
            (0, 0),  # Нижний левый
            (width, 0),  # Нижний правый
            (width, mid_y),  # Средний правый
            (0, mid_y)  # Средний левый
        )
        bottom_colors = (color_bottom, color_bottom, color_mid, color_mid)
        rect_bottom = arcade.create_rectangle_filled_with_colors(bottom_points, bottom_colors)
        self.shape_list.append(rect_bottom)

        # --- 3. ВЕРХНЯЯ ПОЛОВИНА ОКНА (От Синего к Белому) ---
        top_points = (
            (0, mid_y),  # Средний левый
            (width, mid_y),  # Средний правый
            (width, height),  # Верхний правый
            (0, height)  # Верхний левый
        )
        top_colors = (color_mid, color_mid, color_top, color_top)
        rect_top = arcade.create_rectangle_filled_with_colors(top_points, top_colors)
        self.shape_list.append(rect_top)

        self.ball = Ball("ball.png", 0.1)
        self.bar = Bar("bar.png", 0.1)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.bar.change_x = -SPEED_X
        if key == arcade.key.RIGHT:
            self.bar.change_x += SPEED_X

    def on_draw(self):
        arcade.start_render()

        # 4. Отрисовываем обе половины за один вызов
        self.shape_list.draw()

        self.ball.draw()
        self.bar.draw()

    def update(self, delta_time: float):
        self.ball.update()
        self.bar.update()

    def setup(self):
        self.ball.center_x = SCREEN_WIDTH / 2
        self.ball.center_y = SCREEN_HEIGHT / 2
        self.ball.change_x = SPEED_X
        self.ball.change_y = SPEED_Y

        self.bar.center_x = SCREEN_WIDTH / 2
        self.bar.center_y = 20


window = Gay(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()

arcade.run()
