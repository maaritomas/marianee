import math

class JogoDaVelha:
    def __init__(self):
        self.tabuleiro = [' '] * 9
        self.jogador_atual = 'X'
        self.vencedor = None

    def imprimir_tabuleiro(self):
        for i in range(0, 9, 3):
            print(' | '.join(self.tabuleiro[i:i+3]))
            if i < 6:
                print('-' * 9)

    def obter_casas_vazias(self):
        return [i for i, val in enumerate(self.tabuleiro) if val == ' ']

    def realizar_jogada(self, jogada):
        self.tabuleiro[jogada] = self.jogador_atual
        self.jogador_atual = 'O' if self.jogador_atual == 'X' else 'X'

    def desfazer_jogada(self, jogada):
        self.tabuleiro[jogada] = ' '
        self.jogador_atual = 'O' if self.jogador_atual == 'X' else 'X'

    def verificar_vencedor(self):
        combinacoes_vitoria = [
            [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
            [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
            [0, 4, 8], [2, 4, 6]              # Diagonais
        ]
        for combo in combinacoes_vitoria:
            if self.tabuleiro[combo[0]] == self.tabuleiro[combo[1]] == self.tabuleiro[combo[2]] != ' ':
                self.vencedor = self.tabuleiro[combo[0]]
                return self.vencedor
        if ' ' not in self.tabuleiro:
            self.vencedor = 'Empate'
        return self.vencedor

    def minimax(self, profundidade, alfa, beta, jogador_maximizando):
        vencedor = self.verificar_vencedor()
        if vencedor is not None:
            if vencedor == 'X':
                return -10 + profundidade, None
            elif vencedor == 'O':
                return 10 - profundidade, None
            else:
                return 0, None

        if jogador_maximizando:
            melhor_valor = -math.inf
            melhor_jogada = None
            for jogada in self.obter_casas_vazias():
                self.realizar_jogada(jogada)
                valor, _ = self.minimax(profundidade + 1, alfa, beta, False)
                self.desfazer_jogada(jogada)
                if valor > melhor_valor:
                    melhor_valor = valor
                    melhor_jogada = jogada
                alfa = max(alfa, valor)
                if beta <= alfa:
                    break
            return melhor_valor, melhor_jogada
        else:
            melhor_valor = math.inf
            melhor_jogada = None
            for jogada in self.obter_casas_vazias():
                self.realizar_jogada(jogada)
                valor, _ = self.minimax(profundidade + 1, alfa, beta, True)
                self.desfazer_jogada(jogada)
                if valor < melhor_valor:
                    melhor_valor = valor
                    melhor_jogada = jogada
                beta = min(beta, valor)
                if beta <= alfa:
                    break
            return melhor_valor, melhor_jogada

    def jogar(self):
        while not self.verificar_vencedor():
            self.imprimir_tabuleiro()
            if self.jogador_atual == 'X':
                jogada = int(input("Escolha sua jogada (0-8): "))
            else:
                _, jogada = self.minimax(0, -math.inf, math.inf, True)
            self.realizar_jogada(jogada)
            print("\n" + self.jogador_atual + " realizou a jogada.\n")
        self.imprimir_tabuleiro()
        vencedor = self.verificar_vencedor()
        if vencedor == 'Empate':
            print("Empate!")
        else:
            print("O vencedor é:", vencedor)

if __name__ == "__main__":
    jogo = JogoDaVelha()
    jogo.jogar()
