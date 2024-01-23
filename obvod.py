print("vitejte v aplikaci pro vypočet obvodu obdelniku")

a = input("zadejte proměnou a: ")
b = input("zadejte proměnou b: ")

a = int(a)
b = int(b)

if a>0 and b>0:
    vysledek = 2*a+2*b
    print("vysledek je: ", vysledek)
else:
    print("tak jsi nadrbany?")