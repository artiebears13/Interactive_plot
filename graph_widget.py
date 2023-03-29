import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import tkinter as tk
from tkinter import ttk


class GraphWidget:
    def __init__(self, master):
        self.master = master
        self.x_min = -50
        self.x_max = 50
        self.y_min = 0
        self.y_max = 500
        self.color = 'blue'
        self.line_type = '-'
        self.master.config(bg='white')

        self.x = list(range(self.x_min, self.x_max))
        self.y = [i ** 2 for i in self.x]

        self.fig = self.plot_graph()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=1, column=0, columnspan=5)

        self.navigation_toolbar = tk.Frame(self.master, borderwidth=0.5, relief='solid', bg='white')
        self.navigation_label = tk.Label(self.navigation_toolbar, text='Навигация', bg='white')
        self.navigation_label.grid(row=0, column=0, columnspan=2, sticky='nwe')
        self.btn_left = tk.Button(self.navigation_toolbar, text='<', command=self.move_left, bg='white')
        self.btn_left.grid(row=1, column=0)

        self.btn_right = tk.Button(self.navigation_toolbar, text='>', command=self.move_right, bg='white')
        self.btn_right.grid(row=1, column=1)

        self.btn_up = tk.Button(self.navigation_toolbar, text='^', command=self.move_up, bg='white')
        self.btn_up.grid(row=2, column=0)

        self.btn_down = tk.Button(self.navigation_toolbar, text='v', command=self.move_down, bg='white')
        self.btn_down.grid(row=2, column=1)
        self.navigation_toolbar.grid(row=2, column=0)

        self.zoom_toolbar = tk.Frame(self.master, bg='white')

        self.zoom_label = tk.Label(self.zoom_toolbar, text='zoom', bg='white')
        self.zoom_label.grid(row=0, column=0)
        self.btn_zoom_in = tk.Button(self.zoom_toolbar, text='+', command=self.zoom_in, bg='white')
        self.btn_zoom_in.grid(row=0, column=1)

        self.zoom_toolbar.grid(row=2, column=1)

        self.btn_zoom_out = tk.Button(self.zoom_toolbar, text='-', command=self.zoom_out, bg='white')
        self.btn_zoom_out.grid(row=0, column=2)

        self.color_var = tk.StringVar()
        self.color_var.set('blue')
        self.color_label = tk.Label(self.master, text='Цвет:',pady=10, bg='white')
        self.color_label.grid(row=4, column=0)
        self.color_menu = ttk.Combobox(self.master, textvariable=self.color_var,
                                       values=['blue', 'red', 'black', 'yellow', 'green'])
        self.color_menu.bind('<<ComboboxSelected>>', self.apply_params)
        self.color_menu.grid(row=4, column=1)

        # self.lbl_color = tk.Label(self.master, text='Color:')
        # self.lbl_color.grid(row=4, column=0)
        # 
        # self.entry_color = tk.Entry(self.master)
        # self.entry_color.insert(0, self.color)
        # self.entry_color.grid(row=4, column=1)

        # self.lbl_line_type = tk.Label(self.master, text='Line Type:')
        # self.lbl_line_type.grid(row=5, column=0)

        # self.entry_line_type = tk.Entry(self.master)
        # self.entry_line_type.insert(0, self.line_type)
        # self.entry_line_type.grid(row=5, column=1)

        self.btn_apply = tk.Button(self.master, text='Apply', command=self.apply_params, bg='white')
        self.btn_apply.grid(row=6, column=0, columnspan=2,pady=10)

        self.type_var = tk.StringVar()
        self.type_var.set('-')
        self.type_label = tk.Label(self.master, text='Тип:', bg='white')
        self.type_label.grid(row=5, column=0)
        self.type_menu = ttk.Combobox(self.master, textvariable=self.type_var,
                                      values=['solid', 'dashed', 'dashdot',
                                              'dotted'])
        self.type_menu.bind('<<ComboboxSelected>>', self.apply_params)
        self.type_menu.grid(row=5, column=1)

    def plot_graph(self):
        fig = plt.figure(figsize=(5, 4), dpi=100)
        plt.plot(self.x, self.y, color=self.color, linestyle=self.line_type)
        plt.grid()
        plt.ylim((self.y_min, self.y_max))
        return fig

    def update_graph(self):
        self.x = list(range(self.x_min, self.x_max))
        self.y = [i ** 2 for i in self.x]
        plt.clf()
        self.fig = self.plot_graph()
        self.canvas = FigureCanvasTkAgg(self.fig, master=self.master)
        self.canvas.draw()
        self.canvas.get_tk_widget().grid(row=1, column=0, columnspan=5)

    def move_left(self):
        self.x_min -= 10
        self.x_max -= 10
        self.update_graph()

    def move_right(self):
        self.x_min += 10
        self.x_max += 10
        self.update_graph()

    def move_up(self):
        self.y_min += 500
        self.y_max += 500
        self.update_graph()

    def move_down(self):
        self.y_min -= 500
        self.y_max -= 500
        self.update_graph()

    def zoom_in(self):
        self.x_min += 10
        self.x_max -= 10
        self.y_min += 10
        self.y_max -= 10
        self.update_graph()

    def zoom_out(self):
        self.x_min -= 10
        self.x_max += 10
        self.y_min -= 10
        self.y_max += 10
        self.update_graph()

    def apply_params(self, *args):
        self.color = self.color_menu.get()
        self.line_type = self.type_menu.get()
        self.update_graph()
