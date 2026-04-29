from game.debuffs import Covarde


def mini_introducao_robertinho(Nome_Boss):
    boss_ataca_primeiro = False
    covardia_ativa = False
    chance_falha_covardia = 0

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
    elif Escolha_Do_Duelo == "2":
        boss_ataca_primeiro = Covarde["penalidade_instanea"]["boss_ataca_primeiro"]
        chance_falha_covardia = Covarde["penalidade_em_combate"][
            "chance_falha_ataque_magia"
        ]
        covardia_ativa = True
        print(
            "Voce recusa o duelo, mas Robertinho nao aceita um nao como resposta. "
            "Ele ja cai na sua pose de luta."
        )
        print(
            "Como penalidade pela recusa, o primeiro turno do combate e de Robertinho."
        )
        print("Enquanto a covardia durar, voce tem 50% de chance de falhar em ataques e magias.")
    else:
        print("Opcao invalida. Robertinho interpreta sua indecisao como um aceite.")

    return {
        "boss_ataca_primeiro": boss_ataca_primeiro,
        "covardia_ativa": covardia_ativa,
        "chance_falha_covardia": chance_falha_covardia,
    }

def mini_introducao_sacripanta(Nome_Boss):
    boss_ataca_primeiro = False
    covardia_ativa = False
    chance_falha_covardia = 0
    jogador_morreu = False
