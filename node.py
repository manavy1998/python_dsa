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

    def incert_at_end(self, value):
        tail = self.get_tail()
        newNode = node(value)
        tail.nextNode = newNode
    
    def incert_at_start(self, value):
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
    
    
ll = linkedList()

node1 = node(3)
ll.head = node1
ll.incert_at_end(5)

while True:
    inp = input('Enter node value')
    ll.incert_at_start(inp)
    ll.Print()

	
