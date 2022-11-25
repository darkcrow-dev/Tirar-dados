import random

dadoDibujos = {
    1: ("┌─────────┐",
        "│         │",
        "│    ●    │",
        "│         │",
        "└─────────┘"),

    2: ("┌─────────┐",
        "│  ●      │",
        "│         │",
        "│      ●  │",
        "└─────────┘"),

    3: ("┌─────────┐",
        "│  ●      │",
        "│    ●    │",
        "│      ●  │",
        "└─────────┘"),

    4: ("┌─────────┐",
        "│  ●   ●  │",
        "│         │",
        "│  ●   ●  │",
        "└─────────┘"),

    5: ("┌─────────┐",
        "│  ●   ●  │",
        "│    ●    │",
        "│  ●   ●  │",
        "└─────────┘"),

    6: ("┌─────────┐",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "│  ●   ●  │",
        "└─────────┘")
    }

print("Bienvenido al simulador de tiro de dados")
opcionUsuario = input("Desea tirar los dados? Si/No: ")

if(opcionUsuario.lower() == "SI".lower()):
    while(True):
        dado1 = random.randint(1, 6)
        dado2 = random.randint(1, 6)

        print("\nValores de dados lanzados", "\nDado 1: ", dado1, "\nDado 2: ", dado2)
        #print("Valores de dados lanzados \nDado 1: {} \nDado 2: {}".format(dado1, dado2))
        print("\n".join(dadoDibujos[dado1]))
        print("\n".join(dadoDibujos[dado2]))
    
        opcionUsuario = input("\nDesea volver a tirar los dados? Si/No: ")
        if(opcionUsuario.lower() == "NO".lower()):
            print("SIMULADOR FINALIZADO")
            break;
        elif(opcionUsuario.lower() == "SI".lower()):
            dado1 = 0
            dado2 = 0
        else:
            print("ERROR EN LA SELECCION, SIMULADOR FINALIZADO")
            break;
elif(opcionUsuario.lower() == "NO".lower()):
    print("SIMULADOR FINALIZADO")
else:
    print("ERROR EN LA SELECCION, SIMULADOR FINALIZADO")


