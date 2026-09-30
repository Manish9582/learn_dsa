# Tata Daewoo , Range Rover SUVs ,Jaguar Luxury ,Sports Cars ,Tata.ev ,Tata Motors
# Add Data , At The Starting ,At the End , At any where ,delete  <- curcular

class Node:
    def __init__(self,value,next=None,prev=None):
        self.value=value;
        self.next=next;
        self.prev=prev
        

class Cars:
    def __init__(self):
        self.head=None;
    
    def AddCars(self,data):
        ref=Node(data);
        if self.head is None:
            self.head=ref;
            self.head.next=ref;
            self.head.prev=ref;
            return;
        current=self.head;
        
        while current.next !=self.head:
            current=current.next;
        
        current.next=ref;
        ref.prev=current
        ref.next=self.head;
        self.head.prev=ref
        
    def printNodes(self):
        current=self.head
        while True:
            print(current.value)
            current=current.next;
            if current == self.head:
                break;
    

    def AddAtStart(self,data):
        ref=Node(data);
        if self.head is None:
            print('Node is empty');
            
        current=self.head;
        while current.next != self.head:
            current = current.next
        
        ref.next=self.head;
        ref.prev=current
        
        self.head.prev=ref
        current.next=ref;
        
        self.head=ref
        
    def AtTheEnd(self ,data):
        ref=Node(data);
        current=self.head;
        while current.next != self.head:
            current = current.next
            
        current.next=ref;
        ref.prev=current
        ref.next=self.head;
        
    
    def deleteNode(self,data):
        if self.head is None:
            print('Node is empy')
            return;
        
        if self.head==self.head.next:
            if self.head.value==data:
                self.head=None;
                return;
                
        #fisrt node index
        if self.head.value==data:
            last=self.head;
            while last.next !=self.head:
                last=last.next;
            last.next=self.head.next;
            self.head.next.prev=last
            self.head=self.head.next
            
        
        #Delete any where
        current = self.head

        while True:
            if current.value == data:
                current.prev.next = current.next
                current.next.prev = current.prev
                return

            current = current.next

            if current == self.head:
                break
            
            
                
        
          
        

car=Cars();
car.AddCars('Tata Daewoo');
car.AddCars('Range Rover SUVs');
car.AddAtStart('Sports Cars')
car.AtTheEnd('Tata Motors')
car.deleteNode('Tata Daewoo')
car.printNodes()