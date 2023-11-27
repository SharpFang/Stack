class MyQueue:
    def __init__(self):
        self.stack1 = []
        self.stack2 = []

    def push(self, x):
        self.stack1.append(x)

    def pop(self):
        self.move_elements()
        if self.stack2:
            return self.stack2.pop()

    def peek(self):
        self.move_elements()
        if self.stack2:
            return self.stack2[-1]

    def empty(self):
        return not self.stack1 and not self.stack2

    def move_elements(self):
        if not self.stack2:
            while self.stack1:
                self.stack2.append(self.stack1.pop())

# Приклад
my_queue = MyQueue()
my_queue.push(1)
my_queue.push(2)
print(my_queue.peek())  # Вивід: 1
print(my_queue.pop())   # Вивід: 1
print(my_queue.empty())  # Вивід: False
