import tkinter as tk
from graph_widget import GraphWidget

if __name__ == '__main__':
    root = tk.Tk()
    root.title("Graph Widget")

    graph_widget = GraphWidget(root)

    root.mainloop()