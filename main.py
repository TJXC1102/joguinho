import math

def posicao():
    print("        ───▄▀▀▀▄▄▄▄▄▄▄▀▀▀▄───")
    print("        ───█▒▒░░░░░░░░░▒▒█───")
    print("        ────█░░█░░░░░█░░█────")
    print("        ─▄▄──█░░░▀█▀░░░█──▄▄─")
    print("        █░░█─▀▄░░░░░░░▄▀─█░░█")
    print("        █▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀▀█")
    print("        █  HOTEL DE ANIMAIS  █")
    print("        █      POSIÇÕES      █")
    lista = [1, 2, 3, 4, 5, 6, 7, 8]
    print("        █   ", lista[0:4], "   █")
    print("        █   ", lista[4:8], "   █")
    print("        █▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄▄█\n")

#Mostrar os quartos disponíveis
def mostrar_quartos():
    for fileira in quartos:
        print(str(fileira))

#função para mensagem de vitória
def vitoria():
    print("Você ganhou!")

#função que termina o programa se o usuário perder
def fim_do_jogo():
    print("Você perdeu!")
    quit()
#Estabelece o intervalo das posições a serem usadas - variável animal e quarto que será ocupado – input

def alocar_animal(animal, nome):
   while True:
      try:
         posicao = int(input("Em qual posição quer hospedar o " + animal + "?"))
 #verifica se o input está no intervalo determinado
         if posicao > 8 or posicao < 1:
            print("Posição inválida.")
            continue
         elif quartos[math.floor(posicao / 5)][(posicao - 1) % 4]!= "_":
            print("Quarto indisponível.")
            continue
         else:
            quartos[math.floor(posicao / 5)][(posicao - 1) % 4] = nome
            break
      except ValueError:
         print("Número inválido.")
         continue

# Verifica se o usuário perdeu.
# retorna True se o usuário perdeu.
# retorna False se o usuário não perdeu continuando o programa.
def verifica_derrota():
   for fileira in quartos:
      for posicao in range(len(fileira)):
         esquerda = fileira[posicao - 1] if posicao - 1 > -1 else None
         animal = fileira[posicao]
         direita = fileira[posicao + 1] if posicao + 1 < 4 else None
         if animal == "R":
            if esquerda == "G" or direita == "G":
               return True
         elif animal == "C":
            if esquerda == "O" or direita == "O":
               return True
         elif animal == "G":
            if esquerda == "C" or direita == "C":
               return True
         elif animal == "Q":
            if esquerda == "R" or direita == "R":
               return True

#Dicionário relacionando o nome do animal com a letra correspondente.
hospede =dict(G="GATO", C="CÃO", R="RATO", O="OSSO", Q="QUEIJO")

posicao()

#Regras
print("        ***Regras do Hotel***\n")
print("O rato não pode ficar ao lado do gato.")
print("O cão não pode ficar ao lado do osso.")
print("O gato não pode ficar ao lado do cão.")
print("O queijo não pode ficar ao lado do rato")


print("\n    Considere a seguinte relação: \n", hospede)

#Fases do jogo
print("\nBem vindos a fase 1!\n")
print("Na Fase 1, o jogador deve alocar o RATO e o GATO na seguinte matriz que representa os quartos:")
quartos = [["*", "*", "_", "G"], ["R", "_", "*", "*"]]
mostrar_quartos()
alocar_animal("RATO", "R")
alocar_animal("GATO", "G")
if verifica_derrota():
   fim_do_jogo()

print("\nBem vindos a fase 2!\n")
print("Na Fase 2, o jogador deve alocar 2 cães e 1 osso nos seguintes quar-tos:")
quartos = [["_", "*", "*", "*"], ["*", "C", "_", "_"]]
mostrar_quartos()
alocar_animal("CÃO", "C")
alocar_animal("CÃO", "C")
alocar_animal("OSSO", "O")
if verifica_derrota():
   fim_do_jogo()

print("\nBem vindos a fase 3!\n")
print("Na Fase 3, o jogador deve alocar um GATO, um RATO e um OSSO nos se-guintes quartos:")
quartos = [["_", "*", "*", "*"], ["_", "G", "_", "*"]]
mostrar_quartos()
alocar_animal("GATO", "G")
alocar_animal("RATO", "R")
alocar_animal("OSSO", "O")
if verifica_derrota():
   fim_do_jogo()

print("\nBem vindos a fase 4!\n")
print("Na Fase 4, o jogador deve alocar 2 QUEIJOS e 1 OSSO nos seguintes quartos:")
quartos = [["_", "_", "_", "*"], ["*", "R", "*", "*"]]
mostrar_quartos()
alocar_animal("QUEIJO", "Q")
alocar_animal("QUEIJO", "Q")
alocar_animal("OSSO", "O")
if verifica_derrota():
   fim_do_jogo()

vitoria()
