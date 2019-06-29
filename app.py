import time
import math
import sys


def menu():
    print("+------------------------------+")
    print("|Alap számológép               |")
    print("|Válaszd ki a művelet betüjét  |")
    print("|A)Összeadás                   |")
    print("|B)Kivonás                     |")
    print("|C)Szorzás                     |")
    print("|D)Osztás                      |")
    print("|E)Hatványozás                 |")
    print("|F)Gyökvonás                   |")
    print("|A kilépéshez írj egy X betűt! |")
    print("+------------------------------+")


menu()

while True:

    usr_choice = input(">> ")

    if usr_choice == "A" or usr_choice == "a":
        print("Mennyi A?")
        a = int(input(">> "))
        print("Mennyi B?")
        b = int(input(">> "))
        print("Gondolkodok...")
        time.sleep(0.8)
        c = a + b
        print(c)
        print("Ha újra próbálnád akkor nyomj egy M-et")

    elif usr_choice == "B" or usr_choice == "b":
        print("Mennyi A?")
        a = int(input(">> "))
        print("Mennyi B?")
        b = int(input(">> "))
        print("Gondolkodok...")
        time.sleep(0.8)
        c = a - b
        print(c)
        print("Ha újra próbálnád akkor nyomj egy M-et")

    elif usr_choice == "C" or usr_choice == "c":
        print("Mennyi A?")
        a = int(input(">> "))
        print("Mennyi B?")
        b = int(input(">> "))
        print("Gondolkodok...")
        time.sleep(1.8)
        c = a * b
        print(c)
        print("Ha újra próbálnád akkor nyomj egy M-et")

    elif usr_choice == "D" or usr_choice == "d":
        print("Mennyi A?")
        a = int(input(">> "))
        print("Mennyi B?")
        b = int(input(">> "))
        print("Gondolkodok...")
        time.sleep(1.8)
        c = a / b
        print(c)
        print("Ha újra próbálnád akkor nyomj egy M-et")

    elif usr_choice == "E" or usr_choice == "e":
        print("Mennyi A?")
        a = int(input(">> "))
        print("Mennyi B?")
        b = int(input(">> "))
        print("Gondolkodok...")
        time.sleep(1.8)
        c = a ** b
        print(c)
        print("Ha újra próbálnád akkor nyomj egy M-et")

    elif usr_choice == "F" or usr_choice == "f":
        print("Mennyi A?")
        a = int(input(">> "))
        print("Gondolkodok...")
        time.sleep(0)
        c = math.sqrt(a)
        print(c)
        print("Ha újra próbálnád akkor nyomj egy M-et")

    elif usr_choice == "X" or usr_choice == "x":
        sys.exit()

    elif usr_choice == "M" or usr_choice == "m":
        menu()

    elif usr_choice == "pi" or usr_choice == "PI":
        print("a Pi pontos értéke:")
        print(math.pi)

    else:
        print("Kérlek a fent megadott betűk egyikét írd be!")
        print("Ha újra próbálnád akkor nyomj egy M-et")
        print("Ha ki akarsz lépni nyomj egy X-et")
        usr_choice
