# Queues are another form of linear data structure very similar to stacks.
# The difference is queues follow the FIFO rule - First In First Out, much like real life queues,
# Where the person gets in first, gets to leave first.
# Quesues can be implemented with both arrays and linked lists but the array implementation is not eficient
# Because for removing an element from the queues, which happens from the front of the array(queue),
# the indices of the array have to be updated every time, essentially making it an O(n) operation,
# Whereas the same operation can be done in O(1) time with linked lists.
# Queues have enqueue and dequeue operations which correspond to the push and pop operations of stacks , 
# only difference being dequeue removes element from the front
# Time complexities are as follows:
# Peek - O(1)
# Enqueue - O(1)
# Dequeue - o(1)
class Node():
    def __init__(self, data, next=None):
        self.data = data # Stores the value of the node
        self.next = next # Pointer (or Reference) to the next node

class Queue():
    def __init__(self):
        self.first = None # Points to the front of the queue (first element to be removed when dequeued)
        self.last = None # Points to the end of the queue (last element entered)
        self.length = 0

    # Returns the element that is at the front of the queue
    def peek(self):
        if self.first is None:
            return None
        return self.first.data

    # Adds an element to the end of the queue
    # If empty then the new node would be the first entry making it both the first and last
    # Else, the next of the last node, which was pointing to None, point to the new node
    # and them it will update the last node to be the new node
    #Time complexity will be O(1)
    def enqueue(self, data):
        new_node = Node(data)
        if self.last == None:
            self.first = new_node
            self.last = new_node
            self.length = 1
        else:
            self.last.next = new_node
            self.last = new_node
            self.length += 1
        
    # Removes the front element of the queue  
    # If the queue is empty, it will print an apropriate message  
    def dequeue(self):
        if self.last == None:
            print("Queue is Empty")
        # Else, it will simply make the first node become the next element of the first node
        # and decrease the length by 1, effectively deleting the first element.
        else:
            self.first = self.first.next
            self.length -= 1
            #We make the bottom pointer None if there was only 1 element in the stack and that gets popped
            if self.length == 0:
                self.last = None

    #Finally we'll create the print method which prints the elements of the queue in, well, a queue like format
    def print_queue(self):
        if self.length == 0:
            print("Queue Empty")
        else:
            current_pointer = self.first
            while(current_pointer!= None):
                if current_pointer.next == None:
                    print(current_pointer.data)
                else:
                    print(f'{current_pointer.data}  <<--  ', end='')
                current_pointer = current_pointer.next
        print()

my_queue = Queue()
my_queue.enqueue("Joy")
my_queue.enqueue("Matt")
my_queue.enqueue("Pavel")
my_queue.enqueue("Samir")
my_queue.print_queue()
# Joy  <<--  Matt  <<--  Pavel  <<--  Samir

print("First in Queue:",my_queue.peek())
# First in Queue: Joy

print()

my_queue.dequeue()
my_queue.print_queue()
# Matt  <<--  Pavel  <<--  Samir

my_queue.dequeue()
my_queue.dequeue()
my_queue.dequeue()
my_queue.print_queue()
# Queue Empty"

print("First Element:",my_queue.first)
print("Last Element:",my_queue.last)

print("\nQueue Length:",my_queue.length)

my_queue.dequeue()
# Queue is Empty
