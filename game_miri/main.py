import arcade
from telas.tela_menu import TelaMenu
from telas.tela_game import TelaGame

width_j=1920
height_j=1080
title_j="Gravity Jumper"

class main(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=True)

    def on_resize(self, width, height):
        super().on_resize(width, height)

    def on_draw(self):
        self.clear()
#personagem...abs


def Janela():
   main=arcade.Window(width_j,height_j, title_j, resizable=True)
   t1=TelaMenu()
   main.show_view(t1)
   arcade.run()


if __name__=="__main__":
    Janela()




