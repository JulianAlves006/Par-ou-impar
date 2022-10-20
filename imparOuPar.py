from random import randint
def par():
    global p, g
    print("Vamos de par então!!")
    n = int(input("Digite um numero: "))
    bot = randint(0, 100)
    resultado = n + bot
    print(f"O bot digitou {bot}")
    print(f"A soma deu {resultado}")
    if resultado%2 == 1:
        print("Você perdeu!")
        p += 1
    else:
        print("Você ganhou!!")
        g += 1

def impar():
    global p, g
    print("Vamos de impar então!!")
    n = int(input("Digite um numero: "))
    bot = randint(0, 100)
    resultado = n + bot
    print(f"O bot digitou {bot}")
    print(f"A soma deu {resultado}")
    if resultado%2 == 0:
        print("Você perdeu!")
        p += 1
    else:
        print("Você ganhou!!")
        g += 1

def fim():
    global g, p
    if g > 1 and p > 1:     
        print(f"Você ganhou {g} vezes e perdeu {p} vezes")
    elif g == 1 and p > 1:
        print(f"Você ganhou {g} vez e perdeu {p} vezes")
    elif g > 1 and p == 1:
        print(f"Você ganhou {g} vezes e perdeu {p} vez")
    elif g == 1 and p == 1:
        print(f"Você ganhou {g} vez e perdeu {p} vez")
    elif g == 0 and p > 1:
        print(f"Você não ganhou nenhuma vez e perdeu {p} vezes")
    elif g == 0 and p == 1:
        print(f"Você não ganhou nenhuma vez e perdeu {p} vez")
    elif p == 0 and g > 1:
        print(f"Você ganhou {g} vezes e não perdeu nenhuma vez")
    elif p == 0 and g == 1:
        print(f"Você ganhou {g} vez e não perdeu nenhuma vez")
    print("Adeus!! (:")



print("Jogo do par ou impar!!")
g = 0
p = 0
while True:
    try:
        n = int(input("Você gostaria de jogar? [1]Sim; [2] Não: "))
        if n == 1:
            print("Beleza vamos jogar")
            n = int(input("Você deseja ser par[1] ou impar[2]?: "))
            if n == 1:
                par()
            elif n == 2:
                impar()
            else:
                print("Valor invalido!")
        elif n == 2:
            break
        else:
            print("Valor invalido!")
    except:
        print("Você digitou um valor invalido!")
fim()

