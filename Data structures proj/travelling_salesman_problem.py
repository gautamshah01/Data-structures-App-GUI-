import numpy as np
import matplotlib.pyplot as plt
from scipy.spatial import distance
from itertools import permutations
import tkinter as tk
from tkinter import messagebox

class TSPApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Traveling Salesman Problem Solver")
        
        # Set a colorful background
        self.root.configure(bg='lightblue')

        self.points = []

        # Create a larger canvas
        self.canvas = tk.Canvas(root, width=800, height=600, bg="white")
        self.canvas.pack(pady=20)

        # Button styling
        button_options = {'padx': 20, 'pady': 10, 'font': ('Arial', 14)}

        self.button_add = tk.Button(root, text="Add Point", command=self.add_point, **button_options)
        self.button_add.pack(side=tk.LEFT, padx=10)

        self.button_solve = tk.Button(root, text="Solve TSP", command=self.solve_tsp, **button_options)
        self.button_solve.pack(side=tk.LEFT, padx=10)

        self.button_clear = tk.Button(root, text="Clear Points", command=self.clear_points, **button_options)
        self.button_clear.pack(side=tk.LEFT, padx=10)

        self.label_info = tk.Label(root, text="", bg='lightblue', font=('Arial', 12))
        self.label_info.pack(pady=10)

    def add_point(self):
        x = np.random.randint(50, 750)
        y = np.random.randint(50, 550)
        self.points.append((x, y))
        self.draw_point(x, y)
        self.label_info.config(text=f"Added Point: ({x}, {y})")

    def draw_point(self, x, y):
        radius = 8  # Increase radius for better visibility
        self.canvas.create_oval(x - radius, y - radius, x + radius, y + radius, fill="blue")

    def clear_points(self):
        self.canvas.delete("all")
        self.points.clear()
        self.label_info.config(text="")

    def solve_tsp(self):
        if len(self.points) < 2:
            messagebox.showinfo("Error", "Add at least 2 points.")
            return

        num_points = len(self.points)
        distance_matrix = np.zeros((num_points, num_points))

        # Create distance matrix
        for i in range(num_points):
            for j in range(num_points):
                distance_matrix[i][j] = distance.euclidean(self.points[i], self.points[j])

        # Solve TSP using brute force
        min_path = None
        min_distance = float('inf')

        for perm in permutations(range(num_points)):
            current_distance = sum(distance_matrix[perm[i], perm[i + 1]] for i in range(num_points - 1))
            current_distance += distance_matrix[perm[-1], perm[0]]  # Return to start

            if current_distance < min_distance:
                min_distance = current_distance
                min_path = perm

        self.draw_solution(min_path)
        self.label_info.config(text=f"Optimal Distance: {min_distance:.2f}")

    def draw_solution(self, path):
        for i in range(len(path)):
            start = self.points[path[i]]
            end = self.points[path[(i + 1) % len(path)]]
            self.canvas.create_line(start, end, fill="red", width=3)

if __name__ == "__main__":
    root = tk.Tk()
    app = TSPApp(root)
    root.mainloop()
