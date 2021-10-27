#!/usr/bin/python3

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


