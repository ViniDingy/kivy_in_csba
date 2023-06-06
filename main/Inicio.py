##Inicio do código de trabalho da equipe## Aline Tosatti, Eduardo Lubian, Rogerio **, Vinicius Herrera
#Atenção!# Este código utiliza da biblioteca kivy e precisa ser compilado no máximo até o python 3.10
from kivy.config import Config
Config.set('graphics', 'resizable', False)

from kivy.app import App 
from kivy.uix.boxlayout import BoxLayout
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen

class Gerenciador(ScreenManager):
    pass

class Menu(Screen):
    imagem_fundo = 'Fundo.jpg'

    ##Definição de Fontes##
    pasta_fontes = 'Marbella Army.otf'
    pass

class Player1(Screen):
    '''def Gerador_de_Matriz(self):
'''
    pass

class Player2(Screen):
    pass

class Nosso_jogoApp(App):
    def build(self):
        Window.size = (1000, 1000)
        return Gerenciador()
    
    
Nosso_jogoApp().run()
print('olá')






"""                   /^--^\     /^--^\     /^--^\
                      \____/     \____/     \____/
                     /      \   /      \   /      \
                    |        | |        | |        |
                     \__  __/   \__  __/   \__  __/
|^|^|^|^|^|^|^|^|^|^|^|^\ \^|^|^|^/ /^|^|^|^|^\ \^|^|^|^|^|^|^|^|^|^|^|^|
| | | | | | | | | | | | |\ \| | |/ /| | | | | | \ \ | | | | | | | | | | |
########################/ /######\ \###########/ /#######################
| | | | | | | | | | | | \/| | | | \/| | | | | |\/ | | | | | | | | | | | |
|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|_|
"""