#!/usr/bin/python3
import math

def Lbd():
    print("""
    |>+---+----------------------------------------------<|
    |>| 1 |            LUAS BANGUN DATAR                 <|
    |>+---+----------------------------------------------<|
    |>^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^<|
    |>menu:                                              <|
    |>1. luas segitiga-----------------------------------<|
    |>2. luas persegi------------------------------------<|
    |>3. luas persegi panjang----------------------------<|
    |>4. luas lingkaran----------------------------------<|
    |>5. luas trapesium----------------------------------<|
    |>6. luas jajargenjang-------------------------------<|
    |>0. back--------------------------------------------<|
    |>00.exit--------------------------------------------<|
    |>___________________________________________________<|
   """)
    menu = input('select menu: ')
    if menu == '1':
        l_segitiga()
    elif menu == '2':
        l_persegi()
    elif menu == '3':
        l_persegipanjang()
    elif menu == '4':
        l_lingkaran()
    # elif menu == '5':
    # elif menu == '6':
    # elif menu == '0':
    # elif menu == '00':
        # exit()

def back(): 
    Lbd()

def luas_trapesium():  # daftar
    back()

def l_segitiga():  # daftar
    while True:
        print('ditanya: ')
        print('1. luas\n'
        '2. alas\n'
        '3. tinggi\n'
        '0. back\n'
        '00.exit')
        menu = input('input menu: ')
        if menu == '0':
            back()
        elif menu == '1':
            while True:
                a = float(input('alas:'))
                t = float(input('tinggi:'))
                l = (a*t)/2
                print(f'      {a}x{t}\n'
                'luas = -----\n'
                '         2\n'
                f'luas = {l}\n')
                input()
                a = input('try again(y/n)? ')
                if a == 'y' or a == 'Y':
                    print()
                elif a == 'n' or a == 'N':
                    break
        elif menu == '2':
            while True:
                l = int(input('luas: '))
                t = int(input('tinggi: '))
                a = (l*2)/t
                print('%s x 2\n'
                'alas = ------\n'
                '          %s\n'
                'alas = %.2f' % (l, t, a))
                a = input('try again(y/n)? ')
                if a == 'y' or a == 'Y':
                    print()
                elif a == 'n' or a == 'N':
                    break
        elif menu == '3':
            while True:
                l = int(input('luas: '))
                a = int(input('alas: '))
                t = (l*2)/a
                print('%s x 2\ntinggi = -----\n%s\ntinggi = %.2s' % (l, a, t))
                a = input('try again(y/n)?')
                if a == 'y' or a == 'Y':
                    print()
                elif a == 'n' or a == 'N':
                    break
def l_persegi():  # daftar
    while True:
        s = int(input('sis: '))
        l = s*s  # luas bujur sangkar
        print(f'luas = {s} x {s} = {l}')
        a = input('try again(y/n)? ')
        if a == 'y' or a == 'Y':
            print()
        elif a == 'n' or a == 'N':
            back()

def l_persegipanjang():  # daftar
    while True:
        print('Ditanya:\n1. luas\n2. panjang\n3. lebar\n0. back\n00. exit')
        menu = input('select menu: ')
        if menu == '1':
            while True:
                p = float(input('panjang: '))
                l = float(input('lebar: '))
                ls = p*l
                print('luas = p x l')
                print('luas = %s x %s = %s' % (p, l, ls))
                a = input('try again(y/n)? ')
                if a == 'y' or a == 'Y':
                    print()
                elif a == 'n' or a == 'N':
                    break
        elif menu == '2':
            while True:
                l = float(input('luas: '))
                lb = float(input('lebar: '))
                p = l/lb
                print('panjang = luas/lebar')
                print(
                    'p = %s\n'
                    '    --\n'
                    '     %s' % (l, lb))
                print(f'panjang = {p}')
                a = input('try again(y/n)? ')
                if a == 'y' or a == 'Y':
                    print()
                elif a == 'n' or a == 'N':
                    break
        elif menu == '3':
            while True:
                l =  float(input('luas: '))
                p = float(input('panjang: '))
                lb = l/p
                print('lebar = luas/panjang')
                print(
                    '         %s\n'
                    'lebar = --\n'
                    '         %s\n'
                    'lebar = %s'
                    % (l, p, lb)
                )
                a = input('try again(y/n)? ')
                if a == 'y' or a == 'Y':
                    print()
                elif a == 'n' or a == 'N':
                    break
        elif menu == '0':
            back()
        elif menu == '00':
            exit()
        #end l_persegipanjang

#lingkarang
def l_lingkaran():  # daftar
    while True:
        print(
            'diketahui:\n'
            '1. jari-jari\n'
            '2. diameter\n'
            '3. luas\n'
            '0. back\n'
            '00. exit'
        )
        menu = input('select menu: ')
        if menu == '1':
            while True:
                r = float(input('jari-jari: '))
                phi = 22 / 7
                pangkat = r**2
                l = phi*(r**2)
                print(
                    'luas = phixr^2\n'
                    f'    = {phi}*{r}^2\n'
                    f'    = {phi}*{pangkat}\n'
                    f'    = {l}'
                )
                a = input('try again(y/n)?')
                if a == 'y' or a == 'Y':
                    print()
                elif a == 'n' or a == 'N':
                    break

        elif menu == '2':
            while True:
                d = float(input('diameter: '))
                r = d/2 
                phi = 22 / 7
                pangkat = r ** 2
                l = phi * (r ** 2)
                print(
                    'ubah diameter ke jari-jari: %.2f/2 = %.2f\n'
                    'luas = phi x r**2\n'
                    '     = %s x %s **2\n'
                    ''
                )
                # end lingkaran
        elif menu == '3':
            print()
        elif menu == '0':
            back()
        elif menu == '00':
            exit()

while True:
    Lbd()