def hanoi(n, początkowy, koniec, roboczy):

    if n == 1:

        print(f"Przenieś krążek 1 z patyka {początkowy} na patyk {koniec}")

        return

    hanoi(n-1, początkowy, roboczy, koniec)

    print(f"Przenieś krążek {n} z patyka {początkowy} na patyk {koniec}")

    hanoi(n-1, roboczy, koniec, początkowy)

n = 3

hanoi(n, 'A', 'B', 'C')