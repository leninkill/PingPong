import arcade

class Ball(arcade.Sprite):
    def update(self):
        self.center_x += 1

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
        self.ball.center_x = 300
        self.ball.center_y = 300


    def on_draw(self):
        arcade.start_render()

        # 4. Отрисовываем обе половины за один вызов
        self.shape_list.draw()

        self.ball.draw()

    def update(self, delta_time: float):
        self.ball.update()


window = Gay(600, 600, "ПИВО ЛЬЕТСЯ ЧЕРЕЗ КРАЙ СПИРИТЫ ЕБУТ КИТАЙ")

arcade.run()
