##Inicio do código de trabalho da equipe## Aline Tosatti, Eduardo Lubian, Rogerio **, Vinicius Herrera
#Atenção!# Este código utiliza da biblioteca kivy e precisa ser compilado no máximo até o python 3.10
from kivy.config import Config
Config.set('graphics', 'resizable', False)

from kivy.app import App 
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.uix.gridlayout import GridLayout
from kivy.core.audio import SoundLoader

class Jogo:
    def __init__(self, **kwargs):
        self.turno = 0 
        self.tabuleiro = self.criar_tabuleiro()
        self.p1 = self.tabuleiro
        self.navios_restantesp1 = 0
        self.p2 = self.tabuleiro
        self.navios_restantesp2 = 0
        self.log_de_jogop1 = []
        self.log_de_jogop2 = []

    def retorna_p1(self):
        return self.p1
    
    def identifica_posicionamento(self, log_de_jogo):
        pass

    def criar_tabuleiro(self):
        Tabuleiro = []
        for linha in range(10):
            linha = []
            for coluna in range(10):
                 linha.append(0)
            Tabuleiro.append(linha)
        return Tabuleiro
    
    def acao_botão_p1(self, button):
        print("apertou o botão")
        button_id = button.text
        print(button_id)
        bt_id_1 = int(button_id[0])
        bt_id_2 = int(button_id[2])
        button.background_color = (0, 0, 1, 1)
        self.p1[(bt_id_1)][(bt_id_2)] = 1
        for i in range(len(self.p1)):
            for j in range(len(self.p1[i])):
                print('[%1d]'%self.p1[i][j], end ='')
            print("\n")
        self.navios_restantesp1 += 1
        print(self.navios_restantesp1)
        log_atual = []
        log_atual.append(bt_id_1)
        log_atual.append(bt_id_2)
        self.log_de_jogop1.append(log_atual)
        
    
    # Começar por Aqui

    def criar_gridtabuleiro(self):
        for linha in range(len(self.p1)):
            for coluna in range(len(self.p1[linha])):
                bt = Button(
                    text=f"{linha},{coluna}",
                    size_hint=(0.2, 0.2),
                    font_size=24,
                    on_press = self.acao_botão_p1
                )
                bt.id = f"{linha},{coluna}"
                self.ids.gradtab1.add_widget(bt)

''' def posicionar_navios(self, button):
        if self.navios_restantesp1 < 1:
            self.acao_botão_p1
        else:
            if self.navios_restantes < 8 and self.navios_restantes %2 == 0:
                button_id = button.text
                bt_id_1 = int(button_id[0])
                bt_id_2 = int(button_id[2])
                if self.log_de_jogop1[0] - (bt_id_1 - bt_id_2):'''

class Gerenciador(ScreenManager):
    pass

class Menu(Screen, Jogo):
    def __init__(self, **kwargs):
        super().__init__()
        self.som = SoundLoader.load("The Majestic Valkyrie.wav")
    imagem_fundo = 'Fundo.jpg'
    

    ##Definição de Fontes##
    pasta_fontes = 'Marbella Army.otf'
    pass
    
class Player1(Screen, Jogo):
    def __init__(self, **kwargs):
        super().__init__()

    def Inicio(self):
        tabuleiro_de_p1 = Jogo().retorna_p1()
        for i in range(len(tabuleiro_de_p1)):
            for j in range(len(tabuleiro_de_p1[i])):
                print('[%1d]'%tabuleiro_de_p1[i][j], end ='')
            print("\n")
        self.criar_gridtabuleiro()
        
        

class Player2(Screen, Jogo):
    def __init__(self, **kwargs):
        super().__init__()

class Nosso_jogoApp(App):
    def build(self):
        Window.size = (1000, 1000)
        return Gerenciador()
    
print("##Iniciando##")
Nosso_jogoApp().run()
print('##Finalizando##')






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