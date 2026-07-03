import arcade

SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Пинг-понг от Чака"

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

        self.shape_list = arcade.ShapeElementList()

        color_top = (40, 40, 80)
        color_mid = (20, 20, 60)
        color_bottom = (10, 10, 30)

        mid_y = height / 2

        bottom_points = (
            (0, 0),
            (width, 0),
            (width, mid_y),
            (0, mid_y)
        )
        bottom_colors = (color_bottom, color_bottom, color_mid, color_mid)
        rect_bottom = arcade.create_rectangle_filled_with_colors(bottom_points, bottom_colors)
        self.shape_list.append(rect_bottom)

        top_points = (
            (0, mid_y),
            (width, mid_y),
            (width, height),
            (0, height)
        )
        top_colors = (color_mid, color_mid, color_top, color_top)
        rect_top = arcade.create_rectangle_filled_with_colors(top_points, top_colors)
        self.shape_list.append(rect_top)

        self.ball = Ball("ball.png", 0.15)
        self.bar = Bar("bar.png", 0.2)

        self.ball.color = (100, 150, 255, 200)
        self.bar.color = (80, 80, 200, 200)

    def on_key_press(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.bar.change_x = -SPEED_X
        if key == arcade.key.RIGHT:
            self.bar.change_x = SPEED_X

    def on_key_release(self, symbol: int, modifiers: int):
        if symbol == arcade.key.LEFT or symbol == arcade.key.RIGHT:
            self.bar.change_x = 0

    def on_draw(self):
        arcade.start_render()

        self.shape_list.draw()

        self.ball.draw()
        self.bar.draw()

        arcade.draw_text("Пинг-понг от Чака", SCREEN_WIDTH - 200, SCREEN_HEIGHT - 30,
                         (100, 100, 200), 16, font_name="Arial",
                         bold=True)

    def update(self, delta_time: float):
        self.ball.update()
        self.bar.update()

        if arcade.check_for_collision(self.ball, self.bar):
            self.ball.change_y = -self.ball.change_y

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