import tkinter as tk
from tkinter import messagebox

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, data):
        self.items.append(data)

    def pop(self):
        if self.is_empty():
            return None
        return self.items.pop()

    def peek(self):
        if self.is_empty():
            return None
        return self.items[-1]

    def size(self):
        return len(self.items)

class StackGUI:
    def __init__(self, root):
        self.stack = Stack()
        self.root = root
        self.root.title("Stack GUI")
        self.root.configure(bg="#f0f0f0")  # Set background color

        # Make the GUI fill the whole screen
        self.root.geometry("1000x800")  # Set initial size

        self.label = tk.Label(root, text="Enter value to push:", bg="#f0f0f0", font=("Arial", 14))
        self.label.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.entry = tk.Entry(root, font=("Arial", 14), width=30)
        self.entry.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Button styles
        button_style = {'font': ("Arial", 12), 'width': 15, 'height': 1}  # Medium size buttons

        self.push_button = tk.Button(root, text="Push", command=self.push, bg="#4CAF50", fg="white", **button_style)
        self.push_button.grid(row=1, column=0, padx=10, pady=10, sticky="nsew")

        self.pop_button = tk.Button(root, text="Pop", command=self.pop, bg="#FF5722", fg="white", **button_style)
        self.pop_button.grid(row=1, column=1, padx=10, pady=10, sticky="nsew")

        self.peek_button = tk.Button(root, text="Peek", command=self.peek, bg="#2196F3", fg="white", **button_style)
        self.peek_button.grid(row=2, column=0, padx=10, pady=10, sticky="nsew")

        self.size_button = tk.Button(root, text="Size", command=self.size, bg="#FF9800", fg="white", **button_style)
        self.size_button.grid(row=2, column=1, padx=10, pady=10, sticky="nsew")

        self.print_button = tk.Button(root, text="Print Stack", command=self.print_stack, bg="#9C27B0", fg="white", **button_style)
        self.print_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.exit_button = tk.Button(root, text="Exit", command=self.exit_app, bg="#F44336", fg="white", **button_style)
        self.exit_button.grid(row=4, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        self.output = tk.Text(root, height=20, font=("Arial", 12))  # Increased height for output box
        self.output.grid(row=5, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

        # Configure grid to expand
        for i in range(6):
            root.grid_rowconfigure(i, weight=1)
            root.grid_columnconfigure(i, weight=1)

    def push(self):
        value = self.entry.get()
        if value:
            self.stack.push(value)
            self.entry.delete(0, tk.END)
            self.output.insert(tk.END, f"Pushed: {value}\n")
        else:
            messagebox.showerror("Error", "Please enter a value")

    def pop(self):
        value = self.stack.pop()
        if value is not None:
            self.output.insert(tk.END, f"Popped: {value}\n")
        else:
            messagebox.showerror("Error", "Stack is empty")

    def peek(self):
        value = self.stack.peek()
        if value is not None:
            self.output.insert(tk.END, f"Peek: {value}\n")
        else:
            messagebox.showerror("Error", "Stack is empty")

    def size(self):
        size = self.stack.size()
        self.output.insert(tk.END, f"Stack size: {size}\n")

    def print_stack(self):
        self.output.insert(tk.END, "Stack elements:\n")
        if self.stack.is_empty():
            self.output.insert(tk.END, "The stack is empty.\n")
        else:
            for item in self.stack.items[::-1]:
                self.output.insert(tk.END, f"{item}\n")

    def exit_app(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    gui = StackGUI(root)
    root.mainloop()
