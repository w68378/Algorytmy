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
    
def cyfr_znak_space(a):
    
	if ord(a) >= 48 and ord(a) <=57: return 'L'   
    
	elif a=='*' or a=='+' or a=='-' or a=='/' or a=='^': return  'O'
   
    elif a=='=': return 'W' 

    else: return 'blank'   

def operacja(a, b, oper):
    
	if oper == '+': return int(a)+int(b)
    
	elif oper == '-': return int(a)-int(b)
    
	elif oper == '*': return int(a)*int(b)
    
	elif oper == '/': return int(a)/int(b)
    
	elif oper == '^': return int(a)**int(b)

def postfiks(tekst):
    
	argumenty = stack()

    for i in range(len(tekst)):     
        
		k=cyfr_znak_space(tekst[i])       
        
		if k=='O': 
            
			b=argumenty.pop()               
            
			a=argumenty.pop()
            
			argumenty.push(operacja(a,b,tekst[i]))     
        
		elif k=='L': 
        
            argumenty.push(tekst[i])
            
        elif k=='W':
            
			return print(argumenty.pop())

tekst="73+52-2^*=" 

postfiks(tekst)
