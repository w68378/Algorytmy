import os

class kolejka():
    
    def init(self):
        
        self.tab=[]
        
		self.head=0
        
		self.tail=len(self.tab)-1

    def isEmpty(self):
        
		return  (len(self.tab)-self.head) <=0
            
    def enqueue(self,item):
        
		self.tab.append(item)
        
		self.tail+=1

    def enqueuetab(self,item):
        
		for i in range(len(item)):
            
			self.tab.append(item[i])
        
		self.tail=len(self.tab)-1
    
    def dequeue(self):
        
		if not self.isEmpty():
            
			self.tail-=1
            
			return self.tab.pop(self.head)
        
		else: return print("Pusta kolejka")

    def peek(self):
        
		if not self.isEmpty():
            
			return self.tab[self.head]
        
		else: return print("Pusta kolejka")
       
    def size(self):
        
		return len(self.tab)
        
    def str(self):
        
		return str(self.tab)  

def podanie(osoby):
    
   osoby.enqueue(osoby.peek())
   
   osoby.dequeue()

def odpadanie(osoby):
    
	print(f"Odpada {osoby.dequeue()}")
    

def gra_ziemniak(n,imiona):  
    
	osoby=kolejka()
    
	osoby.enqueuetab(imiona)
    
	while(osoby.size()>1):
        

        for i in range(n):   
            
            podanie(osoby)
        
        odpadanie(osoby)
    
    print(f"Zwycięzcą zostaje: {osoby.peek()}")

imiona=['Marek','Mariusz','Dominik','Dominika','Anna','Renata','Artur','Andrzej','Sławomir','Ewelina']

gra_ziemniak(152,imiona)