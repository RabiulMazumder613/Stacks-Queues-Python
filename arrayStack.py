class Stack():

    # The constructor consists of only an empty array
    # as length comes built-in with arrays(lists)
    def __init__(self):
        self.array = []

    # The peek method will allow us to peek at the top element,i.e.,
    # It will return the element at the top of the stack
    # Time complexity will be O(1)    
    def peek(self):
        if len(self.array) == 0:
            return None
        else:
            return self.array[len(self.array) - 1]

    # For push operation, we use the built-in append method of lists, 
    # which appends/pushes/inserts an element at the end of the list(top of the stack)
    def push(self, data):
        self.array.append(data)

    def pop(self):
        if len(self.array) != 0:
            self.array.pop()
        else:
            print("Stack is empty")

    def print_stack(self):
        if len(self.array) == 0:
            print("Stack empty")
        else:
            for i in range(len(self.array)-1, -1, -1):
                print(self.array[i])
        print()
            # Alternative for loop to traverse in reverse order ⬇
            # for i in reversed(self.array):
            #     print(i)

my_stack = Stack()
print("Current Top:",my_stack.peek())
# Current Top: None

print()

my_stack.push("google")
my_stack.push("udemy")
my_stack.push("discord")
my_stack.print_stack()
#discord
#udemy
#google

print(my_stack.__dict__)
#{'array': ['google', 'udemy', 'discord']}

print("Current Top:",my_stack.peek())
# Current Top: discord

print()

my_stack.pop()
my_stack.print_stack()
# udemey
# google


print("Current Top:",my_stack.peek())
# udemy

print(my_stack.__dict__)
#{'array': ['google', 'udemy']}

print()

my_stack.pop()
my_stack.pop()
print(my_stack.__dict__)
my_stack.print_stack()
# {'array': []}
# Stack Empty