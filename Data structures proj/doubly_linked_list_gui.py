import tkinter as tk
from tkinter import messagebox

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def is_empty(self):
        return self.head is None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node

    def delete_at_beginning(self):
        if self.is_empty():
            return None
        deleted_node = self.head
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
        return deleted_node.data

    def delete_at_end(self):
        if self.is_empty():
            return None
        deleted_node = self.tail
        if self.head == self.tail:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
        return deleted_node.data

    def traverse(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

class DoublyLinkedListGUI:
    def __init__(self, root):
        self.linked_list = DoublyLinkedList()
        self.root = root
        self.root.title("Doubly Linked List GUI")

        # Set background color
        self.root.configure(bg="#f0f0f0")

        self.label = tk.Label(root, text="Enter value:", bg="#f0f0f0", font=("Arial", 14))
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, font=("Arial", 14), width=30)
        self.entry.pack(pady=10)

        # Create buttons with improved styling
        button_style = {'font': ("Arial", 12), 'width': 20, 'height': 2}

        self.insert_begin_button = tk.Button(root, text="Insert at Beginning", command=self.insert_at_beginning, bg="#4CAF50", fg="white", **button_style)
        self.insert_begin_button.pack(pady=5)

        self.insert_end_button = tk.Button(root, text="Insert at End", command=self.insert_at_end, bg="#2196F3", fg="white", **button_style)
        self.insert_end_button.pack(pady=5)

        self.delete_begin_button = tk.Button(root, text="Delete at Beginning", command=self.delete_at_beginning, bg="darkred", fg="white", **button_style)
        self.delete_begin_button.pack(pady=5)

        self.delete_end_button = tk.Button(root, text="Delete at End", command=self.delete_at_end, bg="red", fg="white", **button_style)
        self.delete_end_button.pack(pady=5)

        self.traverse_button = tk.Button(root, text="Traverse", command=self.traverse, bg="#9C27B0", fg="white", **button_style)
        self.traverse_button.pack(pady=5)

        self.output = tk.Text(root, height=10, width=50, font=("Arial", 12))
        self.output.pack(pady=10)

    def insert_at_beginning(self):
        value = self.entry.get()
        if value:
            self.linked_list.insert_at_beginning(value)
            self.entry.delete(0, tk.END)
            self.output.insert(tk.END, f"Inserted at beginning: {value}\n")
        else:
            messagebox.showerror("Error", "Please enter a value")

    def insert_at_end(self):
        value = self.entry.get()
        if value:
            self.linked_list.insert_at_end(value)
            self.entry.delete(0, tk.END)
            self.output.insert(tk.END, f"Inserted at end: {value}\n")
        else:
            messagebox.showerror("Error", "Please enter a value")

    def delete_at_beginning(self):
        value = self.linked_list.delete_at_beginning()
        if value is not None:
            self.output.insert(tk.END, f"Deleted from beginning: {value}\n")
        else:
            messagebox.showerror("Error", "Doubly linked list is empty")

    def delete_at_end(self):
        value = self.linked_list.delete_at_end()
        if value is not None:
            self.output.insert(tk.END, f"Deleted from end: {value}\n")
        else:
            messagebox.showerror("Error", "Doubly linked list is empty")

    def traverse(self):
        elements = self.linked_list.traverse()
        self.output.insert(tk.END, "Doubly linked list elements: " + " <-> ".join(map(str, elements)) + " <-> None\n")

if __name__ == "__main__":
    root = tk.Tk()
    gui = DoublyLinkedListGUI(root)
    root.mainloop()
