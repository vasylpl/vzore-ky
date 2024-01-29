funkce1 = True
while funkce1 == True:
    print("Pro výpočet objemu kvádru stiskni 1")
    print("Pro výpočet obvodu obdélníku stiskni 2")
    print("Pro výpočet oobsahu obdélníku stiskni 3")
    print("Pro ukončení programu stiskni 4")

    výběr = int(input("váš výber: "))

    if výběr == 1 :

        print("výpočet objemu kvadru")

        a = int(input("zadej proměnou a: "))
        b = int(input("zadej proměnou b: "))
        c = int(input("zadej proměnou c: "))


        if a>0 and b>0 and c>0:
            vysledek = a*b*c
            a = print("vysledek je: ", vysledek)
        else:
            print("zkus to znovu")


    elif výběr == 2 :
        print("výpočet obvodu obdelníku")

        a = input("zadejte proměnou a: ")
        b = input("zadejte proměnou b: ")

        a = int(a)
        b = int(b)

        if a>0 and b>0:
            vysledek = 2*a+2*b
            print("výsledek je: ", vysledek)
        else:
            print("zkus to znova")


    elif výběr == 3 :
        print("výpočet obsahu obd")

        a = input("zadej proměnou a: ")
        b = input("zadej proměnou b: ")

        a = int(a)
        b = int(b)

        if a>0 and b>0:
            vysledek = a*b
            print("vysledek je: ", vysledek)
        else:
            print("zkus to znovu")


    elif výběr == 4 :
        print("podrž alt a stiskni F4")
        funkce1 = False

    else:
        print("špatný výběre")