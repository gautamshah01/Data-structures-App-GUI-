import tkinter as tk
from tkinter import messagebox

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def is_empty(self):
        return self.head is None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.is_empty():
            self.head = new_node
            return
        current = self.head
        while current.next:
            current = current.next
        current.next = new_node

    def delete_at_beginning(self):
        if self.is_empty():
            return None
        deleted_node = self.head
        self.head = self.head.next
        return deleted_node.data

    def delete_at_end(self):
        if self.is_empty():
            return None
        if self.head.next is None:
            deleted_node = self.head
            self.head = None
            return deleted_node.data
        current = self.head
        while current.next.next:
            current = current.next
        deleted_node = current.next
        current.next = None
        return deleted_node.data

    def traverse(self):
        elements = []
        current = self.head
        while current:
            elements.append(current.data)
            current = current.next
        return elements

class LinkedListGUI:
    def __init__(self, root):
        self.linked_list = LinkedList()
        self.root = root
        self.root.title("Linked List GUI")
        self.root.configure(bg="#f0f0f0")  # Set background color

        self.label = tk.Label(root, text="Enter value:", bg="#f0f0f0", font=("Arial", 14))
        self.label.pack(pady=10)

        self.entry = tk.Entry(root, font=("Arial", 14), width=30)
        self.entry.pack(pady=10)

        # Button styles
        button_style = {'font': ("Arial", 12), 'width': 20, 'height': 2}

        self.insert_begin_button = tk.Button(root, text="Insert at Beginning", command=self.insert_at_beginning,
                                              bg="#4CAF50", fg="white", **button_style)
        self.insert_begin_button.pack(pady=5)

        self.insert_end_button = tk.Button(root, text="Insert at End", command=self.insert_at_end,
                                            bg="#2196F3", fg="white", **button_style)
        self.insert_end_button.pack(pady=5)

        self.delete_begin_button = tk.Button(root, text="Delete at Beginning", command=self.delete_at_beginning,
                                              bg="#FF5722", fg="white", **button_style)
        self.delete_begin_button.pack(pady=5)

        self.delete_end_button = tk.Button(root, text="Delete at End", command=self.delete_at_end,
                                            bg="#FF9800", fg="white", **button_style)
        self.delete_end_button.pack(pady=5)

        self.traverse_button = tk.Button(root, text="Traverse", command=self.traverse,
                                          bg="#9C27B0", fg="white", **button_style)
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
            messagebox.showerror("Error", "Linked list is empty")

    def delete_at_end(self):
        value = self.linked_list.delete_at_end()
        if value is not None:
            self.output.insert(tk.END, f"Deleted from end: {value}\n")
        else:
            messagebox.showerror("Error", "Linked list is empty")

    def traverse(self):
        elements = self.linked_list.traverse()
        self.output.insert(tk.END, "Linked list elements: " + " -> ".join(elements) + " -> None\n")

if __name__ == "__main__":
    root = tk.Tk()
    gui = LinkedListGUI(root)
    root.mainloop()
