#Gera um Nick aléatorio para o jogador
import random
import string


def randomNick():
    return ''.join(random.choice(string.ascii_uppercase + string.digits) for _ in range(7))

#cria um menu para o jogador
def menu():
    print("1 - Jogar")
    print("2 - Sair")
    opcao = int(input("Digite a opção desejada: "))
    return opcao

#cria um loop para o menu
while True:
    opcao = menu()
    if opcao == 1:
        print(" Gerar Nick")
        print(randomNick())

    elif opcao == 2:
        print("Sair")
        break
    else:
        print("Opção inválida")

