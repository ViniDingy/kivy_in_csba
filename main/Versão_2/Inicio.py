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
        self.log_jogo = []

    def pinta_botoes(self, id, cor):
        if cor == "azul":
            self.botoes[id].background_color = (0, 0, 1, 1)
        elif cor == "vermelho":
            self.botoes[id].background_color = (1, 0, 0, 1)
    
    def criar_tabuleiro(Tabuleiro_player):
        for linha in range(10):
            linha = []
            for coluna in range(10):
                 linha.append(0)
            Tabuleiro_player.append(linha)
        return Tabuleiro_player
    
    def criar_gridtabuleiro(self, Tabuleiro_player, id_kivy, navio_player, turno_posição):
        for linha in range(len(Tabuleiro_player)):
            for coluna in range(len(Tabuleiro_player[linha])):
                bt = Button(
                    text=f"{linha},{coluna}",
                    size_hint=(0.2, 0.2),
                    font_size=24,
                    on_press = self.posicionar_navios(bt, navio_player, turno_posição, Tabuleiro_player)# parte do problema "no outro codigo ele atribuia button por osmose"
                )
                bt.id = f"{linha},{coluna}"
                self.ids[f"{linha},{coluna}"] = bt
                self.ids[f"{id_kivy}"].add_widget(bt)
                self.botoes[bt.id] = bt    

    def acao_botão(self, navio_player, Tabuleiro_player, bt_id_1, bt_id_2):
        Tabuleiro_player[(bt_id_1)][(bt_id_2)] = 1
        for i in range(len(Tabuleiro_player)):
            for j in range(len(Tabuleiro_player[i])):
                print('[%1d]'%Tabuleiro_player[i][j], end ='')
            print("\n")
        bt_id_1 = str(bt_id_1)
        bt_id_2 = str(bt_id_2)
        button_id = f'{bt_id_1},{bt_id_2}'
        self.pinta_botoes(button_id, "azul")
        navio_player += 1
        print(navio_player)
        log_atual = []
        log_atual.append(bt_id_1)
        log_atual.append(bt_id_2)
        self.log_jogo.append(log_atual)

    def posicionar_navios(self, button, navio_player, turno_posição, Tabuleiro_player):
        
        print(button.id) ###### Parei aqui - como faço para tribuir "button"
        button_id = button.text
        bt_id_1 = int(button_id[0])
        bt_id_2 = int(button_id[2])

        if Tabuleiro_player[bt_id_1][bt_id_2] == 1:
            print("Selecione um botão não selecionado")
            return
        
        elif turno_posição >= 0 and turno_posição <= 3:
            
            for i in range(2):
                self.acao_botão(navio_player, Tabuleiro_player, bt_id_1, bt_id_2)
                bt_id_2 += 1
            turno_posição +=1
            print(f"com essa jogada = {turno_posição}")

        elif turno_posição >= 4 and turno_posição <= 6:
            
            for i in range(3):
                self.acao_botão(navio_player, Tabuleiro_player, bt_id_1, bt_id_2)
                bt_id_1 += 1
            turno_posição +=1
            print(f"com essa jogada = {turno_posição}")
        
        elif turno_posição >= 7 and turno_posição <= 8:
            
            for i in range(4):
                self.acao_botão(navio_player, Tabuleiro_player, bt_id_1, bt_id_2)
                bt_id_2 += 1
            turno_posição +=1
            print(f"com essa jogada = {turno_posição}")

        elif turno_posição >= 9:
            
            for i in range(5):
                self.acao_botão(navio_player, Tabuleiro_player, bt_id_1, bt_id_2)
                bt_id_2 += 1
            turno_posição +=1
            print(f"com essa jogada = {turno_posição}")

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
        self.p1 = []
        self.navios_restantesp1 = 0
        self.log_de_jogop1 = []
        self.rotação = 0

    def Inicio(self):
        Jogo.criar_tabuleiro(self.p1)
        for i in range(len(self.p1)):
            for j in range(len(self.p1[i])):
                print('[%1d]'%self.p1[i][j], end ='')
            print("\n")
        self.criar_gridtabuleiro(self.p1, 'gradtab1', self.navios_restantesp1, self.turno_posiçãop1)
        
class Player2(Screen, Jogo):
    def __init__(self, **kwargs):
        super().__init__()

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