import jodo_da_forca
import advinhacao

print("****************")
print("Escolha um jogo!")
print("****************")

escolha = int(input("Escolha (1) pafa advinhação e (2) para forca"))

if(escolha == 1):
    advinhacao.jogar()
elif(escolha == 2):
    jodo_da_forca.jogar()
else:
    print("Opção inválida")

print("Pronto!")