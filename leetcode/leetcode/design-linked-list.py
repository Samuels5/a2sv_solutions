class Node:
    def __init__(self,val):
        self.val=val 
        self.next = None       

class MyLinkedList:

    def __init__(self):
        self.head = None
        self.size = 0
        

    def get(self, index: int) -> int:
        if index < self.size and self.head :
            cur = self.head
            for i in range(index):
                cur=cur.next
            print(self.size)
            return cur.val
        print(-1)
        return -1

    def addAtHead(self, val: int) -> None:
        temp = Node(val)
        if self.head == None:
            self.head=temp
        else:
            temp.next=self.head
            self.head = temp
        self.size+=1
        

    def addAtTail(self, val: int) -> None:
        temp = Node(val)
        if self.head == None:
            self.head = temp
        else:
            cur = self.head
            while cur.next != None:
                cur=cur.next
            cur.next=temp
        self.size+=1
        

    def addAtIndex(self, index: int, val: int) -> None:
        
        if index <= self.size:
            if index == 0:
                self.addAtHead(val)
            elif index == self.size:
                self.addAtTail(val)
            else:
                temp = Node(val)
                cur = self.head
                for i in range(index-1):
                    cur=cur.next
                temp.next =cur.next
                cur.next = temp
                self.size+=1
                    
            


        

    def deleteAtIndex(self, index: int) -> None:
        cur = self.head
        if index < self.size:
            if index ==  0:
                self.head = cur.next
            else:
                for i in range(index-1):
                    cur=cur.next
                cur.next =cur.next.next
            self.size -= 1  

        


# Your MyLinkedList object will be instantiated and called as such:
# obj = MyLinkedList()
# param_1 = obj.get(index)
# obj.addAtHead(val)
# obj.addAtTail(val)
# obj.addAtIndex(index,val)
# obj.deleteAtIndex(index)