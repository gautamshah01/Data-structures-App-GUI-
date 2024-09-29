import tkinter as tk
from tkinter import ttk, font
from tkinter import messagebox
from PIL import Image, ImageTk

# Import the GUI classes for different data structures (unchanged)
from stack_gui import StackGUI
from queue_gui import QueueGUI
from priority_queue_gui import PriorityQueueGUI
from linked_list_gui import LinkedListGUI
from doubly_linked_list_gui import DoublyLinkedListGUI
from binary_tree_gui import BinaryTreeGUI
from huffman_coding_gui import HuffmanCodingGUI
from graph_gui import GraphGUI
from hash_table_gui import HashSetApp
from travelling_salesman_problem import TSPApp

class MainGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Data Structures App")

        # Set the GUI to full screen
        self.root.attributes('-fullscreen', True)

        # Set color scheme
        self.bg_color = "#2c3e50"
        self.accent_color = "#3498db"
        self.text_color = "#ecf0f1"
        self.button_color = "#34495e"
        self.hover_color = "green"

        # Use a custom font
        self.custom_font = font.Font(family="Helvetica", size=12)
        self.title_font = font.Font(family="Helvetica", size=24, weight="bold")

        # Configure styles
        self.style = ttk.Style()
        self.style.theme_use('clam')
        self.style.configure("TButton", 
                             padding=10, 
                             relief="flat", 
                             background=self.button_color, 
                             foreground=self.text_color,
                             font=self.custom_font)
        self.style.map("TButton", 
                       background=[('active', self.hover_color)])
        
        self.style.configure("TFrame", background=self.bg_color)
        self.style.configure("TLabel", 
                             background=self.bg_color, 
                             foreground=self.text_color,
                             font=self.custom_font)

        self.start_screen()

    def start_screen(self):
        self.clear_window()

        # Load and resize background image
        self.bg_image = Image.open("background.jpg")
        self.bg_image = self.bg_image.resize((self.root.winfo_screenwidth(), self.root.winfo_screenheight()), Image.Resampling.LANCZOS)
        self.bg_photo = ImageTk.PhotoImage(self.bg_image)

        background_label = tk.Label(self.root, image=self.bg_photo)
        background_label.place(x=0, y=0, relwidth=1, relheight=1)

        # Welcome message
        welcome_label = ttk.Label(self.root, text="Data Structures App", font=self.title_font, foreground=self.text_color)
        welcome_label.pack(pady=40)

        # Start button
        start_button = ttk.Button(self.root, text="Start", command=self.open_main_gui, style="TButton")
        start_button.pack(pady=20)

        # Exit button
        exit_button = ttk.Button(self.root, text="Exit", command=self.exit_app, style="TButton")
        exit_button.pack(pady=10)

    def open_main_gui(self):
        self.clear_window()
        self.create_sidebar()
        self.create_main_content()

    def create_sidebar(self):
        sidebar = ttk.Frame(self.root, style="TFrame", width=200)
        sidebar.pack(side="left", fill="y")

        logo_label = ttk.Label(sidebar, text="Data Structures", font=self.title_font, foreground=self.text_color)
        logo_label.pack(pady=20)
    

        buttons_info = [
            ("Stack", self.open_stack_gui),
            ("Queue", self.open_queue_gui),
            ("Priority Queue", self.open_priority_queue_gui),
            ("Linked List", self.open_linked_list_gui),
            ("Doubly Linked List", self.open_doubly_linked_list_gui),
            ("Binary Tree", self.open_binary_tree_gui),
            ("Huffman Coding", self.open_huffman_coding_gui),
            ("Graph", self.open_graph_gui),
            ("TSP", self.open_tsp_gui),
            ("Hashing", self.open_hash_table_gui)
        ]

        for text, command in buttons_info:
            button = ttk.Button(sidebar, text=text, command=command, style="TButton")
            button.pack(pady=5, padx=10, fill="x")

        exit_button = ttk.Button(sidebar, text="Exit", command=self.exit_app, style="TButton")
        exit_button.pack(pady=10)
            
            
    def create_main_content(self):
        main_frame = ttk.Frame(self.root, style="TFrame")
        main_frame.pack(side="right", fill="both", expand=True)

        title_label = ttk.Label(main_frame, text="Welcome to Data Structures App", font=self.title_font, foreground=self.text_color)
        title_label.pack(pady=20)

        info_text = "Select a data structure from the sidebar to begin."
        info_label = ttk.Label(main_frame, text=info_text, foreground=self.text_color)
        info_label.pack(pady=10)

    def clear_window(self):
        for widget in self.root.winfo_children():
            widget.destroy()

    def exit_app(self):
        if messagebox.askyesno("Exit", "Are you sure you want to exit?"):
            self.root.destroy()

    def open_stack_gui(self):
        self.open_toplevel(StackGUI)
    
    def open_queue_gui(self):
        self.open_toplevel(QueueGUI)

    def open_priority_queue_gui(self):
        self.open_toplevel(PriorityQueueGUI)

    def open_linked_list_gui(self):
        self.open_toplevel(LinkedListGUI)

    def open_doubly_linked_list_gui(self):
        self.open_toplevel(DoublyLinkedListGUI)

    def open_binary_tree_gui(self):
        self.open_toplevel(BinaryTreeGUI)

    def open_huffman_coding_gui(self):
        self.open_toplevel(HuffmanCodingGUI)

    def open_graph_gui(self):
        self.open_toplevel(GraphGUI)

    def open_hash_table_gui(self):
        self.open_toplevel(HashSetApp)

    def open_tsp_gui(self):
        self.open_toplevel(TSPApp)

    # Other methods (open_stack_gui, open_queue_gui, etc.) remain the same

    def open_toplevel(self, gui_class):
        top = tk.Toplevel(self.root)
        gui_class(top)
        top.grab_set()

if __name__ == "__main__":
    root = tk.Tk()
    root.configure(bg="#2c3e50")  # Set background color for the root window
    app =MainGUI(root)
    root.mainloop()
