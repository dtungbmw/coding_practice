class Node :
    next=None
    value=None

class LinkedList:

    header = None
    #tail = None
    size = 0

    a = Node()
    a.value = "a"
    b = Node()
    a.next = b
    b.value = "b"
    c = Node()
    c.value = "c"
    b.next = c
    d = Node()
    d.value = "d"
    c.next = d

    header = a
    size = 4
    #tail = d

    def reverse(self):
        f = self.header
        n1 = f.next
        n2 = None
        for i in range(self.size-1):
            n2 = n1.next
            n1.next = f
            f = n1
            n1 = n2
        self.header = f


    def print(self):
        cnode = self.header
        for i in range(self.size):
            print(cnode.value, end =" ")
            cnode = cnode.next


ll = LinkedList()
ll.print()
print("  ")
ll.reverse()
ll.print()







