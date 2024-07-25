import random

def imprime_inicio():
    print("***************")
    print("Jogo da forca!!")
    print("***************")


def cria_palavra_secreta():
    arquivo = open("palavras.txt", "r")
    palavras = []
    
    for linha in arquivo:                     
        linha = linha.strip()
        palavras.append(linha)
        
    arquivo.close()
    indice = random.randrange(0, len(palavras))
    return palavras[indice].lower()
    

def imprime_letras_descobertas(palavra_secreta, letra_descoberta):
    for l in palavra_secreta:
            if(l in letra_descoberta):
                print(l, end=" ")
            else:
                print("_", end=" ")


def imprime_boneco_e_vidas(vidas):
    print(f"Você perdeu uma vida: {vidas} vidas restrantes")
    if vidas == 4:
        print("O")
    elif vidas == 3:
        print("O")
        print("|")
    elif vidas == 2:
        print("O")
        print("/|\\")
    elif vidas == 1:
        print("O")
        print("/|\\")
        print("\\")
    elif vidas == 0:
        print("O")
        print("/|\\")
        print("/\\")
                

def jogar():
    imprime_inicio()
    
    ganhou =  False;
    vidas = 5
    
    palavra_secreta = cria_palavra_secreta()        
    
    letra_descoberta = []
    numero_letras_descobertas = 0
    
    
    while(not(ganhou)):
        letra = input("\nEscolha uma letra!\n").lower()
        
        if not letra.isalpha() or len(letra) != 1:
            print("Digite somente letras!")
            continue
        
        if(letra not in palavra_secreta):
            vidas -= 1
            imprime_boneco_e_vidas(vidas)
        else:
            letra_descoberta.append(letra)
            for l in palavra_secreta:
                if(l == letra):
                    numero_letras_descobertas += 1
    
        
        if(vidas == 0):
            print("Suas vidas acabaram, você perdeu!")
            break
        else:
            if(numero_letras_descobertas == len(palavra_secreta)):
                print("Você acertou!")
                ganhou = True
        imprime_letras_descobertas(palavra_secreta, letra_descoberta)
            
        
            


    print("Fim de jogo!")
    
if(__name__ == "__main__"):
    jogar()