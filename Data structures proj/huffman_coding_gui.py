import tkinter as tk
from tkinter import scrolledtext, messagebox
import heapq
from collections import Counter

class Node:
    def __init__(self, char=None, freq=None):
        self.char = char
        self.freq = freq
        self.left = None
        self.right = None

    def __lt__(self, other):
        return self.freq < other.freq

def build_huffman_tree(frequencies):
    heap = [Node(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)
    
    while len(heap) > 1:
        left = heapq.heappop(heap)
        right = heapq.heappop(heap)
        merged = Node(freq=left.freq + right.freq)
        merged.left = left
        merged.right = right
        heapq.heappush(heap, merged)
    
    return heap[0]

def generate_codes(node, prefix="", codebook={}):
    if node:
        if node.char is not None:
            codebook[node.char] = prefix
        generate_codes(node.left, prefix + "0", codebook)
        generate_codes(node.right, prefix + "1", codebook)
    return codebook

def huffman_encoding(data):
    if not data:
        return "", {}
    
    frequencies = Counter(data)
    root = build_huffman_tree(frequencies)
    codebook = generate_codes(root)
    encoded_data = ''.join(codebook[char] for char in data)
    
    return encoded_data, codebook

def huffman_decoding(encoded_data, codebook):
    reverse_codebook = {v: k for k, v in codebook.items()}
    decoded_data = ""
    current_code = ""
    
    for bit in encoded_data:
        current_code += bit
        if current_code in reverse_codebook:
            decoded_data += reverse_codebook[current_code]
            current_code = ""
    
    return decoded_data

class HuffmanCodingGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Huffman Coding Visualization")
        self.root.configure(bg="darkgreen")

        self.main_frame = tk.Frame(root, bg="darkgrey")
        self.main_frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.frame_left = tk.Frame(self.main_frame, bg="darkgrey")
        self.frame_left.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        self.label_input = tk.Label(self.frame_left, text="INPUT TEXT:", bg="darkgrey", font=("Arial", 20))
        self.label_input.grid(row=0, column=0, sticky="w", pady=5)

        self.text_input = scrolledtext.ScrolledText(self.frame_left, wrap=tk.WORD, height=4, width=50, borderwidth=2, relief="sunken")
        self.text_input.grid(row=1, column=0, pady=5, padx=10)

        self.button_encode = tk.Button(self.frame_left, text="Encode", command=self.encode_text, bg="red", fg="white")
        self.button_encode.grid(row=2, column=0, pady=5, sticky="ew")

        self.button_decode = tk.Button(self.frame_left, text="Decode", command=self.decode_text, bg="green", fg="white")
        self.button_decode.grid(row=3, column=0, pady=5, sticky="ew")

        self.label_output = tk.Label(self.frame_left, text="Encoded Data:", bg="#e0f7fa", font=("Arial", 20))
        self.label_output.grid(row=4, column=0, sticky="w", pady=5)

        self.text_output = scrolledtext.ScrolledText(self.frame_left, wrap=tk.WORD, height=4, width=50, borderwidth=2, relief="sunken")
        self.text_output.grid(row=5, column=0, pady=5, padx=10)

        self.label_codebook = tk.Label(self.frame_left, text="Codebook (for decoding):", bg="#e0f7fa", font=("Arial", 20))
        self.label_codebook.grid(row=6, column=0, sticky="w", pady=5)

        self.text_codebook = scrolledtext.ScrolledText(self.frame_left, wrap=tk.WORD, height=14, width=50, borderwidth=2, relief="sunken")
        self.text_codebook.grid(row=7, column=0, pady=5, padx=10)

        self.tree_canvas = tk.Canvas(root, bg="#e0f7fa", width=600, height=400, borderwidth=2, relief="sunken")
        self.tree_canvas.grid(row=0, column=1, padx=10, pady=10, rowspan=8, sticky="nsew")
        
        root.grid_rowconfigure(0, weight=1)
        root.grid_columnconfigure(0, weight=1)
        root.grid_columnconfigure(1, weight=2)

    def encode_text(self):
        text = self.text_input.get("1.0", tk.END).strip()
        if not text:
            messagebox.showwarning("Input Error", "Please enter some text to encode.")
            return
        
        encoded_data, codebook = huffman_encoding(text)
        self.text_output.delete("1.0", tk.END)
        self.text_output.insert(tk.END, encoded_data)
        
        self.text_codebook.delete("1.0", tk.END)
        codebook_text = "\n".join(f"{char}: {code}" for char, code in codebook.items())
        self.text_codebook.insert(tk.END, codebook_text)
        self.draw_tree(build_huffman_tree(Counter(text)))

    def decode_text(self):
        encoded_data = self.text_output.get("1.0", tk.END).strip()
        codebook_text = self.text_codebook.get("1.0", tk.END).strip()
        
        if not encoded_data:
            messagebox.showwarning("Input Error", "Please enter encoded data to decode.")
            return
        
        codebook = {}
        if codebook_text:
            for line in codebook_text.splitlines():
                if ":" in line:
                    char, code = line.split(":", 1)
                    codebook[code.strip()] = char.strip()
        
        decoded_data = huffman_decoding(encoded_data, codebook)
        self.text_input.delete("1.0", tk.END)
        self.text_input.insert(tk.END, decoded_data)

    def draw_tree(self, root, x=300, y=20, dx=150, dy=80):
        """Draw Huffman Tree on the canvas."""
        self.tree_canvas.delete("all")

        def draw_node(node, x, y, dx, dy):
            if node:
                # Draw the circular node
                radius = 20
                self.tree_canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="white", outline="black")
                
                # Draw the node's character or frequency
                text_color = "green" if node.char is not None else "red"
                self.tree_canvas.create_text(x, y, text=node.char if node.char is not None else str(node.freq), tags="node", fill=text_color, font=("Arial", 10))

                # Calculate the new position for left and right child nodes
                if node.left:
                    child_x = x - dx
                    child_y = y + dy
                    self.tree_canvas.create_line(x, y + radius, child_x, child_y - radius, tags="line", fill="black")
                    draw_node(node.left, child_x, child_y, dx / 2, dy)
                if node.right:
                    child_x = x + dx
                    child_y = y + dy
                    self.tree_canvas.create_line(x, y + radius, child_x, child_y - radius, tags="line", fill="black")
                    draw_node(node.right, child_x, child_y, dx / 2, dy)

        draw_node(root, x, y, dx, dy)

if __name__ == "__main__":
    root = tk.Tk()
    app = HuffmanCodingGUI(root)
    root.mainloop()
