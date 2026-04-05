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

Vigor = int(input("Digite os pontos que voce quer colocar em vigor (0 a 3): "))
Fisico = int(input("Digite os pontos que voce quer colocar em fisico (0 a 3): "))
Estilo = int(input("Digite os pontos que voce quer colocar em estilo (0 a 3): "))
Instinto = int(input("Digite os pontos que voce quer colocar em instinto (0 a 3): "))

Total = Vigor + Fisico + Estilo + Instinto

# Verificacao para ver se distribuicoes de status estao correta.
if Vigor > 3 or Fisico > 3 or Estilo > 3 or Instinto > 3:
    print("Um dos atributos chegou na quantidade maxima de pontos.")
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
    Hp = 6 + (Vigor * 5)

    # Calculo de defesa
    Defesa = 3 + Fisico

    # Calculo de ataque
    Ataque = 3 + (Fisico * 2)

    # Entrega de vida, defesa e ataque
    print("=" * 30)
    print(f"HP: {Hp}")
    print(f"Defesa: {Defesa}")
    print(f"Ataque: {Ataque}")
    print("=" * 30)
