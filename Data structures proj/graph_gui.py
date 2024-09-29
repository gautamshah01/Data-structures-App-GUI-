import tkinter as tk
from tkinter import simpledialog, messagebox
import random
from collections import deque

class Graph:
    def __init__(self):
        self.graph = {}

    def add_vertex(self, vertex):
        if vertex not in self.graph:
            self.graph[vertex] = []

    def remove_vertex(self, vertex):
        if vertex in self.graph:
            for adjacent in self.graph[vertex]:
                self.graph[adjacent].remove(vertex)
            del self.graph[vertex]

    def add_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            if vertex2 not in self.graph[vertex1]:
                self.graph[vertex1].append(vertex2)
            if vertex1 not in self.graph[vertex2]:
                self.graph[vertex2].append(vertex1)

    def remove_edge(self, vertex1, vertex2):
        if vertex1 in self.graph and vertex2 in self.graph:
            if vertex2 in self.graph[vertex1]:
                self.graph[vertex1].remove(vertex2)
            if vertex1 in self.graph[vertex2]:
                self.graph[vertex2].remove(vertex1)

    def bfs(self, start_vertex):
        visited = set()
        queue = deque([start_vertex])
        bfs_order = []

        while queue:
            vertex = queue.popleft()
            if vertex not in visited:
                visited.add(vertex)
                bfs_order.append(vertex)
                queue.extend(neighbor for neighbor in self.graph[vertex] if neighbor not in visited)
        
        return bfs_order

    def dfs(self, start_vertex):
        visited = set()
        dfs_order = []

        def dfs_helper(vertex):
            visited.add(vertex)
            dfs_order.append(vertex)
            for neighbor in self.graph[vertex]:
                if neighbor not in visited:
                    dfs_helper(neighbor)

        dfs_helper(start_vertex)
        return dfs_order

    def get_edges(self):
        edges = []
        for vertex, neighbors in self.graph.items():
            for neighbor in neighbors:
                if (neighbor, vertex) not in edges:  # Avoid duplicate edges
                    edges.append((vertex, neighbor))
        return edges

    def get_nodes(self):
        return list(self.graph.keys())

class GraphGUI:
    def __init__(self, root):
        self.root = root
        self.root.title("Graph Data Structure")
        self.root.configure(bg="#2E8B57")

        self.graph = Graph()
        self.vertices = {}
        self.canvas_width = 800
        self.canvas_height = 600

        # Title label
        self.label = tk.Label(root, text="Graph Operations", font=("Arial", 16, "bold"), bg="#2E8B57", fg="white")
        self.label.pack(fill=tk.X)

        # Buttons
        self.button_frame = tk.Frame(root, bg="#2E8B57")
        self.button_frame.pack(pady=10)

        self.add_vertex_button = tk.Button(self.button_frame, text="Add Vertex", command=self.add_vertex, bg="#4682B4", fg="white", font=("Arial", 12, "bold"))
        self.add_vertex_button.grid(row=0, column=0, padx=5)

        self.add_edge_button = tk.Button(self.button_frame, text="Add Edge", command=self.add_edge, bg="#4682B4", fg="white", font=("Arial", 12, "bold"))
        self.add_edge_button.grid(row=0, column=1, padx=5)

        self.remove_edge_button = tk.Button(self.button_frame, text="Remove Edge", command=self.remove_edge, bg="#4682B4", fg="white", font=("Arial", 12, "bold"))
        self.remove_edge_button.grid(row=0, column=2, padx=5)

        self.remove_vertex_button = tk.Button(self.button_frame, text="Remove Vertex", command=self.remove_vertex, bg="#4682B4", fg="white", font=("Arial", 12, "bold"))
        self.remove_vertex_button.grid(row=0, column=3, padx=5)

        self.bfs_button = tk.Button(self.button_frame, text="BFS", command=self.bfs, bg="#4682B4", fg="white", font=("Arial", 12, "bold"))
        self.bfs_button.grid(row=0, column=4, padx=5)

        self.dfs_button = tk.Button(self.button_frame, text="DFS", command=self.dfs, bg="#4682B4", fg="white", font=("Arial", 12, "bold"))
        self.dfs_button.grid(row=0, column=5, padx=5)

        # Canvas for drawing the graph
        self.canvas = tk.Canvas(root, width=self.canvas_width, height=self.canvas_height, bg="black")
        self.canvas.pack(fill=tk.BOTH, expand=True)

    def add_vertex(self):
        vertex = simpledialog.askstring("Input", "Enter vertex:")
        if vertex:
            self.graph.add_vertex(vertex)
            self.vertices[vertex] = (random.randint(50, self.canvas_width - 50), random.randint(50, self.canvas_height - 50))
            self.display_graph()

    def add_edge(self):
        vertex1 = simpledialog.askstring("Input", "Enter the first vertex of the edge:")
        vertex2 = simpledialog.askstring("Input", "Enter the second vertex of the edge:")
        if vertex1 and vertex2:
            self.graph.add_edge(vertex1, vertex2)
            self.display_graph()

    def remove_edge(self):
        vertex1 = simpledialog.askstring("Input", "Enter the first vertex of the edge to remove:")
        vertex2 = simpledialog.askstring("Input", "Enter the second vertex of the edge to remove:")
        if vertex1 and vertex2:
            self.graph.remove_edge(vertex1, vertex2)
            self.display_graph()

    def remove_vertex(self):
        vertex = simpledialog.askstring("Input", "Enter the vertex to remove:")
        if vertex:
            self.graph.remove_vertex(vertex)
            if vertex in self.vertices:
                del self.vertices[vertex]
            self.display_graph()

    def bfs(self):
        start_vertex = simpledialog.askstring("Input", "Enter starting vertex for BFS:")
        if start_vertex and start_vertex in self.graph.get_nodes():
            bfs_order = self.graph.bfs(start_vertex)
            messagebox.showinfo("BFS Order", " -> ".join(bfs_order))
        else:
            messagebox.showwarning("Warning", "Vertex not found!")

    def dfs(self):
        start_vertex = simpledialog.askstring("Input", "Enter starting vertex for DFS:")
        if start_vertex and start_vertex in self.graph.get_nodes():
            dfs_order = self.graph.dfs(start_vertex)
            messagebox.showinfo("DFS Order", " -> ".join(dfs_order))
        else:
            messagebox.showwarning("Warning", "Vertex not found!")

    def display_graph(self):
        self.canvas.delete("all")

        # Draw edges
        for vertex1, vertex2 in self.graph.get_edges():
            if vertex1 in self.vertices and vertex2 in self.vertices:
                x1, y1 = self.vertices[vertex1]
                x2, y2 = self.vertices[vertex2]
                self.canvas.create_line(x1, y1, x2, y2, fill="#4682B4", width=2)

        # Draw vertices
        for vertex, (x, y) in self.vertices.items():
            self.canvas.create_oval(x - 20, y - 20, x + 20, y + 20, fill="#87CEFA", outline="#4682B4", width=2)
            self.canvas.create_text(x, y, text=vertex, font=("Arial", 12, "bold"), fill="#00008B")

if __name__ == "__main__":
    root = tk.Tk()
    app = GraphGUI(root)
    root.mainloop()
