# Singly Linked List

class LifeCycle:
    def __init__(self ,value ,nextRef=None):
        self.value=value;
        self.nextRef=nextRef
    

class  Animals:
    def __init__(self):
        self.head=None;
        self.NodeAll=[];

    def AddLifeCycle(self ,value):
        reference=LifeCycle(value)
        if self.head is None:
            self.head=reference;
            return;
        
        current=self.head;
        
        while current.nextRef is not None:
            current=current.nextRef;
            
        current.nextRef=reference;

    def showCycle(self):
        self.NodeAll = []
        current=self.head;
        while current is not None:
            self.NodeAll.append({
                'value':current.value
            })
            current=current.nextRef;
        
        return self.NodeAll;
    
    def AddDataAtStarting(self,value):
        newNode=LifeCycle(value)
        newNode.nextRef=self.head;
        self.head=newNode
        
    def AddLastIndex(self,value):
        ref=LifeCycle(value)
        current=self.head;
        while current.nextRef is not None:
            current=current.nextRef
        current.nextRef=ref
        
    def AddAnywhere(self,search,data):
        current=self.head;
        while current is not None:
            if current.value==search:
                current.value=data
                break;
            else:
                current=current.nextRef;
        current.value=data
            
        
        

system= Animals()
system.AddLifeCycle("frog")
system.AddLifeCycle("snack")
system.AddLifeCycle("egal")


AllNode=system.showCycle()
print(AllNode)

system.AddDataAtStarting("insects") 

AllNode=system.showCycle()
print(AllNode)

system.AddLastIndex('human')

AllNode=system.showCycle()
print(AllNode)

system.AddAnywhere('human','animal')
AllNode=system.showCycle()
print(AllNode)