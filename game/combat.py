import random

from game.player import Hp, Ataque, Defesa, Ficha_Valida
from game.boss import bosses
from game.magia import Fire_Ball, Ice_Ray, Light_Spheres
from game.introducao_bosses import mini_introducao_robertinho

if Ficha_Valida:
    # Definindo as variaveis de combate do player.
    vida_do_player = Hp
    defesa_do_player = Defesa
    ataque_do_player = Ataque

    # Definindo as variaveis de combate magico do player.
    dano_da_magia_do_player = {
        "1": Fire_Ball["dano"] + Fire_Ball["dano_de_fogo"],
        "2": Ice_Ray["dano"] + Ice_Ray["dano_de_gelo"],
        "3": Light_Spheres["dano"],
    }

    # Definindo as variaveis de combate do boss.
    boss_atual = bosses["robertinho"]
    Nome_Boss = boss_atual["Nome_Boss"]
    Hp_Boss = boss_atual["Hp_Boss"]
    Defesa_Boss = boss_atual["Defesa_Boss"]
    Ataque_Boss = boss_atual["Ataque_Boss"]

    vida_do_boss = Hp_Boss
    defesa_do_boss = Defesa_Boss
    ataque_do_boss = Ataque_Boss
    combate_encerrado_por_fuga = False

    efeitos_introducao = mini_introducao_robertinho(Nome_Boss)
    boss_ataca_primeiro = efeitos_introducao["boss_ataca_primeiro"]
    covardia_ativa = efeitos_introducao["covardia_ativa"]
    chance_falha_covardia = efeitos_introducao["chance_falha_covardia"]
    if efeitos_introducao.get("jogador_morreu"):
        vida_do_player = 0

    # Ataque inicial do boss caso o jogador recuse o duelo.
    if boss_ataca_primeiro and vida_do_player > 0:
        if ataque_do_boss >= defesa_do_player:
            dano_do_boss = ataque_do_boss - defesa_do_player
            defesa_do_player = 0
            vida_do_player -= dano_do_boss
        else:
            defesa_do_player -= ataque_do_boss
            dano_do_boss = 0

        print(f"{Nome_Boss} te acertou e te deu {dano_do_boss} de dano.")
        boss_ataca_primeiro = False

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
            if covardia_ativa and random.random() < chance_falha_covardia:
                print("A covardia te trava e seu ataque falha.")
            else:
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
            elif covardia_ativa and random.random() < chance_falha_covardia:
                print("A covardia te trava e sua magia falha.")
            else:
                if dano_magia >= defesa_do_boss:
                    dano_restante = dano_magia - defesa_do_boss
                    defesa_do_boss = 0
                    vida_do_boss -= dano_restante
                else:
                    defesa_do_boss -= dano_magia

                print(f"Voce usou a magia, seu dano foi {dano_magia}.")
        elif Acao_Combate == "3":
            combate_encerrado_por_fuga = True
            break
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
    elif combate_encerrado_por_fuga:
        print("Voce fugiu do combate, mas ganhou a fama de covarde e isso trara consequencias.")
else:
    print("O combate nao pode comecar porque a ficha do jogador ficou invalida.")
