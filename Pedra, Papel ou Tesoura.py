import random
print('Bem vindo ao jogo do Pedra papel ou tesoura, nesse jogo você irá batalhar contra a máquina. Boa sorte!')
print('O que você deseja jogar?')

numrodadas = 3
numdevitorias = 0
numdederrotas = 0
vencedor = str()
decisao = random.choice(['Pedra', 'Papel', 'Tesoura'])
while True:
    if numdevitorias > numdederrotas:
        vencedor = 'você'

    if numdederrotas > numdevitorias:
        vencedor = 'a máquina'
        
    if numrodadas == 0:
        print(f'Acabaram as rodadas, o vencedor foi: {vencedor}.')
        print('Obrigado por jogar!')
        break 

    print('''
1) Pedra
2) Papel
3) Tesoura
    ''')
    resposta_do_usuario = int(input('Digite a opção escolhida: '))

    if resposta_do_usuario < 1 or resposta_do_usuario > 3:
        print('Opção inválida, tente novamente.')
        continue
      
    if decisao == 'Pedra' and resposta_do_usuario == 1:
        decisao = random.choice(['Pedra', 'Papel', 'Tesoura'])
        print('Você jogou Pedra e a máquina também, um empate. Vamos tentar novamente.')
        continue

    if decisao == 'Papel' and resposta_do_usuario == 1:
        decisao = random.choice(['Pedra', 'Papel', 'Tesoura'])
        numrodadas -= 1
        print(f'Você jogou Pedra e a máquina Papel, você perdeu essa rodada. Restam {numrodadas} rodadas. Vamos pra próxima!')
        numdederrotas += 1
        continue
    
    if decisao == 'Tesoura' and resposta_do_usuario == 1:
        decisao = random.choice(['Pedra', 'Papel', 'Tesoura'])
        numrodadas -= 1
        print(f'Você jogou Pedra e a máquina Tesoura, você ganhou essa rodada. Restam {numrodadas} rodadas. Vamos pra próxima!')
        numdevitorias += 1
        continue

    if decisao == 'Pedra' and resposta_do_usuario == 2:
        decisao = random.choice(['Pedra', 'Papel', 'Tesoura'])
        numrodadas -= 1
        print(f'Você jogou Papel e a máquina Pedra, você ganhou essa rodada. Restam {numrodadas} rodadas. Vamos pra próxima!')
        numdevitorias += 1
        continue

    if decisao == 'Papel' and resposta_do_usuario == 2:
        decisao = random.choice(['Pedra', 'Papel', 'Tesoura'])
        print(f'Você jogou Papel e a máquina também, um empate. Vamos tentar novamente.')
        continue

    if decisao == 'Tesoura' and resposta_do_usuario == 2:
        decisao = random.choice(['Pedra', 'Papel', 'Tesoura'])
        numrodadas -= 1
        print(f'Você jogou Papel e a máquina Tesoura, você perdeu essa rodada. Restam {numrodadas} rodadas. Vamos pra próxima!')
        numdederrotas += 1
        continue

    if decisao == 'Pedra' and resposta_do_usuario == 3:
        decisao = random.choice(['Pedra', 'Papel', 'Tesoura'])
        numrodadas -= 1
        print(f'Você jogou Tesoura e a máquina Pedra, você perdeu essa rodada. Restam {numrodadas} rodadas. Vamos pra próxima!')
        numdederrotas += 1
        continue

    if decisao == 'Papel' and resposta_do_usuario == 3:
        decisao = random.choice(['Pedra', 'Papel', 'Tesoura'])
        numrodadas -= 1
        print(f'Você jogou Tesoura e a máquina Papel, você ganhou essa rodada. Restam {numrodadas} rodadas. Vamos pra próxima!')
        numdevitorias += 1
        continue

    if decisao == 'Tesoura' and resposta_do_usuario == 3:
        decisao = random.choice(['Pedra', 'Papel', 'Tesoura'])
        print(f'Você jogou Tesoura e a máquina também, um empate. Vamos tentar novamente.')
        continue