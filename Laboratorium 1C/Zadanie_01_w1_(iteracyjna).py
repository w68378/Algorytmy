a = int(input("Podaj a: "))

b = int(input("Podaj b: "))

while a != b:

    if a > b:

        a = a - b

    else:

        b = b - a

print(f"NWD wynosi {a}")