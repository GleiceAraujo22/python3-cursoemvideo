#Melhore o jogo do DESAFIO 28 onde o computador vai “pensar” em um número entre 0 e 10.
#Só que agora o jogador vai tentar adivinhar até acertar, mostrando no final
#quantos palpites foram necessários para vencer.

from random import randint
from time import sleep
c = 0
computador = randint(0, 10)
print('-=-' * 20)
print('\033[1;31mSou seu computador...Acabei de pensar em um número entre 0 e 10.\033[m')
print('Será que você consegue adivinhar qual foi? ')
print('-=-' * 20 )
acertou = False
palpites = 0
while not acertou:
    jogador = int(input('Qual é o seu palpite? '))
    palpites += 1
    if jogador == computador:
        acertou = True
    else:
        if jogador < computador:
            print('MAIS...Tente mais uma vez. ')
        elif jogador > computador:
            print('MENOS...Tente mais vez.')
print(f'Acertou com {palpites} tentativas. Parabéns!')

