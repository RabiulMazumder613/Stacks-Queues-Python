class Node():
    def __init__(self, data, next=None):
        self.data = data # Stores the value of the node
        self.next = next # Pointer (or Reference) to the next node

class Stack():
    def __init__(self):
        self.top = None
        self.bottom = None
        self.length = 0

# The peek method will allow us to peek at the top element,i.e.,
# It will return the element at the top of the stack
# Time complexity will be O(1)
    def peek(self):
        if self.top is None:
            return None
        return self.top.data

    # Insert an element at the top of the stack time complexity is O(1)
    def push(self, data):
        new_Node = Node(data)
        # If the stack is empty, 
        # we make the top and bottom pointer both point to the new node
        if self.top == None:    # Alternative: (if self.length == 0: ) 
            self.top = new_Node
            self.bottom = new_Node
            self.length = 1
        # Otherwise, we make the next of the new node, 
        # which was pointing to None, 
        # point to the present top and then update the top pointer to be the new_node
        # now the new_node is the top pointer
        else:
            # It is the same as prepend
            new_Node.next = self.top 
            self.top = new_Node 
            self.length += 1

    # Remove the top element from the stack its time complexity is O(1)
    def pop(self):
        # If the stack is empty print this message below
        if self.top is None:  # Alternative: (if self.length == 0: )
            print("Stack is empty")
        # Else we make the top pointer point to what is next of the top pointer and decrease the length by 1, 
        # effectively deleting the top element.
        else:
            self.top = self.top.next
            self.length -= 1
            # We make the bottom pointer None if there was only 1 element in the stack 
            # and that gets popped
            if self.length == 0:
                self.bottom = None

    #Finally we'll implement a print method which prints the elements of the stack from top to bottom
    #This will be an O(n) operation as we'll obviously have to traverse the entire linked list to print all elelments
    def print_stack(self):
        if self.top == None:
            print("Stack empty")
        else:
            current_pointer = self.top
            while(current_pointer != None):
                print(current_pointer.data)
                current_pointer = current_pointer.next
        print()


my_stack = Stack()
print("Current Top:",my_stack.peek())
# Current Top: None

my_stack.push('google')
my_stack.push('udemy')
my_stack.push('discord')
my_stack.print_stack()
#discord
#udemy
#google

print("Current Top:",my_stack.peek())
# Current Top: discord

print("\nStack Length:",my_stack.length)
# Stack Length: 3

print("\nCurrent Bottom:",my_stack.bottom.data)
# Current Bottom: google

my_stack.pop()
my_stack.print_stack()
#udemy
#google

print("Stack Length:",my_stack.length)
# Stack Length: 2

print("\nCurrent Top:",my_stack.peek())
# Current Top: udemy

print()

my_stack.pop()
my_stack.print_stack()
# google

print("Current Top:",my_stack.peek())
print("Current Bottom",my_stack.bottom)
# Current Top: google

print() 

my_stack.pop()
my_stack.print_stack()
#Stack Empty

print("Current Top:",my_stack.peek())
print("Current Bottom:",my_stack.bottom)
# Current Top: None
# Current Bottom: None

print("\nStack Length:",my_stack.length)
# Stack Length: 0
