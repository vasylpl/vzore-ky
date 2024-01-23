print("vitejte v aplikaci pro vypočet obsahu obdelniku")

a = input("zadejte proměnou a: ")
b = input("zadejte proměnou b: ")

a = int(a)
b = int(b)

if a>0 and b>0:
    vysledek = a*b
    print("vysledek je: ", vysledek)
else:
    print("zkus to znovu")