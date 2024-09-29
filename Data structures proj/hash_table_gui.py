import tkinter as tk
from tkinter import messagebox

class HashTable:
    def __init__(self, size):
        self.size = size
        self.table = [[] for _ in range(size)]  # Initialize a list of empty lists

    def hash_function(self, value):
        return sum(ord(char) for char in value) % self.size

    def add(self, value):
        index = self.hash_function(value)
        # Check for duplicates in the chain
        if value not in self.table[index]:
            self.table[index].append(value)
            return True  # Successfully added
        return False  # Value already exists

    def contains(self, value):
        index = self.hash_function(value)
        return value in self.table[index]

    def delete(self, value):
        index = self.hash_function(value)
        if value in self.table[index]:
            self.table[index].remove(value)
            return True  # Successfully deleted
        return False  # Value not found

    def display(self):
        return "\n".join(f"Index {i}: {chain}" for i, chain in enumerate(self.table) if chain)

class HashSetApp:
    def __init__(self, root):
        self.root = root
        self.root.title("GAUTAM--SHAH---S108")
        self.root.configure(bg='lightyellow')

        self.hash_table = HashTable(10)  # Hash table size of 10

        # Label and Entry for Value
        self.label_value = tk.Label(root, text="Enter String Value:", bg='lightyellow', font=('Arial', 14))
        self.label_value.pack(pady=10)

        self.label_value = tk.Label(root, text="GAUTAM  SHAH S108", bg='lightyellow', font=('Arial', 14))
        self.label_value.pack(pady=10)

        self.entry_value = tk.Entry(root, font=('Arial', 14), width=20)
        self.entry_value.pack(pady=10)

        # Button styling
        button_options = {'padx': 20, 'pady': 10, 'font': ('Arial', 14)}

        self.button_add = tk.Button(root, text="Add", command=self.add_value, **button_options)
        self.button_add.pack(side=tk.LEFT, padx=10)

        self.button_check = tk.Button(root, text="Check", command=self.check_value, **button_options)
        self.button_check.pack(side=tk.LEFT, padx=10)

        self.button_delete = tk.Button(root, text="Delete", command=self.delete_value, **button_options)
        self.button_delete.pack(side=tk.LEFT, padx=10)

        # Text box for output
        self.text_output = tk.Text(root, height=10, width=50, font=('Arial', 14), bg='white')
        self.text_output.pack(pady=20)

    def add_value(self):
        value = self.entry_value.get().strip()
        if value:
            if self.hash_table.add(value):
                messagebox.showinfo("Success", f"Value '{value}' added.")
            else:
                messagebox.showinfo("Error", f"Value '{value}' already exists.")
            self.entry_value.delete(0, tk.END)
            self.display_hash_table()
        else:
            messagebox.showinfo("Error", "Please enter a valid string.")

    def check_value(self):
        value = self.entry_value.get().strip()
        if value:
            if self.hash_table.contains(value):
                messagebox.showinfo("Result", f"Value '{value}' is in the hash table.")
            else:
                messagebox.showinfo("Result", f"Value '{value}' is not in the hash table.")
        else:
            messagebox.showinfo("Error", "Please enter a valid string.")

    def delete_value(self):
        value = self.entry_value.get().strip()
        if value:
            if self.hash_table.delete(value):
                messagebox.showinfo("Success", f"Value '{value}' deleted.")
            else:
                messagebox.showinfo("Error", f"Value '{value}' not found.")
            self.entry_value.delete(0, tk.END)
            self.display_hash_table()
        else:
            messagebox.showinfo("Error", "Please enter a valid string.")

    def display_hash_table(self):
        self.text_output.delete(1.0, tk.END)  # Clear previous output
        output = self.hash_table.display()
        self.text_output.insert(tk.END, "Current Hash Table:\n" + (output if output else "Empty"))

if __name__ == "__main__":
    root = tk.Tk()
    app = HashSetApp(root)
    root.mainloop()
