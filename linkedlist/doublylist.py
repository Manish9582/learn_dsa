class Node:
    def __init__(self ,data,next=None ,prev=None):
        self.value=data;
        self.next=next;
        self.prev=prev


class doublyList:
    def __init__(self):
        self.head=None;
        self.list=[];
    
    def AddData(self,data):
        ref=Node(data)
        if self.head is None:
            self.head=ref;
            return;
        
        current=self.head;
        while current.next is not None:
            current=current.next
            current=current.prev
        current.next=ref
        ref.prev=current
    
    def printAll(self):
        self.list=[];
        current=self.head;
        while current is not None:
            self.list.append({
                'name':current.value,
                'next':current.next,
                'prev':current.prev
            })
            current=current.next;
        return self.list;
    
    def AddAtStarting(self,data):
        current=self.head;
        ref=Node(data);
        if self.head is None:
            self.head=ref;
            return;
        
        current.prev=ref
        ref.next=current;
        self.head=ref
    
    def AddAtTheEnd(self,data):
        ref=Node(data)
        if self.head is None:
            self.head=ref
            return;
        
        current=self.head;
        while current.next is not None:
            current=current.next
        current.next=ref
        ref.prev=current
    
    def deleteIndex(self, data):
        current = self.head
        previous = None

        while current is not None:
            if current.value == data:
                if previous is None:
                    self.head = current.next
                else:
                    previous.next = current.next

                return
            previous = current
            current = current.next

        
        
        


db=doublyList();
db.AddData('varun')
db.AddData('vivek')

db.AddAtStarting('tahir')
db.AddAtTheEnd('gautam')
db.deleteIndex('gautam')

lst=db.printAll()
print(lst)