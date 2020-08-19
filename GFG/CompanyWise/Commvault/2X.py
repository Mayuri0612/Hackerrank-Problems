##################Implement stack using ll(insertion and del at end)############################
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedListStack:
    def __init__(self):
        self.head = None

    def isEmpty(self):
        return self.head == None

    def push(self, data):
        new_node = Node(data)
        if self.isEmpty():
            self.head = new_node
        else:
            last = self.head
            while(last.next is not None):
                last = last.next
            last.next = new_node


    def pop(self):
        if self.isEmpty():
            return None
        else:
            temp = self.head
            while(temp.next.next is not None):
                temp = temp.next
            temp.next = None


    def printlist(self):
        if self.isEmpty():
            return None
        else:
            temp = self.head
            while temp is not None:
                print(temp.data,sep = ' ', end = ' ')
                temp = temp.next

######################## Function to reverse stack elements using recursion ############

def reverseStack(self,stack):
    if self.isEmpty():
        temp = stack.pop()
        reverse(stack)
        fillBottom(stack, temp)

def fillBottom(self,stack, data):
    if self.isEmpty():
        stack.push(data)
    else:
        temp = stack(pop)
        fillBottom(stack, data)
        stack.push(temp)

###############################Main####################################################

s = LinkedListStack()
n = int(input())
inputarr = [int(i) for i in input().split()][:n]
for j in range(n):
    s.push(inputarr[j])
print("Our stack is : ", end = '')
s.printlist()
s.pop()
s.pop()
print("\nOur popped stack is : ", end = '')
s.printlist()




            

                




