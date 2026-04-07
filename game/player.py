from game.classes import Guerreiro, Mago, Ladino

# Ficha de Status

# Identidade
Nome_do_Personagem = input("Digite seu nome: ")
Classe = input("Digite sua classe: ")

# Status de combate
pontos = 6
Ficha_Valida = False
Hp = 0
Defesa = 0
Ataque = 0

while not Ficha_Valida:
    try:
        Vigor = int(input("Digite os pontos que voce quer colocar em vigor (0 a 3): "))
        Fisico = int(input("Digite os pontos que voce quer colocar em fisico (0 a 3): "))
        Estilo = int(input("Digite os pontos que voce quer colocar em estilo (0 a 3): "))
        Instinto = int(input("Digite os pontos que voce quer colocar em instinto (0 a 3): "))
    except ValueError:
        print("Digite apenas numeros inteiros.")
        continue

    Total = Vigor + Fisico + Estilo + Instinto

    # Verificacao para ver se distribuicoes de status estao correta.
    if Vigor > 3 or Fisico > 3 or Estilo > 3 or Instinto > 3:
        print("Um dos atributos passou da quantidade maxima de pontos.")
    elif Total > pontos:
        print("Voce gastou mais do que o total de pontos permitido.")
    elif Total < pontos:
        print("Voce ainda nao gastou todos os seus pontos.")
    elif Vigor < 0 or Fisico < 0 or Estilo < 0 or Instinto < 0:
        print("Um dos atributos ficou abaixo do minimo necessario.")
    else:
        Ficha_Valida = True
        print("=" * 30)
        print("Ficha criada com sucesso.".center(30))
        print("=" * 30)
        print(f"Nome: {Nome_do_Personagem}")
        print(f"Classe: {Classe}")
        print(f"Vigor: {Vigor}")
        print(f"Fisico: {Fisico}")
        print(f"Estilo: {Estilo}")
        print(f"Instinto: {Instinto}")
        print("=" * 30)

        # Calculo de vida
        if Classe.lower() == "guerreiro":
            Hp = 10 + (Vigor * 5) + Guerreiro["Bonus_de_Hp_G"]
        elif Classe.lower() == "mago":
            Hp = 10 + (Vigor * 5) + Mago["Bonus_de_Hp_M"]
        elif Classe.lower() == "ladino":
            Hp = 10 + (Vigor * 5) + Ladino["Bonus_de_Hp_L"]
        else:
            Hp = 10 + (Vigor * 5)

        # Calculo de defesa
        if Classe.lower() == "guerreiro":
            Defesa = 3 + Fisico + Guerreiro["Bonus_de_Defesa_G"]
        elif Classe.lower() == "mago":
            Defesa = 3 + Fisico + Mago["Bonus_de_Defesa_M"]
        elif Classe.lower() == "ladino":
            Defesa = 3 + Fisico + Ladino["Bonus_de_Defesa_L"]
        else:
            Defesa = 3 + Fisico

        # Calculo de ataque
        if Classe.lower() == "guerreiro":
            Ataque = 3 + Fisico + Guerreiro["Bonus_de_Ataque_G"]
        elif Classe.lower() == "mago":
            Ataque = 3 + Estilo + Mago["Bonus_de_Ataque_M"] + Mago["Bonus_de_Estilo_M"]
        elif Classe.lower() == "ladino":
            Ataque = 3 + Fisico + Ladino["Bonus_de_Ataque_L"] + Ladino["Bonus_de_Estilo_L"]
        else:
            Ataque = 3 + Fisico

        # Entrega de vida, defesa e ataque
        print("=" * 30)
        print(f"HP: {Hp}")
        print(f"Defesa: {Defesa}")
        print(f"Ataque: {Ataque}")
        print("=" * 30)
