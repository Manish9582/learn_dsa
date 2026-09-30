class Node:
    def __init__(self):
        self.data=[];
    
    def push(self,data):
        self.data.append(data)
        
    def printAll(self):
        print(self.data)
    
    def pop(self):
        self.data.pop(0)
    
    def peek(self):
        return self.data[0]

data=Node();
data.push(10);
data.push(30);
data.push(13);
data.push(40);
data.pop()
rt=data.peek()
print(rt)
data.printAll()