import arcade
import asyncio
import random

SCREEN_WIDTH = 960
SCREEN_HEIGHT = 720
SCREEN_TITLE = "Car Game"
CAR_SPEED = 5
CAR_ANGLE = 20
WALL_SPEED = 5


class Game(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.bg = arcade.load_texture("bg.png")
        self.car = Car("yellow_car.png", 0.8)
        self.wall = Wall("wall.png", 0.8)
        self.score = 0
        self.game = True
        self.win = False

    def setup(self):
        self.car.center_x = SCREEN_WIDTH/2
        self.car.center_y = 135
        self.wall.center_x = SCREEN_WIDTH/2
        self.wall.center_y = SCREEN_HEIGHT
        self.wall.change_y = WALL_SPEED

    # def setup_wall(self):
    #     self.wall.center_x = random.randint(180, 780)
    #     self.wall.center_y = SCREEN_HEIGHT
    #     self.wall.change_y = WALL_SPEED

    def on_draw(self):
        self.clear()
        arcade.draw_texture_rectangle(
            SCREEN_WIDTH/2, SCREEN_HEIGHT/2, SCREEN_WIDTH, SCREEN_HEIGHT, self.bg)
        self.car.draw()
        self.wall.draw()
        arcade.draw_text(f"Score: {self.score}", 60,
                         SCREEN_HEIGHT - 50, (204, 204, 0), 40)
        if not self.game:
            arcade.draw_text(
                f"You have lost :(", SCREEN_WIDTH/2-220, SCREEN_HEIGHT/2-20, (155, 155, 130), 50)
        if self.score >= 10:
            self.win = True
            arcade.draw_text(
                f"You have Won :D", SCREEN_WIDTH/2-250, SCREEN_HEIGHT/2-20, (155, 155, 130), 50)

    def update(self, delta_time):
        if self.game and not self.win:
            self.car.update()
            self.wall.update()
        # if self.car.center_y == self.wall.center_y:
        #self.score += 1
        # if self.wall.bottom < 0:
        # self.setup_wall()
        if arcade.check_for_collision(self.wall, self.car):
            self.game = False

    def on_key_press(self, key, modifers):
        if self.game and not self.win:
            if key == arcade.key.LEFT:
                self.car.change_x = -CAR_SPEED
                self.car.angle = CAR_ANGLE
            if key == arcade.key.RIGHT:
                self.car.change_x = CAR_SPEED
                self.car.angle = -CAR_ANGLE
            #Up & Down
            if key == arcade.key.UP:
                self.car.change_y = CAR_SPEED
            if key == arcade.key.DOWN:
                self.car.change_y = -CAR_SPEED

    def on_key_release(self, key, modifiers):
        if key == arcade.key.LEFT:
            self.car.change_x = 0
            self.car.angle = 0
        if key == arcade.key.RIGHT:
            self.car.change_x = 0
            self.car.angle = 0
        if key == arcade.key.UP:
            self.car.change_y = 0
        if key == arcade.key.DOWN:
            self.car.change_y = 0


class Car(arcade.Sprite):
    def update(self):
        self.center_x += self.change_x
        self.center_y += self.change_y


class Wall(arcade.Sprite):
    def update(self):
        self.center_y -= self.change_y
        if self.top < 0:
            self.bottom = SCREEN_HEIGHT + random.randint(0, SCREEN_HEIGHT)
            self.center_x = random.randint(168, SCREEN_WIDTH-168)
            window.score += 1


window = Game(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
window.setup()
arcade.run()
