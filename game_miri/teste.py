import arcade

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 500
SCREEN_TITLE = "Resizing Window Example"
START = 0
END = 2000
STEP = 50

class TelaMenu(arcade.View):
    def __init__(self):
        super().__init__()

    def on_draw(self):
        arcade.start_render()
        # Draw menu screen

class TelaGame(arcade.View):
    def __init__(self):
        super().__init__()

        self.fundo = arcade.load_texture(file_name="./assets/fundo.png")
        self.jogador_sprite = arcade.AnimatedWalkingSprite()
        self.lista_pedra = arcade.SpriteList()
        self.lista_cenario = arcade.SpriteList()
        self.pos_x = 110
        self.pos_x2 = 260
        self.velocidade = 6

        self.inicializar_jogador()
        self.inicializar_cenario()
        self.inicializar_pedras()

    def inicializar_jogador(self):
        self.jogador_sprite.walk_left_textures = []
        self.jogador_sprite.walk_right_textures = []
        self.jogador_sprite.stand_right_textures = []
        self.jogador_sprite.stand_left_textures = []

        for i in range(2):
            self.jogador_sprite.walk_left_textures.append(
                arcade.load_texture(f"./assets/astronauta_{i}.png", flipped_horizontally=True)
            )
            self.jogador_sprite.walk_right_textures.append(
                arcade.load_texture(f"./assets/astronauta_{i}.png")
            )
        self.jogador_sprite.stand_right_textures.append(
            arcade.load_texture("./assets/astronauta_idle.png")
        )
        self.jogador_sprite.stand_left_textures.append(
            arcade.load_texture("./assets/astronauta_idle.png", flipped_horizontally=True)
        )

    def inicializar_cenario(self):
        self.lista_cenario = arcade.SpriteList()
        for i in range(20):
            self.lista_cenario.append(
                arcade.Sprite("./assets/chao.jpg", 1, center_x=i * self.pos_x, center_y=50)
            )

    def inicializar_pedras(self):
        self.lista_pedra = arcade.SpriteList()
        for i in range(7):
            pedra = arcade.Sprite("./assets/rocharoxa.png", 0.3, center_x=i * self.pos_x2, center_y=150)
            pedra.change_x = 2  # Add some movement to the rocks
            self.lista_pedra.append(pedra)

    def on_draw(self):
        arcade.start_render()
        arcade.draw_lrwh_rectangle_textured(0, 0, 1920, 1080, self.fundo)
        self.lista_cenario.draw()
        self.lista_pedra.draw()
        self.jogador_sprite.draw()

    def update(self, delta_time: float):
        self.lista_pedra.update()

def main():
    window = arcade.Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE, resizable=True)
    t1 = TelaMenu()
    t2 = TelaGame()
    window.show_view(t1)
    arcade.run()

if __name__ == "__main__":
    main()