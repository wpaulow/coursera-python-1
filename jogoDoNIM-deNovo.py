def partida():
    
    n = 0
    m = 0
    vezComp = False
    pecas = 0

    while n < 1:
        n = int(input("Quantas peças? "))
        print()

    while n <= m or m <= 0:
        m = int(input("Limite de peças por jogada? "))
        print()
        
    if n % (m+1) == 0:
        print("Você começa!\n")
        pecas = usuario_escolhe_jogada(n, m)
        n -= pecas
        vezComp = True
    else:
        print("Computador começa!\n")
        pecas = computador_escolhe_jogada(n, m)
        n -= pecas

    while n > 0:
        if n == 1:
            print("Agora resta apenas uma peça no tabuleiro.\n")
        else:
            print("Agora restam %d peças no tabuleiro.\n" % n)
        if vezComp:
            pecas = computador_escolhe_jogada(n, m)
            vezComp = False
            n -= pecas
            if pecas == 1:
                print("O computador tirou uma peça.\n")
            else:
                print("O computador tirou %d peças.\n" % pecas)
        else:
            pecas = usuario_escolhe_jogada(n, m)
            vezComp = True
            n -= pecas
            if pecas == 1:
                print("Você tirou uma peça.\n")
            else:
                print("Você tirou %d peças.\n" % pecas)

    print("Fim do jogo! O computador ganhou!")



    
def usuario_escolhe_jogada(n, m):

    pecas = 0

    while pecas < 1 or pecas > m:
        try:
            pecas = int(input("Quantas peças você vai tirar? "))
        except:
            print("Oops! Jogada inválida! Tente de novo.\n")
            continue
        if pecas < 1 or pecas > m:
            print("Oops! Jogada inválida! Tente de novo.\n")

    return pecas 


    
def computador_escolhe_jogada(n, m):

    pecas = 1

    while pecas < m:
        if (n - pecas) % (m + 1) == 0:
            return pecas
        pecas += 1
    
    return m



def campeonato():

    print("Você escolheu um campeonato!\n")
    print("**** Rodada 1 ****\n")
    partida()
    print("**** Rodada 2 ****\n")
    partida()
    print("**** Rodada 3 ****\n")
    partida()
    print("\n**** Final do campeonato! ****\n")
    print("Placar: Você 0 X 3 Computador")


def main():

    print("Bem-vindo ao jogo do NIM! Escolha:\n")

    escolha = 0

    while escolha < 1 or escolha > 2:
        escolha = int(input("1 - para jogar uma partida isolada\n"
                            "2 - para jogar um campeonato "))

    if escolha == 1:
        print("Você escolheu uma partida!\n")
        partida()
    else:
        print("Você escolheu um campeonato!\n")
        campeonato()


main()









