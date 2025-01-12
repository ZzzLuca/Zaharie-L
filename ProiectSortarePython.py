import tkinter as tk
import random
import threading
import time


class SortingVisualizer:
    def __init__(self, root):
        self.root = root
        self.root.title("Vizualizator Algoritmi de Sortare")
        self.root.geometry("1366x768")  # Set window size to 1366x768
        self.root.resizable(True, True)  # Make the window resizable

        self.arr = []
        self.bars = []
        self.algorithm = None
        self.speed = 0.05  # Default speed
        self.is_paused = False
        self.is_sorting = False

        self.create_widgets()
        self.create_bars()

    def create_widgets(self):
        # Create a frame for the controls to keep them grouped together
        control_frame = tk.Frame(self.root)
        control_frame.grid(row=0, column=0, padx=20, pady=20, sticky="ns")

        self.algorithm_label = tk.Label(control_frame, text="Alege un algoritm de sortare:")
        self.algorithm_label.grid(row=0, column=0, pady=5)

        self.algorithm_var = tk.StringVar(value="Bubble Sort")
        self.algorithm_menu = tk.OptionMenu(control_frame, self.algorithm_var, "Bubble Sort", "Insertion Sort",
                                            "Selection Sort")
        self.algorithm_menu.grid(row=1, column=0, pady=5)

        self.size_label = tk.Label(control_frame, text="Numar elemente:")
        self.size_label.grid(row=2, column=0, pady=5)

        self.size_slider = tk.Scale(control_frame, from_=10, to=100, orient="horizontal")
        self.size_slider.set(50)
        self.size_slider.grid(row=3, column=0, pady=5)

        self.randomize_button = tk.Button(control_frame, text="Randomizează", command=self.randomize)
        self.randomize_button.grid(row=4, column=0, pady=5)

        self.start_button = tk.Button(control_frame, text="Începe sortarea", command=self.start_sorting)
        self.start_button.grid(row=5, column=0, pady=5)

        self.pause_button = tk.Button(control_frame, text="Pauză", command=self.toggle_pause)
        self.pause_button.grid(row=6, column=0, pady=5)

        self.reset_button = tk.Button(control_frame, text="Resetează", command=self.reset)
        self.reset_button.grid(row=7, column=0, pady=5)

        self.quit_button = tk.Button(control_frame, text="Ieșire", command=self.root.quit)
        self.quit_button.grid(row=8, column=0, pady=5)

        # Create a label for the speed slider
        self.speed_label = tk.Label(control_frame, text="Viteză sortare:")
        self.speed_label.grid(row=9, column=0, pady=5)

        # Create a slider for speed adjustment (from 0.01 to 1.0)
        self.speed_slider = tk.Scale(control_frame, from_=0.01, to=1.0, resolution=0.01, orient="horizontal")
        self.speed_slider.set(self.speed)
        self.speed_slider.grid(row=10, column=0, pady=5)

        # Create a Canvas to hold the bars (increased canvas width and height)
        self.canvas = tk.Canvas(self.root, width=1100, height=600, bg='white')
        self.canvas.grid(row=0, column=1, padx=20, pady=20, rowspan=9, sticky="nsew")

    def create_bars(self):
        # Initialize the array with random values
        self.arr = [random.randint(50, 600) for _ in range(self.size_slider.get())]
        self.bars = []

        # Draw the bars as rectangles on the canvas with the default color set to green
        for i in range(len(self.arr)):
            bar = self.canvas.create_rectangle(i * 25, 600 - self.arr[i], (i * 25) + 20, 600,
                                               fill='green')  # Default color green
            self.bars.append(bar)

    def update_bars(self, arr, highlighted_bars=None):
        # Update the position and size of the bars on the canvas
        for i, bar in enumerate(self.bars):
            if highlighted_bars and i in highlighted_bars:
                self.canvas.itemconfig(bar, fill='pink')  # Highlight the bar as pink
            else:
                self.canvas.itemconfig(bar, fill='green')  # Reset color to green
            self.canvas.coords(bar, i * 25, 600 - arr[i], (i * 25) + 20, 600)

    def randomize(self):
        self.arr = [random.randint(50, 600) for _ in range(self.size_slider.get())]
        self.update_bars(self.arr)

    def start_sorting(self):
        if not self.is_sorting:
            self.is_sorting = True
            self.algorithm = self.algorithm_var.get()
            # Get the current speed value from the speed slider
            self.speed = self.speed_slider.get()
            if self.algorithm == "Bubble Sort":
                self.sort_thread = threading.Thread(target=self.run_sorting_algorithm, args=(bubble_sort,))
            elif self.algorithm == "Insertion Sort":
                self.sort_thread = threading.Thread(target=self.run_sorting_algorithm, args=(insertion_sort,))
            elif self.algorithm == "Selection Sort":
                self.sort_thread = threading.Thread(target=self.run_sorting_algorithm, args=(selection_sort,))
            self.sort_thread.start()

    def run_sorting_algorithm(self, algorithm):
        if algorithm == bubble_sort:
            self.run_algorithm_with_gui_updates(algorithm, self.arr, self.update_bars)
        elif algorithm == insertion_sort:
            self.run_algorithm_with_gui_updates(algorithm, self.arr, self.update_bars)
        elif algorithm == selection_sort:
            self.run_algorithm_with_gui_updates(algorithm, self.arr, self.update_bars)
        self.is_sorting = False

    def run_algorithm_with_gui_updates(self, algorithm, arr, update_function):
        n = len(arr)
        for i in range(n):
            for j in range(0, n - i - 1):
                highlighted_bars = []
                if arr[j] > arr[j + 1]:
                    arr[j], arr[j + 1] = arr[j + 1], arr[j]
                    highlighted_bars = [j, j + 1]  # Mark bars being compared
                update_function(arr, highlighted_bars)
                time.sleep(self.speed)  # Adjust the speed dynamically
                if self.is_paused:
                    while self.is_paused:
                        time.sleep(0.1)  # Pause the sorting algorithm
                if not self.is_sorting:
                    break
            if not self.is_sorting:
                break

    def toggle_pause(self):
        self.is_paused = not self.is_paused

    def reset(self):
        self.is_paused = False
        self.is_sorting = False
        self.arr = []
        self.bars = []
        self.create_bars()
        self.update_bars(self.arr)


# Sorting Algorithms (Bubble Sort, Insertion Sort, Selection Sort)
def bubble_sort(arr, root, canvas, bars, speed, update_function):
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
            update_function(arr, highlighted_bars=[j, j + 1])
            time.sleep(speed)


def insertion_sort(arr, root, canvas, bars, speed, update_function):
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and key < arr[j]:
            arr[j + 1] = arr[j]
            j -= 1
        arr[j + 1] = key
        update_function(arr, highlighted_bars=[j + 1, i])
        time.sleep(speed)


def selection_sort(arr, root, canvas, bars, speed, update_function):
    for i in range(len(arr)):
        min_idx = i
        for j in range(i + 1, len(arr)):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        update_function(arr, highlighted_bars=[i, min_idx])
        time.sleep(speed)


if __name__ == "__main__":
    root = tk.Tk()
    visualizer = SortingVisualizer(root)
    root.mainloop()