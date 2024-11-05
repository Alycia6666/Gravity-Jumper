import arcade
import os
from telas.tela_game import TelaGame

class TelaMenu(arcade.View):
    botao_start=None

    def __init__(self):
        super().__init__()

        # Verificar se o arquivo existe antes de tentar carregá-lo
       
        self.botao_start=arcade.Sprite("./assets/botao2.png",
                                       center_x = self.window.width/2,
                                       center_y = self.window.height/2,
                                       )

    def on_draw(self):
        arcade.start_render()
        if self.botao_start:
            self.botao_start.draw()

    def on_mouse_press(self, x: int, y: int, button: int, modifiers: int):
        if self.botao_start and self.botao_start.collides_with_point( (x,y) ):
            t2=TelaGame()
            self.window.show_view(t2)