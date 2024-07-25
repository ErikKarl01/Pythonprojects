    
def jogar(): 
    import random

    print("*"*35)
    print("Bem vondo ao jodo de adivinhação!")
    print("*"*35)
    print("\n")

    numero_secreto = random.randrange(1, 101)
    pontos_perdidos = 0
    pontos_total = 1000
    porcentagem_aproximacao = 0.0

    while(True):
        escolha_proseguir = int(input("Deseja proseguir com o jogo de advinhação? (1) Sim (0) Não: \n")) 
        
        if(escolha_proseguir == 1):
            dificuldade = int(input("Escolha um nível de dificuldade: (1) Fácil (2) Médio (3) Difícil: \n"))
        elif(escolha_proseguir == 0):
            print("Finalizando!")
            exit()
        else:
            print("Escolha inválica, digite 1 ou 0: \n")
            continue

        if(dificuldade == 1):
            tentativas = 32
            break
        elif(dificuldade == 2):
            tentativas = 16
            break
        elif(dificuldade == 3):
            tentativas = 8
            break
        else:
            print("Escolha inválida!")
            print("Escolha 1, 2 ou 3 apenas!")
            continue



    for rodada in range(1, tentativas + 1):
        if(pontos_total <= 0):
            break
        print("Você perde uma certa quantidade de pontos a medida que sua resposta se distância do numero secreto, cuidado com suas respostas!")
        print("\nTentativa {} de {}".format(rodada, tentativas))
        chute = int(input("Digite seu número entre 1 e 100: "))  # Por padrão o input prioriza string; 
        print("Você escolheu: ", chute)
        
        if(chute > 100 or chute < 1):
            print("Digite um número entre 1 e 100 apenas!")
            continue
        
        acertou    = numero_secreto == chute
        maior      = numero_secreto < chute
        menor      = numero_secreto > chute 
        
        if(acertou):
            print("Você acertou!")
            break
        else:
            print("Você errou!")
            porcentagem_aproximacao = (abs(numero_secreto-chute))*100/numero_secreto
            print(porcentagem_aproximacao)
            if(porcentagem_aproximacao<=5):
                print("Você está quase acdertando!\n")
                pontos_perdidos = 10
            elif(porcentagem_aproximacao<= 25):
                print("Está muito proximo!\n")
                pontos_perdidos = 100
            elif(porcentagem_aproximacao<=50):
                print("Está a meio caminho da resposta!\n")
                pontos_perdidos = 150
            else:
                print("Está longe da resposta!\n")
                pontos_perdidos = 250
            print("Porcentágem da distância: {:.2f}%".format(porcentagem_aproximacao))
            pontos_total -= pontos_perdidos

    if(pontos_total > 0):
        print("\nTentativas esgotadas")
    else:
        print("\nVocê perdeu todos os seus pontos!")
        
if(__name__ == "__main__"):
    jogar()
        