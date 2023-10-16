import random

RED   = "\033[1;31m" 
BOLD  = "\033[;1m"
RESET = "\033[0;0m"
GREEN = "\033[0;32m"
CYAN  = "\033[1;36m"
BLUE  = "\033[1;34m"

bonequinhos = {0: "______\n|   _o_\n|    |\n|   / \\\n|\n|", 1: "______\n|   _o_\n|    |\n|   /\n|\n|", 2: "______\n|   _o_\n|    |\n|\n|\n|\n", 3: "______\n|   _o_\n|\n|\n|\n|", 4: "______\n|    o\n|\n|\n|\n|", 5: "______\n|\n|\n|\n|\n|"}

while True:
    print(CYAN + "\nJOGO DA FORCA" + RESET)
    print("você pode digitar a palavra inteira - serão palavras ou frases - não tem acentos ou \"ç\"\n")

    vidas = 5
    wordslist = open('frases.txt').read().split("\n")
    word = (wordslist[random.randint(0, 100)]).upper()

    n = (len(word))
    hidden = []
    for i in range(n):
        if word[i] == ' ':
            hidden.append(" ")
        else:
            hidden.append("_")
    print(*hidden, sep= ' ')

    fails = []

    while "_" in hidden:

        print(bonequinhos[vidas])
        print("\n")
        letter = (input("Digite uma letra: ")).upper()

        if letter == word:
            hidden = list(letter)
            print("\n")
            print(*hidden, sep= ' ')
            break

        if letter in word:
            index = 0
            for i in word:
                if i == letter:
                    hidden[index] = letter
                index += 1
            print("\n")
            print(*hidden, sep= ' ')
            print("\n")

        elif not letter in word:
            vidas -= 1
            print(BLUE + f"\nVocê perdeu uma vida, agora você só tem {vidas}, tome cuidado!\n" + RESET)
            fails.append(letter)
            print("\n")
            print(*hidden, sep= ' ')
            print("\n")

        print("tentativas falhas:", end=" ")
        print(*fails, sep= ' - ')

        if vidas == 0:
            print(RED + "\nVOCÊ MORREU!" + RESET)
            print(bonequinhos[vidas])
            print("\n")
            break

    if vidas == 0:
        print(f"A resposta era {word}\n")
        None
    else:
        print(GREEN + "\nVOCÊ GANHOU!\n" + RESET)

    try:
        op = int(input("Você deseja continuar jogando? Digite 0 para sair, e 1 para continuar: "))
        if op == 0:
            break
        if op == 1:
            None
        if op != 0 and op != 1:
            print(RED + "RESPOSTA INVÁLIDA" + RESET + " o jogo parou\n")
            break
    except ValueError:
        print(RED + "RESPOSTA INVÁLIDA" + RESET + " o jogo parou\n")
        break