class stack():
    
	def init(self):
        
		self.stack = list()

    def isEmpty(self):
        
		return len(self.stack) <=0

    def push(self,item):
        
		self.stack.append(item)

    def pop(self):
        
		if self.isEmpty(): return None
        
		else: return self.stack.pop()
    
    def peek(self):
        
		if self.isEmpty():
            
			return None
        
		else: return self.stack[len(self.stack)-1]
    
    def str(self):
        
		return str(self.stack)
    

def czylitera(a):
    
	if ord(a)>=65 and ord(a)<=90: return "WL"   
    
	elif ord(a)>=97 and ord(a)<122: return "ML" 
    
	elif ord(a)>=48 and ord(a)<=57: return "C"  
    
	elif a==' ': return "Space"
    
	else: return "NL"  

def poprawnosc(tekst):
    
	slowo=stack()
    
	b="W zdanie występuje błąd"
    
	popr="Zdanie poprawne"

    for i in tekst:
        if not slowo.isEmpty(): p=k   
        k=czylitera(i)
        

        if k=='Space': slowo=stack()   
        
        elif k=='ML':  
              
            if  slowo.isEmpty() or p!='C' and p!='NL':
                
				slowo.push(i)                                      
                
            else: return b

        elif k=='WL':                  
            
			if slowo.isEmpty(): slowo.push(i)
            
			else: return b
        
        elif k=='C': 
            
			if slowo.isEmpty() or czylitera(slowo.peek())=='C':     
                
				slowo.push(i)
            
			else: return b

        elif k=='NL':           
		
            slowo.push(i)
            
        else: return b

    return popr


a='Ala ma kota'  

b='Al@ m@ k0ta'  

c='alA ma kota'   

d='Ala ma 231 kotow!!!'  

e='A!a &ma kota' 

tab=[a,b,c,d,e]

for j in tab:
    
	print(poprawnosc(j))