# A simple Python program for traversal of a linked list 
  
# Node class 
class Node: 
  
    # Function to initialise the node object 
    def __init__(self, data): 
        self.data = data  # Assign data 
        self.next = None  # Initialize next as null 
  
  
# Linked List class contains a Node object 
class LinkedList: 
  
    # Function to initialize head 
    def __init__(self): 
        self.head = None
  
    # This function prints contents of linked list 
    # starting from head 
    def printlinkedlist(self): 
        temp = self.head 
        while (temp): 
            print (temp.data, end =' ') 
            temp = temp.next
            
    def insertAtStart(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        
        self.head = new_node
        
    def insertAtNode(self, prev_node, new):
        if prev_node is None:
            print("Invalid slot")
        else:
            newnode = Node(new)
            newnode.next = prev_node.next
            prev_node.next = newnode
    
    def insertAtEnd(self, newdata):
        newnode1 = Node(newdata)
        if self.head is None:
            self.head = newnode1
            return
        else:
            last = self.head
            while(last.next):
                last = last.next
            last.next = newnode1
            
# Code execution starts here 
if __name__=='__main__': 

    llist = LinkedList()
    
    llist.head = Node("a")
    second = Node("b")
    third = Node("c")
    
    llist.head.next = second;
    second.next = third;
    
    llist.insertAtNode(second,"y")
    llist.insertAtStart("f")
    llist.insertAtEnd("hh")
    llist.printlinkedlist()
