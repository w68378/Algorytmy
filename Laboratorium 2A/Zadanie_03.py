import random

def najw(l,r,A):

    m=(r-l)+1      

    if m==1: return A[l]    

    elif m==2: 

        if A[l]>A[r]: return A[l]   

        else: return A[r]  

    else:  

        a=najw(l,r-(m//2),A)     

        b=najw(r-(m//2)+1,r,A)      

        if a>b:                         

            return a

        else:

            return b

tab=[random.randint(1, 100) for _ in range(25)]

print(najw(0,len(tab)-1,tab))             
        