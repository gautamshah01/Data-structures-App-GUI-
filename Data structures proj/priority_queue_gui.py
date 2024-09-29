    
import tkinter as tk  
from tkinter import messagebox  
  
class PriorityQueue:  
    def __init__(self):  
        self.queue = []  
  
    def is_empty(self):  
        return len(self.queue) == 0  
  
    def enqueue(self, item, priority):  
        self.queue.append((item, priority))  
        self.queue.sort(key=lambda x: x[1])  # Sort by priority  
  
    def dequeue(self):  
        if self.is_empty():  
            return None  
        return self.queue.pop(0)[0]  
  
    def traverse(self):  
        return self.queue  
  
class PriorityQueueGUI:  
    def __init__(self, root):  
        self.root = root  
        self.root.title("Priority Queue GUI")  
  
        self.pq = PriorityQueue()  
  
        self.create_widgets()  
  
    def create_widgets(self):  
        # Create frame for controls  
        control_frame = tk.Frame(self.root, bg="lightblue", padx=10, pady=10)  
        control_frame.pack(padx=20, pady=20, fill=tk.X)  
  
        # Enqueue section  
        tk.Label(control_frame, text="Item:", bg="lightblue").grid(row=0, column=0, sticky=tk.W)  
        self.item_entry = tk.Entry(control_frame)  
        self.item_entry.grid(row=0, column=1, padx=5, pady=5)  
  
        tk.Label(control_frame, text="Priority:", bg="lightblue").grid(row=1, column=0, sticky=tk.W)  
        self.priority_entry = tk.Entry(control_frame)  
        self.priority_entry.grid(row=1, column=1, padx=5, pady=5)  
  
        tk.Button(control_frame, text="Enqueue", command=self.enqueue_item, bg="lightgreen").grid(row=2,
 column=0, columnspan=2, pady=10)  
  
        # Dequeue section  
        tk.Button(control_frame, text="Dequeue", command=self.dequeue_item, bg="lightcoral").grid(row=3, 
column=0, columnspan=2, pady=10)  
  
        # Traverse section  
        tk.Button(control_frame, text="Traverse", command=self.traverse_queue, 
bg="lightyellow").grid(row=4, column=0, columnspan=2, pady=10)  
  
        # Text area for display  
        self.text_area = tk.Text(self.root, height=10, width=40, bg="lightgray")  
        self.text_area.pack(padx=20, pady=10)  
  
    def enqueue_item(self):  
        item = self.item_entry.get()  
        priority = self.priority_entry.get()  
  
        if not item or not priority.isdigit():  
            messagebox.showwarning("Input Error", "Please enter a valid item and priority.")  
            return  
  
        priority = int(priority)  
        self.pq.enqueue(item, priority)  
        self.item_entry.delete(0, tk.END)  
        self.priority_entry.delete(0, tk.END)  
        self.update_text_area("Item enqueued successfully.")  
  
    def dequeue_item(self):  
        item = self.pq.dequeue()  
        if item is None:  
            self.update_text_area("Priority Queue is empty.")  
        else:  
            self.update_text_area(f"Dequeued: {item}")  
  
    def traverse_queue(self):  
        queue_contents = self.pq.traverse()  
        if not queue_contents:  
            self.update_text_area("Priority Queue is empty.")  
        else:  
            output = "Priority Queue contains:\n"  
            for item, priority in queue_contents:  
                output += f"Item: {item}, Priority: {priority}\n"  
            self.update_text_area(output)  
  
    def update_text_area(self, message):  
        self.text_area.delete(1.0, tk.END)  
        self.text_area.insert(tk.END, message)  
  
if __name__ == "__main__":  
    root = tk.Tk()  
    app = PriorityQueueGUI(root)  
    root.mainloop()  
