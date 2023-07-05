def NWD_I_reku(a,b):
    
    if a==b: return print(f"nwd wynosi: {a}")
    
	elif a>b: return nwd_I_reku(a-b,b)
    
	else: return nwd_I_reku(a,b-a)

a=int(input("Podaj a: "))

b=int(input("podaj b: "))

nwd_I_reku(a,b)