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
    
def nawiasy(tekst):
    
	stos= stack()
    
	for i in tekst:
        
		if i=="(" or i=="[" or i=="{": stos.push(i)
        
		elif i==")" or i=="]" or i=="}": 
           
		   if stos.isEmpty(): return print("Błąd w tekście")
           
		   elif ord(stos.peek()) == ord(i)-1 or ord(stos.peek()) == ord(i)-2: stos.pop() 
           
		   else: return print("Błąd w tekście")  
        
    if not stos.isEmpty(): return print("Błąd w tekście") 
    
	else: return print ("Tekst poprawny")


przyk_tekst=['(()()()())','(((())))','(()((())()))','((((((())','()))','(()()(()']

for i in przyk_tekst:
    
	nawiasy(i)



