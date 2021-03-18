from time import sleep
import random

print('{:_^20}'.format(' Jokenpô '))
print('\nVamos jogar pedra, papel e tesoura!')


lista = ['pedra', 'papel', 'tesoura']
jogador = int(
    input(
        '''[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura
Digite sua escolha:'''
    )
)

print('No 3 nós jogamos!')

sleep(1)
print('1')
sleep(1)
print('2')
sleep(1)
print('3!')
maquina = random.choice(lista)


if jogador == 1:
    print('Você escolheu pedra!')
    print('Eu escolho {}!'.format(maquina))
    if maquina == 'pedra':
        print('Deu empate! Ninguém leva dessa vez.')
    elif maquina == 'papel':
        print('Papel ganha de pedra! Eu venci!')
    elif maquina == 'tesoura':
        print('Pedra ganha de tesoura, você venceu. :(')
elif jogador == 2:
    print('Você escolheu papel')
    print('Eu escolho {}!'.format(maquina))
    if maquina == 'pedra':
        print('Papel ganha de pedra, você venceu.')
    elif maquina == 'papel':
        print('Deu empate! Ninguém leva dessa vez.')
    elif maquina == 'tesoura':
        print('Tesoura ganha de papel, você perdeu!')
elif jogador == 3:
    print('Você escolheu tesoura')
    print('Eu escolho {}!'.format(maquina))
    if maquina == 'pedra':
        print('Pedra ganha de tesoura, você perdeu!')
    elif maquina == 'papel':
        print('Tesoura ganha de papel, você venceu. :(')
    elif maquina == 'tesoura':
        print('Deu empate! Ninguém leva dessa vez.')
else:
    print('Está opção não está disponível, tente novamente')
