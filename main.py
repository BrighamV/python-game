"""Code from a website. I typed it out myself to give me some practice"""

import random
import arcade

SPRITE_SCALING_PLAYER = 0.5
SPRITE_SCALING_COIN =0.2
COIN_COUNT = 50

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

class MyGame(arcade.Window):
    def __init__(self):
        # Call the parent class initializer
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, "Sprite Example")

        # Variables that will hod sprite lists
        self.player_list = None
        self.coin_list = None

        #set up the player info
        self.player_sprite = None
        self.score = 0

        # Dont show the mouse cursor
        self.set_mouse_visible(False)

        arcade.set_background_color(arcade.color.AMAZON)

    def setup(self):
        """ Set up the game and initialize the variabes"""

        # Sprite lists
        self.player_list = arcade.SpriteList()
        self.coin_list = arcade.SpriteList()

        #score
        self.score = 0

        #set up the player
        self.player_sprite = arcade.Sprite("myGuy.img", SPRITE_SCALING_PLAYER)
        self.player_sprite.center_x = 50
        self.player_sprite.center_y = 50
        self.player_list.append(self.player_sprite)

        #create the coins
        for i in range(COIN_COUNT):

            #CREATE THE COIN INSTANCE
            coin = arcade.Sprite("coins.img", SPRITE_SCALING_COIN)

            #position the coin
            coin.center_x = random.randrange(SCREEN_WIDTH)
            coin.center_y = random.randrange(SCREEN_HEIGHT)

            # ADD THE COIN TO THE LISTS
            self.coin_list.append(coin)

    def on_draw(self):
        """draw the character and coins"""
        arcade.start_render()
        self.con_list.draw()
        self.player_list.draw()

        #put the text on the screen.
        output = "Score: {self.score}"
        arcade.draw_text(output, 10, 20, arcade.color.WHITE, 14)

    def on_mouse_motion(self, x, y, dx, dy):
        """Mouse motion"""
        #move the center of the player sprite to match the mouse x, y
        self.player_sprite.center_x = x
        self.player_sprite.center_y = y

    def update(self, delta_time):
        """movement and game logic"""
        #call update on all sprites
        self.coin_list.update()

        #generate a list of all sprites that collided with the player.
        coins_hit_list = arcade.check_for_collision_with_list(self.player_sprite, self.coin_list)

        # Loop through each colliding sprite, remove it, and add to the score.
        for coin in coins_hit_list:
            coin.remove_from_sprite_lists()
            self.score += 1

    def main(self):
        window = MyGame()
        window.setup()
        arcade.run()

    if __name__ == "__main__":
        main()