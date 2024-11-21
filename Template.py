import arcade


SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720
SCREEN_TITLE = ""


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)

    def setup(self):
        pass

    def on_draw(self):
        self.clear()

    def update(self, delta_time):
        pass


window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()