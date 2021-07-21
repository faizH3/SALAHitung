import math


def part3():  # daftar ke3 kalkulus persamaan dan pertidaksamaan
    print('''
    |>3.  PART 3(PERSAMAAN DAN PERTIDAKSAMAAN------------<|
    menu:
    1.  persamaan
    2.  pertidaksamaan
    0.  kembali
    00. keluar    
    ''')
    menu = input('menu: ')
    if menu == '1':
        while True:
            print('''
bentuk umum persmnaan kuadrat ax^2+bx+c=0
contoh:
x^2+x-2=0
a=1, b=1,, c=-2

input a: 1
input b: 1
input c: -2

    -b+-/b^2-4ac
x = ------------
        2a
    -1+-/1^2-4(1)(-2)     
  = -----------------
           2(1)
    -1+-/1+8
  = --------
       2
    -1+-/9
  = ------
      2
    -1+-3
  = -----
      2
     -1+3  |      -1-3
x1 = ----- | x2 = -----
       2   |        2
      2    |      -4
   = ---   |    = ---
      2    |       2
x1 = 1     |x2  = -2
            ''')
            print('-------------------------')
            print('menentukan akar persamaan')
            print('      ax^2+bx+c=0\n')
            a = int(input('input a: '))
            b = int(input('input b: '))
            c = int(input('input c: '))
            bb = -b
            b_2 = b ** 2
            ac = 4 * a * c
            d = (b ** 2) - (4 * a * c)
            penyebut = 2 * a
            akar = math.sqrt(b)
            xa = bb + akar
            xb = bb - akar
            x1 = (bb + akar) / (2 * a)
            x2 = (bb - akar) / (2 * a)
            # print(b_2, ac, d, penyebut, akar)
            print('''
            menggunakan rumus persamaan kuadrat:
                -b +- /b^2-4ac
            x = --------------
                       2a

                -(%s) +- /%s^2-4(%s)(%s)
            x = ------------------
                        2(%s)

                %s +- /%s-(%s)
              = -------------
                      %s

                %s +- /%s
              = --------
                    %s

                %s +- %i
              = -------
                   %s
                 %s + %i 
            x1 = ------  
                   %s
                 %i
               = -
                 %s
            x1 = %s

                 %s - %i
            x2 = ------
                   %s
                 %i
               = --
                 %s
            x2 = %s
            ''' % (
                b, b, a, c, a, bb, b_2, ac, penyebut, bb, d, penyebut, bb, akar, penyebut, bb, akar, penyebut, xa,
                penyebut,
                x1, bb, akar, penyebut, xb, penyebut, x2))
            print('jadi akar-akar persamaannya adalah, x1 = %s dan dan x2 = %s' % (x1, x2))
            print('\n[yes|no|exit]')
            a = input("ulangi lagi[y/n/x]: ")
            if a == "n" or a == "N":
                break
            elif a == "y" or a == "Y":
                print()
            elif a == 'x' or a == 'X':
                exit()
        # !!!!!!tambah pertidaksamaan


def part1():  # daftar ke1 kalkulus
    print('''
    |>1.  PART 1(FUNGSI LINEAR)--------------------------<|
    bentuk operasi:
    1.  y = ax + b
    2.  y = ax^2 + bx + c
    0.  back
    00. exit
    ''')
    menu = input('menu: ')
    if menu == '1':
        while True:
            print('''
    contoh:
    y = ax + b
    soal
    y = 2x + 8
    input a = 2
    input b = 8
            ''')
            a = float(input("input a: "))
            b = float(input('input b: '))
            print('misal, x = 0')
            print('y = %s(0)+(%s)' % (a, b))
            x = b / a
            y = a * 0 + b
            print('y = %s ----->(0,%s)\n' % (y, y))
            print('misal, y = 0')
            print('(0) = %sx + %s' % (a, b))
            print('%sx = %s' % (a, b))
            print('       %s' % (b))
            print('x = -------')
            print("       %s" % (a))
            ab = 'x = %.2f ------>(%.2f,0)' % (x, x)
            print(ab)
            print('titik koordinatnya adalah (0,%.2f) dan (%.2f,0)' % (y, x))
            input()
            a = input('try again(y/n)? ')
            if a == 'y' or a == 'Y':
                print()
            elif a == 'n' or a == 'N':
                break


def luas_segitiga():  # daftar luas bangun datar
    while True:
        print('ditanya: ')
        print("menu: ")
        print('1. luas\n'
              '2. alas\n'
              '3. tinggi\n'
              '0. back')
        # print('ditanya:')
        menu = input('input menu: ')
        if menu == '0':
            daftarlist()
        elif menu == '1':
            while True:
                a = float(input('alas: '))
                t = float(input('tinggi: '))
                luas = (a * t) / 2
                print(f'       {a}x{t}\n'
                      'luas = -------\n'
                      f'          2\n'
                      f'luas = %s' % (luas))
                a = input('try again(y/n)? ')
                if a == 'y' or a == 'Y':
                    print()
                elif a == 'n' or a == 'N':
                    break
        elif menu == '2':
            while True:
                luas = int(input("luas: "))
                t = int(input("tinggi: "))
                a = (luas * 2) / t
                print('       %s x 2\n'
                      'alas = ------\n'
                      '          %s\n'
                      'alas = %.3s' % (luas, t, a))
                a = input("try again(y/n)? ")
                if a == 'y' or a == 'Y':
                    print()
                elif a == 'n' or a == 'N':
                    break
        elif menu == '3':
            while True:
                luas = int(input('luas: '))
                a = int(input('alas: '))
                t = (luas * 2) / a
                print('         %s x 2\n'
                      'tinggi = ------\n'
                      '            %s\n'
                      'tinggi = %.2s' % (luas, a, t))
                a = input('try again(y/n)? ')
                if a == 'y' or a == 'Y':
                    print()
                elif a == 'n' or a == 'N':
                    break


def luas_persegi():  # daftar luas bangun datar
    while True:
        print('2. luas persegi')
        s = int(input("sisi: "))
        luas = s * s
        print(f'luas = {s} x {s} = {luas}')
        a = input('try again(y/n)? ')
        if a == 'y' or a == 'Y':
            print()
        elif a == 'n' or a == 'N':
            luasbangundatar()


def luas_persegiPanjang():  # daftar luas bangun datar
    while True:
        print('3. luas persegi panjang')
        print('Ditanya: \n'
              '1. luas\n'
              '2. panjang\n'
              '3. lebar\n'
              '0. kembali\n'
              '00. keluar')
        menu = input('pilih menu: ')
        if menu == '1':
            while True:
                p = float(input('panjang: '))
                l = float(input('lebar: '))
                luas = p * l
                print('luas  = p x l')
                print('luas = %s x %s = %s' % (p, l, luas))
                a = input('try again(y/n)? ')
                if a == 'y' or a == 'Y':
                    print()
                elif a == 'n' or a == 'N':
                    break
        elif menu == '2':
            while True:
                luas = float(input('luas: '))
                l = float(input('lebar: '))
                p = luas / l
                print('panjang = luas / lebar')
                print('          %s\n'
                      'panjang = --\n'
                      '          %s' % (luas, l))
                print(f'panjang = {p}')
                a = input('try again(y/n)? ')
                if a == 'y' or a == 'Y':
                    print()
                elif a == 'n' or a == 'N':
                    break
        elif menu == '3':
            while True:
                luas = float(input('luas: '))
                p = float(input('panjang: '))
                l = luas / p
                print('lebar = luas / panjang')
                print('        %s\n'
                      'lebar = --\n'
                      '        %s\n' % (luas, p))
                print(f'lebar = {l}')
                a = input('try again(y/n)? ')
                if a == 'y' or a == 'Y':
                    print()
                elif a == 'n' or a == 'N':
                    break
        elif menu == '0':
            luasbangundatar()


def luas_lingkaran():  # daftar luas bangun datar
    while True:
        print("diketahui: \n"
              "1. jari-jari\n"
              "2. diameter\n"
              "3. luas\n"
              "0. kembali\n"
              "00. exit")
        menu = input("pilih menu: ")
        if menu == '1':
            while True:
                r = float(input("jari-jari: "))
                phi = 22 / 7
                pangkat = r ** 2
                luas = phi * (r ** 2)
                print("luas = phi x r^2")
                print('luas = 22/7 x %s^2' % (r))
                print("luas = 22/7 x %.2f" % (pangkat))
                print('luas = %.3s' % (luas))
                a = input("try again(y/n)? ")
                if a == 'y' or a == 'Y':
                    print()
                elif a == 'n' or a == 'N':
                    break
        elif menu == '2':
            while True:
                d = float(input('diameter: '))
                r = d / 2
                phi = 22 / 7
                pangkat = r ** 2
                luas = phi * (r ** 2)
                print('ubah diamater ke jari-jari: %.2f/2 = %.2f' % (d, r))
                print('luas = phi x r^2')
                print('luas = 22/7 x %.2f^2' % (r))
                print('luas = 22/7 x %.2f' % (pangkat))
                print('luas = %.2f' % (luas))
                a = input('try again(/n)? ')
                if a == 'y' or a == 'Y':
                    print()
                elif a == 'n' or a == 'N':
                    break
        elif menu == '3':
            while True:
                print('diketahui: ')
                luas = float(input(''))
                phi = 22 / 7
                r = luas / phi
                print('r = luaas/phi')
                print('r = %.2f / %.2f' % (luas, phi))
                print('r = %.2f' % (r))
                a = input('try again(y/n)? ')
                if a == 'y' or a == 'Y':
                    print()
                elif a == 'n' or a == 'N':
                    break
        elif menu == '0':
            luasbangundatar()
        elif menu == '00':
            exit()


def luas_trapesium():  # daftar luas bangun datar
    # belum ada isi
    luasbangundatar()


def luas_jajargenjang():  # daftar luas bangun datar
    # belum ada isi
    luasbangundatar()


def daftarlist():
    print("""
======================================================
||||||||||||PROGRAM KALKULATOR SEDERHANA||||||||||||||
|>--------------------------------------------------<|
[>>>>>>>>>>>>>>>>>>>>MENU PROGRAM<<<<<<<<<<<<<<<<<<<<]
|====================================================|
|>+---+                                             <|
|>| 1 | LUAS BANGUN DATAR                           <|
|>+---+                                             <|
|>| 2 | MENGHITUNG DERET LUAS BUJUR SANGKAR KALKULUS<|
|>+---+                                             <|
|>| 3 | KALKULUS                                    <|
|>+---+                                             <|
|>| 0 | EXIT                                        <|
|>+---+                                             <|
|>^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^<|
|>__________________________________________________<|
   """)
    print(">>>>>>>>>>>>>>>>>>>")
    menu = input('input menu: ')
    print(">>>>>>>>>>>>>>>>>>>")
    if menu == '1':
        luasbangundatar()
    elif menu == '2':
        deret()
    elif menu == '3':
        kalkulus()
    elif menu == '0':
        exit()


def luasbangundatar():
    print("""

    |>+---+----------------------------------------------<|
    |>| 1 | LUAS BANGUN DATAR                            <|
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
    menu = input("select menu: ")
    if menu == '1':
        luas_segitiga()
    elif menu == '2':
        luas_persegi()
    elif menu == '3':
        luas_persegiPanjang()
    elif menu == '4':
        luas_lingkaran()
    elif menu == '5':
        luas_trapesium()
    elif menu == '0':
        daftarlist()
    elif menu == '00':
        exit()


def deret():
    while True:
        print('''
        |>+---+---------------------------------------------<|
        |>| 2 | MENGHITUNG DERET LUAS BUJUR SANGKAR KALKULUS<|
        |>+---+---------------------------------------------<|
        ''')
        c1 = float(input("sisi bujur sangkar pertama[1]:"))
        c2 = c1 / 2  # bujur sangkar ke-2 ==mencari sisi miring
        c_2 = c2 ** 2
        c3 = (c2 ** 2) + (c2 ** 2)
        c4 = math.sqrt(c3)
        c5 = c4 / 2  # bujur sangkar ke-3 ==mencari sisi miring
        c_5 = c5 ** 2
        c6 = (c5 ** 2) + (c5 ** 2)
        c7 = math.sqrt(c6)
        c8 = c1 * c1  # luas bujur sangkar pertama
        c9 = (c4) * c4  # luas bujur sangkar kedua
        c10 = c7 * c7  # luas bujur sangkar ketiga
        cr = c9 / c8  # rasio
        c_r = 1 - cr
        c11 = c8 / (1 - cr)  # total luas
        print("luas [1]= %.2f x %.2f" % (c1, c1))
        print("luas [1]= %.2f" % (c8))
        print("")
        print("sisi [2]?")
        print("sisi [2] = sisi miring segitiga siku-siku sama kaki")
        print("A^2 = %.2f^2 + %.2f^2" % (c2, c2))
        print("A^2 = %.2f + %.2f" % (c_2, c_2))
        print("A   = /%.2f" % (c3))
        print("A   = %.2f" % (c4))
        print("")
        print("sisi [2], %.2f" % (c4))
        print("luas [2] = %.2f x %.2f" % (c4, c4))
        print("luas [2] = %.2f" % (c9))
        print("")
        print("sisi [3]?")
        print("A^2 = %.2f^2 + %.2f^2" % (c5, c5))
        print("A^2 = %.2f + %.2f" % (c_5, c_5))
        print("A   = /%.2f" % (c6))
        print("A   = %.2f" % (c7))
        print("")
        print("sisi [3],%.2f" % (c7))
        print("luas [3] = %.2f x %.2f" % (c7, c7))
        print("luas [3] = %.2f" % (c10))
        print("")
        print("rasio = %.2f / %s" % (c9, c8))
        print("      = %.2f" % (cr))
        print("")
        print("total luas[s] = %s / (1-%.2f)" % (c8, cr))
        print("              = %s / %.2f" % (c8, c_r))
        print("              = %.2f" % (c11))
        print("")
        print("luas bujur sangkar pertama:%.2f" % (c8))
        print("luas bujur sangkar kedua  :%.2f" % (c9))
        print("luas bujur sangkar ketiga :%.2f" % (c10))
        print("rasio                     :%.2f" % (cr))
        print("jumlah luas               :%.2f" % (c11))
        print("-----------------------------------------------------------------")
        menu = input('try again(y/n)? ')
        if menu == 'y' or menu == 'Y':
            print()
        elif menu == 'n' or menu == 'N':
            daftarlist()


def kalkulus():
    print("""
    |>+---+----------------------------------------------<|
    |>| 3 | KALKULUS                                     <|
    |>+---+----------------------------------------------<|
    |>^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^<|
    |>                        menu:                      <|
    |>1.  PART 1(FUNGSI LINEAR)--------------------------<|
    |>?.  PART 2(SISTEM BILANGAN REAL)-------------------<|
    |>3.  PART 3(PERSAMAAN DAN PERTIDAKSAMAAN------------<|
    |>?.  PART 4(PERTIDAKSAMAAN IRASIONAL)---------------<|
    |>?.  PART 5(QUIS)-----------------------------------<|
    |>?.  PART 6(LIMIT FUNGSI)---------------------------<|
    |>?.  PART 7(LIMIT FUNGSI)---------------------------<|
    |>?.  PART 8(TURUNAN FUNGSI)-------------------------<|
    |>?.  PART 9(MID)------------------------------------<|
    |>??. PART 10(SISTEM BILANGAN REAL DAN FUNGSI)-------<|
    |>??. PART 11(LINEAR TENTU DAN TAK TENTU)------------<|
    |>??. PART 12(INTEGRAL)------------------------------<|
    |>??. PART 13(INTEGRAL GANDA)------------------------<|
    |>0.  back-------------------------------------------<|
    |>00. exit-------------------------------------------<|
    |>___________________________________________________<|
    """)
    print('Note! ? kosong')
    menu = input('pilih menu: ')
    if menu == '1':
        part1()
    # elif menu=='2':
    #     part2()
    elif menu == '3':
        part3()  # persamaan--------input c masih error jika valuenya positif
    elif menu == '0':
        daftarlist()
    elif menu == '00':
        exit()


daftarlist()