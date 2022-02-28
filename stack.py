# This .py file includes both the implementation of the class Stack and the requested showcase
import sys  # Needed to handle the passed arguments


class Stack:
    def __init__(self, maxSize = 1000):
        self.elements = []  # Stack implementation using a list
        self.size = 0  # Stack is initially empty
        self.maxSize = maxSize  # Stack has a maximum size

    def is_empty(self):
        return self.size == 0  # Currently 0 elements in the stack

    def is_full(self):
        return self.size == self.maxSize  # Currently maximum number of elements in the stack

    def push(self, newElement):
        if self.is_full():  # Check if there is enough space in the stack to add the new element
            # print("New elements cannot be added to a full stack!\n")
            return  # Don't do anything
        else:
            self.size += 1  # Increase the size by 1
            return self.elements.append(newElement)  # Add the element

    def pop(self):
        if self.is_empty():  # Check if there is at least one element in the stack
            # print("Stack is already empty!\n")
            return None  # No element to pop
        else:
            self.size -= 1  # Decrease the size by 1
            return self.elements.pop()  # Exclude the first element


def main(argv):
    if (len(sys.argv) - 1) != 1:  # Check if there are multiple strings as input
        print ("Input must be one string!")
    string = sys.argv[1]  # String is the first argument after program's name
    stack = Stack(len(string))  # Create a big enough stack
    for char in string:  # For each character of the given string
        # print(char)
        if char == '(' or char == '[' or char == '{':
            stack.push(char)  # Add it to stack
        elif char == ')':  # When ')' is encountered
            if stack.pop() != '(':  # '(' should be at the top of the stack in order to be balanced
                print ("Given string is NOT balanced!")
                return
        elif char == ']':  # When ']' is encountered
            if stack.pop() != '[':  # '[' should be at the top of the stack in order to be balanced
                print ("Given string is NOT balanced!")
                return
        elif char == '}':  # When '}' is encountered
            if stack.pop() != '{':  # '{' should be at the top of the stack in order to be balanced
                print ("Given string is NOT balanced!")
                return
        else:  # Another character
            print("Invalid input! It should contains only: '(', ')', '[', ']', '{', '}'")
            return
    if stack.is_empty():  # If at the end the stack is empty
        print("Given string is balanced!")  # No '(', '[', '{' remains unmatched and therefore stack is balanced
    else:  # If there is at least one '(', '[', '{' remains unmatched, stack is not balanced
        print ("Given string is NOT balanced!")


if __name__ == '__main__':
    main(sys.argv[1:])  # Pass every argument except the program's name to a function that gets the job done
