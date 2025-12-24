class Stack:
    def __init__(self):
        self.data = []   

    def push(self, item):
        self.data.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.data.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.data[-1]
    def empty(self):
        self.data = []
    def is_empty(self):
        return len(self.data) == 0

    def __len__(self):
        return len(self.data)

    def __repr__(self):
        return repr(self.data[::-1])  

class UndoRedoSystem:
    def __init__(self):
        self.text = ""
        self.undo_stack = []
        self.redo_stack = []

    def type_char(self, ch):
        self.undo_stack.append(self.text)
        self.text += ch
        self.redo_stack.clear()

    def undo(self):
        if self.undo_stack:
            self.redo_stack.append(self.text)
            self.text = self.undo_stack.pop()

    def redo(self):
        if self.redo_stack:
            self.undo_stack.append(self.text)
            self.text = self.redo_stack.pop()

    def get_text(self):
        return self.text


mySys = UndoRedoSystem()
