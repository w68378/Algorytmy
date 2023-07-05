def nwd_II_reku(a,b):
    
    if b==0: return print(f"nwd wynosi {a}")
    
	else: return nwd_II_reku(b,a%b)
         

a=int(input("Podaj a: "))

b=int(input("Podaj b: "))

Nnwd_II_reku(a,b)