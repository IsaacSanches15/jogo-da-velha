import random

rodando_1 = False
rodando_2 = False
simbolo1 = "X"
simbolo2 = "O"
casas = [
    " ",
    " ",
    " ",  # casas do tabuleiro
    " ",
    " ",
    " ",
    " ",
    " ",
    " ",
]


#
def tabuleiro():  # tabuleiro
    print(casas[0], "|", casas[1], "|", casas[2])
    print("__________")
    print(casas[3], "|", casas[4], "|", casas[5])
    print("__________")
    print(casas[6], "|", casas[7], "|", casas[8])
    print("")


#
def teste_vitoria_1():  # condição de vitoria jogador um
    global casas
    global rodando
    global perguntar
    global rodando_1
    global rodando_2
    global vitoria
    perguntar = "a"
    if (
        casas[0] == simbolo1
        and casas[1] == simbolo1
        and casas[2] == simbolo1
        or casas[3] == simbolo1
        and casas[4] == simbolo1
        and casas[5] == simbolo1
        or casas[6] == simbolo1
        and casas[7] == simbolo1
        and casas[8] == simbolo1
        or casas[0] == simbolo1
        and casas[3] == simbolo1
        and casas[6] == simbolo1
        or casas[1] == simbolo1
        and casas[4] == simbolo1
        and casas[7] == simbolo1
        or casas[2] == simbolo1
        and casas[5] == simbolo1
        and casas[8] == simbolo1
        or casas[0] == simbolo1
        and casas[4] == simbolo1
        and casas[8] == simbolo1
        or casas[2] == simbolo1
        and casas[4] == simbolo1
        and casas[6] == simbolo1
        or casas[0] == simbolo1
        and casas[1] == simbolo1
        and casas[2] == simbolo1
        or casas[3] == simbolo1
        and casas[4] == simbolo1
        and casas[5] == simbolo1
        or casas[6] == simbolo1
        and casas[7] == simbolo1
        and casas[8] == simbolo1
        or casas[0] == simbolo1
        and casas[3] == simbolo1
        and casas[6] == simbolo1
        or casas[1] == simbolo1
        and casas[4] == simbolo1
        and casas[7] == simbolo1
        or casas[2] == simbolo1
        and casas[5] == simbolo1
        and casas[8] == simbolo1
        or casas[0] == simbolo1
        and casas[4] == simbolo1
        and casas[8] == simbolo1
        or casas[2] == simbolo1
        and casas[4] == simbolo1
        and casas[6] == simbolo1
    ):
        print("Jogador 1 Ganhou a Partida!!")
        print("")
        while perguntar == "a":
            perguntar = str(input("Deseja Jogar Novamente? (s/n) "))
            if perguntar == "s":
                casas = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
                break
            elif perguntar == "n":
                print("Obrigado por Jogar!!")
                rodando_1 = False
                rodando_2 = False
                vitoria = 1
                break
            else:
                print("Responda Novamente a Pergunta.")
    elif (
        casas[0] != " "
        and casas[1] != " "
        and casas[2] != " "
        and casas[3] != " "
        and casas[4] != " "
        and casas[5] != " "
        and casas[6] != " "
        and casas[7] != " "
        and casas[8] != " "
    ):
        print("Empate!!")
        print()
        while perguntar == "a":
            perguntar = str(input("Deseja Jogar Novamente? (s/n) "))
            if perguntar == "s":
                casas = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
                break
            elif perguntar == "n":
                print("Obrigado por Jogar!!")
                rodando_1 = False
                rodando_2 = False
                vitoria = 2
                break
            else:
                print("Responda Novamente a Pergunta.")


#
def teste_vitoria_2():  # condição de vitoria jogador 2
    global casas
    global rodando
    global perguntar
    global rodando_1
    global rodando_2
    global vitoria
    perguntar = "a"
    if (
        casas[0] == simbolo2
        and casas[1] == simbolo2
        and casas[2] == simbolo2
        or casas[3] == simbolo2
        and casas[4] == simbolo2
        and casas[5] == simbolo2
        or casas[6] == simbolo2
        and casas[7] == simbolo2
        and casas[8] == simbolo2
        or casas[0] == simbolo2
        and casas[3] == simbolo2
        and casas[6] == simbolo2
        or casas[1] == simbolo2
        and casas[4] == simbolo2
        and casas[7] == simbolo2
        or casas[2] == simbolo2
        and casas[5] == simbolo2
        and casas[8] == simbolo2
        or casas[0] == simbolo2
        and casas[4] == simbolo2
        and casas[8] == simbolo2
        or casas[2] == simbolo2
        and casas[4] == simbolo2
        and casas[6] == simbolo2
        or casas[0] == simbolo2
        and casas[1] == simbolo2
        and casas[2] == simbolo2
        or casas[3] == simbolo2
        and casas[4] == simbolo2
        and casas[5] == simbolo2
        or casas[6] == simbolo2
        and casas[7] == simbolo2
        and casas[8] == simbolo2
        or casas[0] == simbolo2
        and casas[3] == simbolo2
        and casas[6] == simbolo2
        or casas[1] == simbolo2
        and casas[4] == simbolo2
        and casas[7] == simbolo2
        or casas[2] == simbolo2
        and casas[5] == simbolo2
        and casas[8] == simbolo2
        or casas[0] == simbolo2
        and casas[4] == simbolo2
        and casas[8] == simbolo2
        or casas[2] == simbolo2
        and casas[4] == simbolo2
        and casas[6] == simbolo2
    ):
        print("Jogador 2 ganhou a Partida!!")
        print("")
        while perguntar == "a":
            perguntar = str(input("Deseja Jogar Novamente? (s/n) "))
            if perguntar == "s":
                casas = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
                break
            elif perguntar == "n":
                print("Obrigado por Jogar")
                rodando_1 = False
                rodando_2 = False
                vitoria = 2
                break
            else:
                print("Responda Novamente a Pergunta")
    elif (
        casas[0] != " "
        and casas[1] != " "
        and casas[2] != " "
        and casas[3] != " "
        and casas[4] != " "
        and casas[5] != " "
        and casas[6] != " "
        and casas[7] != " "
        and casas[8] != " "
    ):
        print("Empate!!")
        print()
        while perguntar == "a":
            perguntar = str(input("Deseja Jogar Novamente? (s/n) "))
            if perguntar == "s":
                casas = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
                break
            elif perguntar == "n":
                print("Obrigado por Jogar!!")
                rodando_1 = False
                rodando_2 = False
                vitoria = 2
                break
            else:
                print("Responda Novamente a Pergunta.")


#
def jogada_jogador_1():  # faz a jogada e confere se a joga do jogador 1 é viavel
    global casas
    global simbolo1
    global simbolo2
    teste_1 = True
    print("")
    jogada1 = int(input("Jogador 1, Digite a casa que deseja jogar. (1 ao 9) ")) - 1
    print("")
    while teste_1:
        if casas[jogada1] == " " and casas[jogada1] != simbolo2:
            casas[jogada1] = simbolo1
            break
        elif casas[jogada1] == simbolo2:
            print("Local ja ocupado.")
            jogada1 = int(input("Refaça sua jogada! ")) - 1
            casas[jogada1] = simbolo1
            break
        elif casas[jogada1] == simbolo1:
            print("Local ja ocupado.")
            jogada1 = int(input("Refaça sua jogada! ")) - 1
            casas[jogada1] = simbolo1
            break
        else:
            print("Erro")


#
def jogada_jogador_2():  # faz a jogada e confere se a joga do jogador 2 é viavel
    global casas
    global simbolo1
    global simbolo2
    teste_2 = True
    print("")
    jogada2 = int(input("Jogador 2, Digite a casa que deseja jogar. (1 ao 9) ")) - 1
    print("")
    while teste_2:
        if casas[jogada2] == " " and casas[jogada2] != simbolo1:
            casas[jogada2] = simbolo2
            break
        elif casas[jogada2] == simbolo1:
            print("Local ja ocupado.")
            jogada2 = int(input("Refaça sua jogada! ")) - 1
            casas[jogada2] = simbolo2

            break
        elif casas[jogada2] == simbolo2:
            print("Local ja ocupado.")
            jogada2 = int(input("Refaça sua jogada! ")) - 1
            casas[jogada2] = simbolo2
            break
        else:
            print("Erro!!")


#
def jogada_maquina():  # faz a jogada da maquina e verifica se é possivel usar aquela casa
    global casas
    global simbolo1
    global simbolo2
    global rodando_1
    global rodando_2
    global perguntar
    global vitoria
    print("Vez da maquina.")
    print("")
    if casas[4] == " " and casas[4] != simbolo2:
        casas[4] = simbolo2
    elif casas[0] == " " and casas[0] != simbolo2:
        casas[0] = simbolo2
    elif casas[2] == " " and casas[2] != simbolo2:
        casas[2] = simbolo2
    elif casas[6] == " " and casas[6] != simbolo2:
        casas[6] = simbolo2
    elif casas[8] == " " and casas[8] != simbolo2:
        casas[8] = simbolo2
    elif casas[1] == " " and casas[1] != simbolo2:
        casas[1] = simbolo2
    elif casas[3] == " " and casas[3] != simbolo2:
        casas[3] = simbolo2
    elif casas[5] == " " and casas[5] != simbolo2:
        casas[5] = simbolo2
    elif casas[7] == " " and casas[7] != simbolo2:
        casas[7] = simbolo2
    else:
        print("Sem movimentos Possiveis!")


#
vitoria = 3
quem_começa = random.randint(1, 2)
pergunta_modo_de_jogo = True
while pergunta_modo_de_jogo:
    modo_de_jogo = input("Deseja jogar sozinho ou com um amigo? (sozinho/amigo) ")
    print("")
    if modo_de_jogo == "sozinho":
        rodando_1 = True
        rodando_2 = False
        pergunta_modo_de_jogo = False
        if quem_começa == 2:
            tabuleiro()
            jogada_maquina()
    elif modo_de_jogo == "amigo":
        rodando_1 = False
        rodando_2 = True
        pergunta_modo_de_jogo = False
        if quem_começa == 2:
            tabuleiro()
            jogada_jogador_2()
while rodando_1 == True:
    tabuleiro()
    teste_vitoria_2()
    if vitoria == 2 or vitoria == 1:
        break
    jogada_jogador_1()
    tabuleiro()
    teste_vitoria_1()
    if vitoria == 1 or vitoria == 2:
        break
    jogada_maquina()

while rodando_2 == True:
    tabuleiro()
    teste_vitoria_2()
    if vitoria == 2 or vitoria == 1:
        break
    jogada_jogador_1()
    tabuleiro()
    teste_vitoria_1()
    if vitoria == 1 or vitoria == 2:
        break
    jogada_jogador_2()
