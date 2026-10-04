class Circular:
    def __init__(self,size):
        self.size=size;
        self.rear=self.front=-1;
        self.lts=[None]*size
    
    def isEmpty(self):
        return self.front==-1 and self.rear==-1;
    
    def isFull(self):
        return (self.rear+1)%self.size==self.front;
    
    def Enqueue(self,data):
        if self.isFull():
            print('Queue is full');
            return;
        if self.isEmpty():
            self.lts[self.rear+1]=data
            self.front+=1;
            self.rear+=1;
            return;
        else:
            self.rear=(self.rear+1)%self.size
            self.lts[self.rear]=data;
            return;
    
    def Dequeue(self):
        if self.isEmpty():
            print('Alreay Empty');
            return;
        self.lts[self.front]=None;        
        if self.rear == self.front:
            self.rear=self.front=-1;
            return;
        self.front=(self.front+1)%self.size
           
            
    def peak(self):
        print(self.lts)
        
    
   

cr=Circular(3);
cr.Enqueue(4)  
cr.Enqueue(5)
cr.Enqueue(9)
cr.Dequeue()
cr.Dequeue()
cr.Dequeue()
cr.Enqueue(30)
cr.Enqueue(67)
cr.Enqueue(7)
cr.Enqueue(90)
cr.peak();      