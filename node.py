class node:
    def __init__(self, value=None, nextNode = None):
        self.value = value
        self.nextNode = nextNode
        
class linkedList(node):
    def __init__(self, head=None):
	    self.head=head
	    
    def tail(self, head):
	    self.cur = head
	    while True:
        	print (self.cur.value, " -> ", end=""),
        	if(self.cur.nextNode == None):
        	    return cur
        	    break
        	self.cur = self.cur.nextNode
    def traverse(self):
        self.cur = self.head
        while True:
        	print (self.cur.value, " -> ", end=""),
        	if(self.cur.nextNode == None):
        	    break
        	self.cur = self.cur.nextNode
    def incert(self, value=None):
        self.newnode = node(value)
        self.tail = self.tail(self.head)
        print(self.tail.value)
        self.tail.nextNode = self.newnode
        self.traverse()
        return
        
    
    
ll = linkedList()

node1 = node(3)
ll.head = node1



cur = ll.head
while True:
	print (cur.value, " -> ", end=""),
	if(cur.nextNode == None):
	    break
	cur = cur.nextNode
	
while True:
    print(ll.head)
    inp = input("Enter node value: ")
    ll.incert(inp)
