# RPG de Texto em Python

Projeto simples para praticar Python sem funcoes por enquanto.

## Estrutura

- `main.py`: inicia o fluxo do jogo
- `game/player.py`: cria a ficha do jogador
- `game/boss.py`: define os atributos do boss
- `game/combat.py`: roda o combate

## Como funciona hoje

1. `main.py` inicia o projeto
2. `game/player.py` pede nome, classe e distribuicao de pontos
3. Se a ficha estiver valida, `game/combat.py` inicia a luta
4. Se a ficha estiver invalida, o combate nao comeca

## Como rodar

```powershell
python main.py
```

## Regras atuais

- o jogador tem `6` pontos para distribuir
- cada atributo vai de `0` a `3`
- `vigor` aumenta o HP
- `fisico` aumenta defesa e ataque
- o boss comeca com vida, defesa e ataque fixos

## Ideias para expandir depois

- adicionar golpes diferentes
- adicionar uma introdução do boss na luta
- adicionar sistema de classes
- usar `estilo` e `instinto` no combate
- criar mais de um boss
- adicionar itens e cura
- no futuro, organizar tudo com funcoes
