class stack:
    def __init__(self,size):
        self.maxsize = size
        self.top = -1
        self.stk = []
    def isEmpty(self):
        return(self.top == -1)
    def isFull(self):
        return(self.top ==(self.maxsize - 1))
    def peek(self):
        if (not self.isEmpty()):
            return(self.stk[self.top])
    def push(self,ele):
        if (not self.isFull()):
            self.top +=1
            self.stk.append(ele)
            return True
        return False
    def pop(self):
        if (not self.isEmpty()):
            self.top -=1
            self.stk.remove(self.stk[-1])
            return True
        return False
    
s= int(input("Enter the size of stack::"))
stack1 = stack(s)
stack2 = stack(s)#another stack will be used for sortiong
e="None"#like stack2 it is also ised for sortiong
while(s>0):
    s-=1
    stack1.push(int(input("Enter element:")))
while ( not stack1.isEmpty()):
    e = stack1.peek()
    stack1.pop()
    while ( not stack2.isEmpty() and stack2.peek()>e):
        stack1.push(stack2.peek())
        stack2.pop()
    stack2.push(e)
#at this point the elements are sorted and stored into stack
#and restore these into the stack1
print("/nAfter sortiong:")
while (not stack2.isEmpty()):
    e = stack2.peek()
    print("Element:",e,sep='')
    stack1.push(e)
    stack2.pop()