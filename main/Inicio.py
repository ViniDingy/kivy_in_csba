##Inicio do código de trabalho da equipe## Aline Tosatti, Eduardo Lubian, Rogerio **, Vinicius Herrera
#Atenção!# Este código utiliza da biblioteca kivy e precisa ser compilado no máximo até o python 3.10
from kivy.config import Config
Config.set('graphics', 'resizable', False)

from kivy.app import App 
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.properties import StringProperty
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout

class Jogo:
    def __init__(self, **kwargs):
        self.turno = 0 
        self.tabuleiro = self.criar_tabuleiro()
        self.p1 = self.tabuleiro
        self.navios_restantesp1 = 0
        self.p2 = self.tabuleiro
        self.navios_restantesp2 = 0

    def criar_tabuleiro(self):
        Tabuleiro = []
        for linha in range(10):
            lin = []
            for coluna in range(10):
                 lin.append(0)
            Tabuleiro.append(lin)
        return Tabuleiro
    
    # Começar por Aqui

    def criar_gridtabuleiro(self):
        for i in range(self.p1):
            for j in range(self.p1[i]):
                bt = Button(id = f'bt{i},{j}',text = f'{i},{j}')
                self.ids['gradtab1'].add_widget(bt)

class Gerenciador(ScreenManager):
    pass

class Menu(Screen, Jogo):
    def __init__(self, **kwargs):
        super().__init__()

    def Inicio(self):
        print(self.tabuleiro)
        self.criar_gridtabuleiro()

    imagem_fundo = 'Fundo.jpg'

    ##Definição de Fontes##
    pasta_fontes = 'Marbella Army.otf'
    pass
    
class Player1(Screen, Jogo):
    def __init__(self, **kwargs):
        super().__init__()

    def Inicio(self):
        print(self.tabuleiro)
        self.criar_gridtabuleiro()

class Player2(Screen, Jogo):
    def __init__(self, **kwargs):
        super().__init__()

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