a = int(input("Podaj a: "))

b = int(input("Podaj b: "))

while  b:

    zmian = b

    b = a % b

    a = zmian

print(f"NWD wynosi: {a}")