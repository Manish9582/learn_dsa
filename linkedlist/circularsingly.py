# Add Data , At The Starting ,At the End , At any where ,delete  <- curcular

class Node:
    def __init__(self,value ,next=None):
        self.data=value;
        self.next=next;


class Car:
    def __init__(self):
        self.head=None;
        self.lst=[];
    
    def AddData(self,data):
        ref=Node(data);
        if self.head is None:
            self.head=ref
            ref.next=ref
            return;
        
        current=self.head;
        while current.next != self.head:
            current = current.next
        current.next=ref;
        ref.next=self.head
    
    def PrintNodes(self):
        if self.head is None:
            print('Node is empty');
            return;
        
        current=self.head;
        while True:
            print("current data",current.data,"current next",current.next)
            current=current.next;
            if current==self.head:
                break;
            
    def AddATStarting(self, data):
        ref = Node(data)
        if self.head is None:
            self.head = ref
            ref.next = ref
            return

        current = self.head
        while current.next != self.head:
            current = current.next

        current.next = ref
        ref.next = self.head
        self.head = ref
        
    
    def AddAtLast(self,data):
        ref=Node(data);
        if self.head is None:
            self.head = ref
            ref.next = ref
            return
        
        current=self.head;
        while current.next != self.head:
            current=current.next;
        
        current.next=ref;
        ref.next=self.head;
        
    def DeleteNode(self,deletevalue):
        print(deletevalue)
        if self.head is None:
            print('Node is empty');
            
        #if only one node Node Delete  
        if self.head.next==self.head:  
            if self.head==deletevalue:
                self.next=None;
            return;
        
        #fisrt node
        if self.head.data==deletevalue:
            frst=self.head;
            while frst.next !=self.head:
                frst=frst.next;
            self.head=self.head.next;
            frst.next=self.head
            
        prev=self.head;
        current=self.head;
        while current.next != self.head:
            if current.data==deletevalue:
                prev.next=current.next;
                return;
            
            prev = current
            current = current.next
        print("Value not found")
            
 
cr=Car();
cr.AddData('nano');
cr.AddData('tata mahindra');  
cr.AddData('thar');
cr.AddATStarting('rols royal');   
cr.AddAtLast('lamboar');
cr.DeleteNode('rols royal')
cr.PrintNodes()      