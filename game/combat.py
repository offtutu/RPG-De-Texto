from game.player import Hp, Ataque, Defesa, Ficha_Valida
from game.boss import Nome_Boss, Hp_Boss, Ataque_Boss, Defesa_Boss

if Ficha_Valida:
    # Definindo as variaveis de combate do player.
    vida_do_player = Hp
    defesa_do_player = Defesa
    ataque_do_player = Ataque

    # Definindo as variaveis de combate do boss.
    vida_do_boss = Hp_Boss
    defesa_do_boss = Defesa_Boss
    ataque_do_boss = Ataque_Boss

    # Sistema de combate.
    while vida_do_player > 0 and vida_do_boss > 0:
        print("=" * 30)
        print(f"Sua vida: {vida_do_player}")
        print(f"Vida do boss: {vida_do_boss}")
        print(f"Defesa do boss: {defesa_do_boss}")
        print("=" * 30)

        print("1 - atacar")
        print("2 - fugir")
        Acao_Combate = input("Escolha sua acao: ")

        if Acao_Combate == "1":
            if ataque_do_player >= defesa_do_boss:
                dano_restante = ataque_do_player - defesa_do_boss
                defesa_do_boss = 0
                vida_do_boss -= dano_restante
            else:
                defesa_do_boss -= ataque_do_player
            print(f"Voce acertou o boss, seu dano foi {ataque_do_player}.")
        elif Acao_Combate == "2":
            print("Voce nao pode fugir bobalhao.")
        else:
            print("Essa opcao vira em breve...")

        if vida_do_boss <= 0:
            break

        if ataque_do_boss >= defesa_do_player:
            dano_do_boss = ataque_do_boss - defesa_do_player
            defesa_do_player = 0
            vida_do_player -= dano_do_boss
        else:
            defesa_do_player -= ataque_do_boss
            dano_do_boss = 0

        print(f"{Nome_Boss} te acertou e te deu {dano_do_boss} de dano.")

    # Mensagem do final da luta, quando um dos dois morre.
    if vida_do_player <= 0:
        print("Voce foi morto por:", Nome_Boss)
    elif vida_do_boss <= 0:
        print(f"Voce matou o {Nome_Boss}")
    # Aqui é setada a condição onde o usuário tem que uma ficha para o combate.
else:
    print("O combate nao pode comecar porque a ficha do jogador ficou invalida.")
