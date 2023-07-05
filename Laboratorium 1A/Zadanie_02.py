n=-1

ile=0

while n<=0:

    n=int(input("Podaj n: "))

while n>0:

    a=int(input("Podaj liczbe: "))

    if a<0: ile+=1

    n-=1

print(f"W ciągu występuje {ile} liczb ujemnych")