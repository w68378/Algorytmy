def fibonaccii(n,tab=[0,1]):   
    
	range=len(tab)             
    
	while(range<=n):            
        
		tab.append(tab[range-1]+tab[range-2])
        
		range+=1
        
    return tab[range-1]

n=56

print(fibonaccii(n))