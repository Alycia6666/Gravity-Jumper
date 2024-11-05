import arcade
import random

class TelaGame(arcade.View):
    def __init__(self, load_posicao_X=500, load_posicao_Y=100):
        super().__init__()
        self.A_pressed = False
        self.D_pressed = False
        self.W_pressed = False 
        self.game_over = False
        self.inimigo_aparecer = True

        self.camera =arcade.Camera(self.window.width, self.window.height)
        self.gui_camera =arcade.Camera (self.window.width, self.window.height)

        self.fundo_over=arcade.load_texture(file_name="./assets/game_over.png", width=1920, height=1080)    
        self.fundo=arcade.load_texture(file_name="./assets/fundo.png", width=1500, height=750)
        self.fundo = arcade.load_texture(file_name="./assets/fundo.png")
        self.final = arcade.load_texture(file_name="./assets/aastronauta.png", width=900, height=1000)
        self.jogador=arcade.SpriteList()
        self.jogador_sprite = arcade.AnimatedWalkingSprite()
        self.jogador_sprite.center_x=100
        self.jogador_sprite.center_y=200
        self.jogador_sprite.scale=0.7

    
        self.jogador_sprite.walk_left_textures.append(
            arcade.load_texture("./assets/astronauta_idle.png",
                                flipped_horizontally=True)
        )
        self.jogador_sprite.walk_right_textures.append(
            arcade.load_texture("./assets/astronauta_idle.png")
        )

        self.jogador_sprite.walk_left_textures.append(
                arcade.load_texture("./assets/astronauta_1.png",
                                    flipped_horizontally=True)
            )
        self.jogador_sprite.walk_right_textures.append(
                arcade.load_texture("./assets/astronauta_1.png")
            )
        self.jogador_sprite.stand_right_textures.append(
                arcade.load_texture("./assets/astronauta_idle.png")
            )
        self.jogador_sprite.stand_left_textures.append(
                arcade.load_texture("./assets/astronauta_idle.png",
                                    flipped_horizontally=True)
            )
        self.jogador.append(self.jogador_sprite) # Define the sprite attribute
        self.velocidade = 6
        self.lista_pedra = arcade.SpriteList()
        self.lista_cenario = arcade.SpriteList()
        self.pos_x = 110
        self.pos_x2 = 300


        self.inimigo_sprite=arcade.AnimatedWalkingSprite()
        self.inimigo_sprite.walk_left_textures.append(arcade.load_texture("./assets/alien.png", flipped_horizontally=True))
        self.inimigo_sprite.stand_right_textures.append(arcade.load_texture("./assets/alien.png"))
        self.inimigo_sprite.walk_left_textures.append(arcade.load_texture("./assets/alien.png", flipped_horizontally=True))
        self.inimigo_sprite.walk_right_textures.append(arcade.load_texture("./assets/alien.png"))
        self.inimigo_sprite.stand_left_textures.append(arcade.load_texture("./assets/alien.png", flipped_horizontally=True))
        self.inimigo_sprite.walk_right_textures.append(arcade.load_texture("./assets/alien.png"))

        # posição, tamanho e velocidade do inimigo
        self.inimigo_sprite.center_x=100
        self.inimigo_sprite.center_y=500
        self.inimigo_sprite.scale=1.5
        self.inimigo_velocidade=2

        # configuração de dimensão de imagem do chão
        for i in range(100): 
            self.lista_cenario.append(
                arcade.Sprite("./assets/chao.jpg",
                              1,
                              center_x=i*self.pos_x,
                              center_y=50
                              )
            )
        # configuração de quantidade de rocha
        for i in range(20):
             if random.randrange(10):
                self.lista_pedra.append(
                    arcade.Sprite("./assets/rocharoxa.png",
                                  0.3,
                                  center_x=i*self.pos_x2,
                                  center_y=150))
            
        self.fisica_cenario=arcade.PhysicsEnginePlatformer(self.jogador_sprite,
                                           self.lista_cenario)
        
        self.fisica_pedra=arcade.PhysicsEnginePlatformer(self.jogador_sprite,
                                           self.lista_pedra)
        
    def pan_camera_to_user(self, panning_fraction: float = 1.0):
        if self.jogador_sprite.center_x < 13500:
            screen_center_x = self.jogador_sprite.center_x - (self.window.width / 2)

            if screen_center_x < 0:
                screen_center_x = 0
    
            user_centered = screen_center_x, 0

            self.camera.move_to(user_centered, panning_fraction)

    def on_resize(self, width, height):
        super().on_resize(width, height)
        self.camera.resize(width, height)
        self.gui_camera.resize(width, height)

    def on_draw(self):
        if not self.game_over:
            arcade.start_render()
            arcade.draw_lrwh_rectangle_textured(0, 0,
                                                1920, 1080,
                                                self.fundo)
            self.lista_cenario.draw()
            self.camera.use()
            self.lista_pedra.draw()
            self.jogador.draw()
            self.jogador_sprite.draw()
            self.gui_camera.use()
            if  self.inimigo_aparecer==True:
                self.inimigo_sprite.draw()
                
            if self.jogador_sprite.center_x > 5000:
                arcade.draw_lrwh_rectangle_textured(self.window.current_camera.position.x + self.window.width/1.7, 0,
                                            width=500, height=500,
                                            texture=self.final)
        elif self.game_over==True:
            arcade.draw_lrwh_rectangle_textured(0, 0,
                                            self.window.width, self.window.height,
                                            self.fundo_over)
    

    def on_update(self, delta_time: float):
                
        if self.game_over==False:
            self.jogador_sprite.update_animation()
            self.jogador.update()
            self.inimigo_sprite.update_animation(delta_time)
            self.inimigo_sprite.update()
            self.fisica_cenario.update()
            self.fisica_pedra.update()
            self.pan_camera_to_user(panning_fraction=0.12)

            if self.jogador_sprite.center_x > 300 and self.inimigo_aparecer==True:
                self.inimigo_sprite.change_x = self.inimigo_velocidade
        
            if self.jogador_sprite.center_x > 4500:
                self.inimigo_aparecer= False

        if self.inimigo_sprite.collides_with_sprite(self.jogador_sprite):
            self.game_over= True


    def on_key_press(self, tecla: int, modifiers: int):
        if tecla==arcade.key.A:
            self.jogador_sprite.change_x== self.velocidade

        if tecla==arcade.key.D:
            self.jogador_sprite.change_x= self.velocidade

        if tecla==arcade.key.W:
            self.jogador_sprite.change_y=10

        if tecla==arcade.key.S:
            self.jogador_sprite.change_y==self.velocidade

    def on_key_release(self, _symbol: int, _modifiers: int):
        self.jogador_sprite.change_x=0
        self.jogador_sprite.change_y=0

def main():
    window = arcade.Window(1920, 1080, "Meu Jogo")
    tela_game = TelaGame()
    window.show_view(tela_game)
    arcade.run()

if __name__ == "__main__":
    main()

