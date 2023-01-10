class node:
    def __init__(self, value=None, nextNode = None):
        self.value = value
        self.nextNode = nextNode
        
class linkedList(node):
    def __init__(self, head=None):
	    self.head=head
	    
    def get_tail(self):
        if self.head is None:
            return None
        itr = self.head
        while True:
            if itr.nextNode is None:
                return itr
            itr = itr.nextNode

    def iterate(self, position):
        itr = self.head
        for i in range(position):
            if itr.nextNode is None:
                print('Linked list over, position too large.')
                return
            itr = itr.nextNode
        return itr

    def insert(self, value, position):
        oldNode = self.iterate(position-1)
        newNode = node(value)
        newNode.nextNode = oldNode.nextNode
        oldNode.nextNode = newNode

    def insert_at_end(self, value):
        tail = self.get_tail()
        newNode = node(value)
        tail.nextNode = newNode
    
    def insert_at_start(self, value):
        newNode = node(value)
        newNode.nextNode = self.head
        self.head = newNode

    def Print(self):
        itr = self.head
        while True:
            print(itr.value," -> ", end="")
            if itr.nextNode is None:
                return
            itr = itr.nextNode
    def rev_rec(self, node):
        if node.nextNode is None:
            print(node.value, end=" ")
            return
        self.rev_rec(node.nextNode)
        print(node.value, end=" ")
        return

    def Print_rev(self):
        if self.head != None:
            self.rev_rec(self.head)
        else:
            print('Empty Linked List.')
            return
    
    def rev_ll_rec_exe(self, node):
        if node.nextNode is None:
            self.head = node
            return
        self.rev_ll_rec_exe(node.nextNode)
        tempNode = node.nextNode
        tempNode.nextNode = node
        node.nextNode = None
        return

    def rev_ll_rec(self):
        if self.head != None:
            self.rev_ll_rec_exe(self.head)
        else:
            print('Empty Linked List.')
            return
        
    
ll = linkedList()

node1 = node(3)
ll.head = node1
ll.insert_at_end(5)

for i in range(4):
    val= input('Enter node value : ')
    ll.insert_at_end(int(val))
    
ll.Print()
print()
ll.rev_ll_rec()
ll.Print()
