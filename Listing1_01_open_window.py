"""
platformer Game (plat平台，former框架，Game游戏)
"""
import arcade #导入游戏库 arcade

#Constants常量，恒定
SCREEN_WIDTH=1000#screen屏幕_width宽度
SCREEN_HEIGHT=650#screen屏幕_height高度
SCREEN_TITLE="Platformer"#screen屏幕_title标题

class MyGame(arcade.Window):
    #类型 名称MyGame【目录名用于搜索】(用arcade库。窗口)：
    """#注释
    Main application class.#主要 应用程序 类型
    """#注释

    def __init__(self):

        # Call the parent class and set up the window
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

        arcade.set_background_color(arcade.csscolor.CORNFLOWER_BLUE)

    def setup(self):
        """Set up the game here. Call this function to restart the game."""
        pass

    def on_draw(self):
        """Render the screen."""

        arcade.start_render()
        # Code to draw the screen goes here


def main():
    """Main method"""
    window = MyGame()
    window.setup()
    arcade.run()


if __name__ == "__main__":
    main()