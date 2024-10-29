class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("Stack is empty")

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            raise IndexError("Stack is empty")

    def size(self):
        return len(self.items)


# 1. Function to Evaluate Postfix Expressions Using a Stack
def evaluate_postfix(expression):
    stack = Stack()
    operators = set(['+', '-', '*', '/'])

    for token in expression.split():
        if token.isdigit():
            stack.push(int(token))
        elif token in operators:
            operand2 = stack.pop()
            operand1 = stack.pop()
            if token == '+':
                stack.push(operand1 + operand2)
            elif token == '-':
                stack.push(operand1 - operand2)
            elif token == '*':
                stack.push(operand1 * operand2)
            elif token == '/':
                stack.push(operand1 / operand2)
    
    return stack.pop()

# Test evaluate_postfix
print(evaluate_postfix("3 4 + 2 * 7 /"))  # Expected output: (3 + 4) * 2 / 7 = 2.0


# 2. Queue Using Two Stacks
class QueueWithStacks:
    def __init__(self):
        self.stack1 = Stack()
        self.stack2 = Stack()

    def enqueue(self, item):
        self.stack1.push(item)

    def dequeue(self):
        if self.stack2.is_empty():
            while not self.stack1.is_empty():
                self.stack2.push(self.stack1.pop())
        if self.stack2.is_empty():
            raise IndexError("Queue is empty")
        return self.stack2.pop()

# Test QueueWithStacks
queue = QueueWithStacks()
queue.enqueue(1)
queue.enqueue(2)
queue.enqueue(3)
print(queue.dequeue())  # Expected output: 1
print(queue.dequeue())  # Expected output: 2
queue.enqueue(4)
print(queue.dequeue())  # Expected output: 3


# 3. Task Scheduler Using a Queue
class Queue:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def enqueue(self, item):
        self.items.append(item)

    def dequeue(self):
        if not self.is_empty():
            return self.items.pop(0)
        else:
            raise IndexError("Queue is empty")

    def size(self):
        return len(self.items)


def task_scheduler(tasks):
    queue = Queue()
    for task in tasks:
        queue.enqueue(task)

    while not queue.is_empty():
        task = queue.dequeue()
        print(f"Processing task: {task}")

# Test Task Scheduler
tasks = ["task1", "task2", "task3", "task4"]
task_scheduler(tasks)  # Expected output: Processes each task in the order they were added


# 4. Convert Infix Expression to Postfix Using a Stack
def infix_to_postfix(expression):
    stack = Stack()
    postfix = ""
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2, '(': 0}

    for token in expression:
        if token.isalnum():  # If operand, add to output
            postfix += token
        elif token == '(':  # If '(', push to stack
            stack.push(token)
        elif token == ')':  # If ')', pop until '(' is found
            top_token = stack.pop()
            while top_token != '(':
                postfix += top_token
                top_token = stack.pop()
        else:
            # If operator, pop operators of higher or equal precedence
            while not stack.is_empty() and precedence[stack.peek()] >= precedence[token]:
                postfix += stack.pop()
            stack.push(token)

    # Pop all remaining operators
    while not stack.is_empty():
        postfix += stack.pop()

    return postfix

# Test infix_to_postfix
print(infix_to_postfix("A+B*C-D"))  # Expected output: ABC*+D-