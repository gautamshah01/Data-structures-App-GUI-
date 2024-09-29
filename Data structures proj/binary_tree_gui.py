import tkinter as tk
from tkinter import messagebox, scrolledtext

class TreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self):
        self.root = None

    def insert(self, value):
        if not self.root:
            self.root = TreeNode(value)
        else:
            self._insert_recursive(self.root, value)

    def _insert_recursive(self, node, value):
        if value < node.value:
            if node.left is None:
                node.left = TreeNode(value)
            else:
                self._insert_recursive(node.left, value)
        else:
            if node.right is None:
                node.right = TreeNode(value)
            else:
                self._insert_recursive(node.right, value)

    def preorder(self, node, visit):
        if node:
            visit(node.value)
            self.preorder(node.left, visit)
            self.preorder(node.right, visit)

    def inorder(self, node, visit):
        if node:
            self.inorder(node.left, visit)
            visit(node.value)
            self.inorder(node.right, visit)

    def postorder(self, node, visit):
        if node:
            self.postorder(node.left, visit)
            self.postorder(node.right, visit)
            visit(node.value)

class BinaryTreeGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("Binary Tree GUI")
        self.master.geometry("800x550")

        # Main frame
        self.main_frame = tk.Frame(master)
        self.main_frame.pack(pady=20)

        # Canvas for tree graph
        self.canvas = tk.Canvas(self.main_frame, bg="#f0f0f0", width=800, height=400)
        self.canvas.pack()

        # Frame for user input
        self.input_frame = tk.Frame(master)
        self.input_frame.pack()

        # Label for user instructions
        self.label = tk.Label(self.input_frame, text="Enter an integer or string:", font=("Arial", 12))
        self.label.pack(pady=10)

        # Entry for user input
        self.entry = tk.Entry(self.input_frame, font=("Arial", 14))
        self.entry.pack(pady=10)

        # Buttons for inserting values
        self.int_button = tk.Button(self.input_frame, text="Insert Integer", command=self.add_integer, bg="#4CAF50", fg="white", font=("Arial", 14), width=15)
        self.int_button.pack(side=tk.LEFT, padx=5)

        self.str_button = tk.Button(self.input_frame, text="Insert String", command=self.add_string, bg="#2196F3", fg="white", font=("Arial", 14), width=15)
        self.str_button.pack(side=tk.LEFT, padx=5)

        # Frame for traversal buttons
        self.button_frame = tk.Frame(master)
        self.button_frame.pack(pady=10)

        # Buttons for traversals
        self.preorder_button = tk.Button(self.button_frame, text="Preorder", command=self.preorder_traversal, bg="#FF9800", fg="white", font=("Arial", 14), width=10)
        self.preorder_button.pack(side=tk.LEFT, padx=5)

        self.inorder_button = tk.Button(self.button_frame, text="Inorder", command=self.inorder_traversal, bg="#FF9800", fg="white", font=("Arial", 14), width=10)
        self.inorder_button.pack(side=tk.LEFT, padx=5)

        self.postorder_button = tk.Button(self.button_frame, text="Postorder", command=self.postorder_traversal, bg="#FF9800", fg="white", font=("Arial", 14), width=10)
        self.postorder_button.pack(side=tk.LEFT, padx=5)

        # Clear button
        self.clear_button = tk.Button(self.button_frame, text="Clear", command=self.clear_tree, bg="#F44336", fg="white", font=("Arial", 14), width=10)
        self.clear_button.pack(side=tk.LEFT, padx=5)

        # Frame for traversal output
        self.output_frame = tk.Frame(master)
        self.output_frame.pack(pady=10)

        self.output_label = tk.Label(self.output_frame, text="Traversal Output:", font=("Arial", 12))
        self.output_label.pack()

        # Scrolled text for displaying traversal results
        self.output_text = scrolledtext.ScrolledText(self.output_frame, width=80, height=10, font=("Arial", 10), wrap=tk.WORD)
        self.output_text.pack()

        self.tree = BinaryTree()

    def insert_and_draw(self, value):
        self.tree.insert(value)
        self.redraw_tree()

    def redraw_tree(self):
        self.canvas.delete("all")
        self.output_text.delete(1.0, tk.END)  # Clear previous output
        self.draw_tree(self.tree.root, 400, 30, 200)

    def draw_tree(self, node, x, y, x_offset):
        if node:
            # Draw the node
            self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="#4CAF50")
            self.canvas.create_text(x, y, text=str(node.value), font=("Arial", 10))
            # Draw left child
            if node.left:
                self.canvas.create_line(x, y + 20, x - x_offset, y + 80)
                self.draw_tree(node.left, x - x_offset, y + 80, x_offset // 2)
            # Draw right child
            if node.right:
                self.canvas.create_line(x, y + 20, x + x_offset, y + 80)
                self.draw_tree(node.right, x + x_offset, y + 80, x_offset // 2)

    def perform_traversal(self, order):
        traversal_result = []
        if order == 'preorder':
            self.tree.preorder(self.tree.root, traversal_result.append)
        elif order == 'inorder':
            self.tree.inorder(self.tree.root, traversal_result.append)
        elif order == 'postorder':
            self.tree.postorder(self.tree.root, traversal_result.append)
        
        self.show_traversal_result(traversal_result)

    def show_traversal_result(self, result):
        result_str = ' -> '.join(map(str, result))
        self.output_text.delete(1.0, tk.END)  # Clear previous output
        self.output_text.insert(tk.END, result_str)

    def add_integer(self):
        value = self.entry.get()
        if value.isdigit():
            self.insert_and_draw(int(value))
            self.entry.delete(0, tk.END)
        else:
            messagebox.showerror("Invalid Input", "Please enter a valid integer.")

    def add_string(self):
        value = self.entry.get()
        if value:
            self.insert_and_draw(value)
            self.entry.delete(0, tk.END)
        else:
            messagebox.showerror("Invalid Input", "Please enter a valid string.")

    def preorder_traversal(self):
        self.perform_traversal('preorder')

    def inorder_traversal(self):
        self.perform_traversal('inorder')

    def postorder_traversal(self):
        self.perform_traversal('postorder')

    def clear_tree(self):
        self.tree = BinaryTree()
        self.canvas.delete("all")
        self.output_text.delete(1.0, tk.END)  # Clear output
        self.entry.delete(0, tk.END)  # Clear entry

if __name__ == "__main__":
    root = tk.Tk()
    gui = BinaryTreeGUI(root)
    root.mainloop()
