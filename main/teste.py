import random
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.button import Button
from kivy.uix.label import Label


class BatalhaNavalGame(GridLayout):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.cols = 5
        self.navios_posicionados = 0
        self.tabuleiro = []
        self.turno = 0
        self.palpites_restantes = 27
        self.criar_tabuleiro()
        self.posicionar_navios()
        self.criar_botoes()

    def criar_tabuleiro(self):
        for _ in range(5):
            linha = ["O"] * 5
            self.tabuleiro.append(linha)

    def posicionar_navios(self):
        while self.navios_posicionados < 3:
            linha = random.randint(0, 4)
            coluna = random.randint(0, 4)
            if self.tabuleiro[linha][coluna] == "O":
                self.tabuleiro[linha][coluna] = "N"
                self.navios_posicionados += 1

    def criar_botoes(self):
        for linha in range(5):
            for coluna in range(5):
                botao = Button(
                    text="",
                    size_hint=(0.2, 0.2),
                    font_size=24,
                    on_release=self.realizar_palpite,
                )
                botao.linha = linha
                botao.coluna = coluna
                self.add_widget(botao)

    def realizar_palpite(self, botao):
        if self.tabuleiro[botao.linha][botao.coluna] == "N":
            botao.text = "X"
            self.tabuleiro[botao.linha][botao.coluna] = "X"
            self.palpites_restantes -= 1
            if self.palpites_restantes == 0:
                self.exibir_mensagem("Fim do jogo!")
        else:
            botao.text = "X"
            self.palpites_restantes -= 1
            if self.palpites_restantes == 0:
                self.exibir_mensagem("Fim do jogo!")

    def exibir_mensagem(self, mensagem):
        self.clear_widgets()
        label = Label(text=mensagem, font_size=30)
        self.add_widget(label)


class BatalhaNavalApp(App):
    def build(self):
        return BatalhaNavalGame()


if __name__ == "__main__":
    BatalhaNavalApp().run()
