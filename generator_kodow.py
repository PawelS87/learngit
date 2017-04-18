import random
import sys
print('######## GENERATOR KODÓW #########\n############# ver:1.0 ############\n' + '############## ' +(sys.platform)+ ' #############\n')
wyjscie = 'N'
while wyjscie == 'N':
    try:
        X = int(input('Podaj liczbę znaków w kodzie: '))
        print()
    except ValueError:
        print("Proszę wpisać poprawną liczbę ")
        continue
    try:
        N = int(input('Ile kodów losowych wygenerować? '))
        print()
    except ValueError:
        print("Proszę wpisać poprawną liczbę ")
        continue
    lista = ['1','2','3','4','5','6','7','8','9','0',
         'q','w','e','r','t','y','u','i','o','p',
         'a','s','d','f','g','h','j','k','l','z',
         'x','c','v','b','n','m',
         'Q','W','E','R','T','Y','U','I','O','P',
         'A','S','D','F','G','H','J','K','L','Z',
         'X','C','V','B','N','M',]
    z = ''
    for a in range(N):
        wynik = [random.choice(lista)for a in range(X)]
        wynik = [random.choice(lista)for a in range(X)]
        print(z.join(wynik))
    print('\n---> kodów wygenerowanych: ' + str(N) + '\n---> ilość znaków w kodzie: ' + str(X)+'\n')
    pytanie = input('wygenerować ponownie? T/N\n')
    if pytanie == 'T' or pytanie == 't' or pytanie == 'tak' or pytanie == 'TAK':
         print('\n')
    elif pytanie == 'N' or pytanie == 'n' or pytanie == 'nie' or pytanie == 'NIE':
         wyjscie = 'T'
    else:
        print('Niepoprawny wybór... Wyjście')

        wyjscie = 'T'
