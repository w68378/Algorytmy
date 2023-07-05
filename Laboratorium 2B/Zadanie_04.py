def newton(n=5,m=5):
    
	if n<0 or m<0: return print("nieprawidłowa wartosc")
    
	tab=[[]]   
    
	i=0
    
	while(i<n):                 
        
		j=0
        
		while(j<m):             
            
			if j==0 or j==i: tab[i].append(1)
            
			elif j>i: tab[i].append("NaN")
            
			else: tab[i].append(tab[i-1][j]+tab[i-1][j-1])
            
			j+=1
        
		i+=1
        
		tab.append([])
    print(tab)

newton()


    