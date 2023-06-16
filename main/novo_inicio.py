##Inicio do código de trabalho da equipe## Aline Tosatti, Eduardo Lubian, Rogerio **, Vinicius Herrera
#Atenção!# Este código utiliza da biblioteca kivy e precisa ser compilado no máximo até o python 3.10
from kivy.config import Config
Config.set('graphics', 'resizable', False)

from kivy.app import App 
from kivy.uix.button import Button
from kivy.core.window import Window
from kivy.uix.screenmanager import ScreenManager, Screen
from kivy.core.audio import SoundLoader

class Jogo:
    def __init__(self, **kwargs):
        self.botoes = {}
        self.turno = 0 
    
    def pinta_botoes(self, id):
        self.botoes[id].background_color = (0, 0, 1, 1)

    def criar_tabuleiro(self):
        Tabuleiro = []
        for linha in range(10):
            linha = []
            for coluna in range(10):
                 linha.append(0)
            Tabuleiro.append(linha)
        return Tabuleiro
    
    def acao_botão_p1(self, bt_id_1, bt_id_2):
        self.p1[(bt_id_1)][(bt_id_2)] = 1
        for i in range(len(self.p1)):
            for j in range(len(self.p1[i])):
                print('[%1d]'%self.p1[i][j], end ='')
            print("\n")
        bt_id_1 = str(bt_id_1)
        bt_id_2 = str(bt_id_2)
        button_id = f'{bt_id_1},{bt_id_2}'
        self.pinta_botoes(button_id)
        self.navios_restantesp1 += 1
        print(self.navios_restantesp1)
        log_atual = []
        log_atual.append(bt_id_1)
        log_atual.append(bt_id_2)
        self.log_de_jogop1.append(log_atual)

    def acao_botão_p2(self, button, bt_id_1, bt_id_2):
        button.background_color = (1, 0, 0, 1)
        print(button.id)
        self.p2[(bt_id_1)][(bt_id_2)] = 1
        for i in range(len(self.p2)):
            for j in range(len(self.p2[i])):
                print('[%1d]'%self.p2[i][j], end ='')
            print("\n")
        self.navios_restantesp2 += 1
        print(self.navios_restantesp2)
        log_atual = []
        log_atual.append(bt_id_1)
        log_atual.append(bt_id_2)
        self.log_de_jogop2.append(log_atual)

    # Começar por Aqui

    def criar_gridtabuleiro(self):
        for linha in range(len(self.p1)):
            for coluna in range(len(self.p1[linha])):
                bt = Button(
                    text=f"{linha},{coluna}",
                    size_hint=(0.2, 0.2),
                    font_size=24,
                    on_press = self.posicionar_naviosp1
                )
                bt.id = f"{linha},{coluna}"
                self.ids.gradtab1.add_widget(bt)
                self.botoes[bt.id] = bt

    def criar_gridtabuleiro_p2(self):
        for linha in range(len(self.p2)):
            for coluna in range(len(self.p2[linha])):
                bt = Button(
                    text=f"{linha},{coluna}",
                    size_hint=(0.2, 0.2),
                    font_size=24,
                    on_press = self.acao_botão_p2
                )
                bt.id = f"{linha},{coluna}"
                self.ids.gradtab2.add_widget(bt)
                self.botoes[bt.id] = bt

    def posicionar_naviosp1(self, button):
        
        print(button.id)
        tipo_id = type(button.id)
        tipo_button = type(self.p1[0][0])
        button_id = button.text
        bt_id_1 = int(button_id[0])
        bt_id_2 = int(button_id[2])

        if self.p1[bt_id_1][bt_id_2] == 1:
            print("Selecione um botão não selecionado")
            return
        
        if self.turno_posiçãop1 <= 3:
            self.acao_botão_p1(bt_id_1, bt_id_2)
            bt_id_2 += 1
            self.acao_botão_p1(bt_id_1, bt_id_2)
            self.turno_posiçãop1 +=1
            print(f"com essa jogada = {self.turno_posiçãop1}")

        if self.turno_posiçãop1 >= 4 and self.turno_posiçãop1 <= 6:
            self.acao_botão_p1(bt_id_1, bt_id_2)
            bt_id_2 += 1
            self.acao_botão_p1(bt_id_1, bt_id_2)
            bt_id_2 += 1
            self.acao_botão_p1(bt_id_1, bt_id_2)
            self.turno_posiçãop1 +=1
            print(f"com essa jogada = {self.turno_posiçãop1}")

class Gerenciador(ScreenManager):
    pass

class Menu(Screen, Jogo):
    def __init__(self, **kwargs):
        super().__init__()
    
    
        if self.ids.check.active == True:
            self.som = SoundLoader.load("The Majestic Valkyrie.wav")
    imagem_fundo = 'Fundo.jpg'
    

    ##Definição de Fontes##
    pasta_fontes = 'Marbella Army.otf'
    pass
    
class Player1(Screen, Jogo):
    def __init__(self, **kwargs):
        super().__init__()
        self.turno_posiçãop1 = 0
        self.p1 = self.criar_tabuleiro()
        self.navios_restantesp1 = 0
        self.log_de_jogop1 = []

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
        self.turno_posiçãop2 = 0
        self.p2 = self.criar_tabuleiro()
        self.navios_restantesp2 = 0
        self.log_de_jogop2 = []
        
    def Inicio(self):
        tabuleiro_de_p2 = Jogo().retorna_p2()
        for i in range(len(tabuleiro_de_p2)):
            for j in range(len(tabuleiro_de_p2[i])):
                print('[%1d]'%tabuleiro_de_p2[i][j], end ='')
            print("\n")
        self.criar_gridtabuleiro_p2()

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