from game.player import Hp, Ataque, Defesa, Ficha_Valida
from game.boss import Nome_Boss, Hp_Boss, Ataque_Boss, Defesa_Boss
from game.magia import Fire_Ball, Ice_Ray, Light_Spheres

if Ficha_Valida:
    # Definindo as variaveis de combate do player.
    vida_do_player = Hp
    defesa_do_player = Defesa
    ataque_do_player = Ataque

    # Definindo as variaveis de combate magico do player.
    dano_da_magia_do_player = {
        "1": Fire_Ball["dano"],
        "2": Ice_Ray["dano"],
        "3": Light_Spheres["dano"],
    }

    # Definindo as variaveis de combate do boss.
    vida_do_boss = Hp_Boss
    defesa_do_boss = Defesa_Boss
    ataque_do_boss = Ataque_Boss

    # Mini introducao do combate.
    print("=" * 30)
    print("Voce encontra uma porta gigante de uma sala, deseja empurrar para abrir?")
    print("1 - Sim")
    print("2 - Nao")
    Escolha_Da_Porta = input("Escolha uma opcao: ")
    if Escolha_Da_Porta == "1":
        print(
            f"Voce empurra a porta e ela se abre, revelando um grande salao. "
            f"No centro tem uma pilha de corpos e, no topo dela, esta {Nome_Boss}."
        )
    elif Escolha_Da_Porta == "2":
        print(
            f"Voce decide nao abrir a porta, mas ela se abre sozinha. "
            f"No centro do salao tem uma pilha de corpos e, no topo dela, esta {Nome_Boss}."
        )
    else:
        print("Opcao invalida. A porta se abre sozinha.")

    print("Robertinho: Finalmente alguem para estar em minha ultima danca...")
    print("Robertinho te convida para um duelo ate a morte, voce deseja aceitar?")
    print("1 - Sim")
    print("2 - Nao")
    Escolha_Do_Duelo = input("Escolha uma opcao: ")
    if Escolha_Do_Duelo == "1":
        print("Voce aceita o duelo. Robertinho ja cai na sua pose de luta.")
    else:
        print(
            "Voce recusa o duelo, mas Robertinho nao aceita um nao como resposta. "
            "Ele ja cai na sua pose de luta."
        )
        print(
            "Como penalidade pela recusa, o primeiro turno do combate e de Robertinho."
        )

    # Ataque inicial do boss caso o jogador recuse o duelo.
    if Escolha_Do_Duelo == "2":
        if ataque_do_boss >= defesa_do_player:
            dano_do_boss = ataque_do_boss - defesa_do_player
            defesa_do_player = 0
            vida_do_player -= dano_do_boss
        else:
            defesa_do_player -= ataque_do_boss
            dano_do_boss = 0

        print(f"{Nome_Boss} te acertou e te deu {dano_do_boss} de dano.")

    # Sistema de combate.
    while vida_do_player > 0 and vida_do_boss > 0:
        print("=" * 30)
        print(f"Sua vida: {vida_do_player}")
        print(f"Vida do boss: {vida_do_boss}")
        print(f"Defesa do boss: {defesa_do_boss}")
        print("=" * 30)

        print("1 - atacar")
        print("2 - usar magia")
        print("3 - fugir")
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
            print("Escolha uma magia para usar:")
            print("1 - Bola de Fogo")
            print("2 - Raio de Gelo")
            print("3 - Esferas de Luz")
            Magia_Escolhida = input("Escolha uma magia: ")

            dano_magia = dano_da_magia_do_player.get(Magia_Escolhida)
            if dano_magia is None:
                print("Magia invalida. Voce perdeu a vez.")
                dano_magia = 0

            if dano_magia >= defesa_do_boss:
                dano_restante = dano_magia - defesa_do_boss
                defesa_do_boss = 0
                vida_do_boss -= dano_restante
            else:
                defesa_do_boss -= dano_magia

            print(f"Voce usou a magia, seu dano foi {dano_magia}.")
        elif Acao_Combate == "3":
            print("Voce nao pode fugir bobalhao.")
        else:
            print("Essa opcao ainda nao existe.")

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
else:
    print("O combate nao pode comecar porque a ficha do jogador ficou invalida.")
