import matplotlib
import numpy as np
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import pandas as pd
import tkinter as tk

class Plotter(object):
    """description of class"""

    def __init__(self, usdata = pd.DataFrame()):
        self.root = tk.Tk();
        self.canvas = None
        self._USData = usdata
        self.y_vars = []
        self.second_y_vars = []

    def figureDailyPosTests(self):
        x = self._USData["date"]
        y = self._USData["positiveIncrease"]
        fig = Figure()
        axes = fig.add_subplot(111)
        axes.plot(x,y)
        return fig

    def figureDailyTotalTests(self):
        x = self._USData["date"]
        y = self._USData["totalTestResultsIncrease"]
        fig = Figure()
        axes = fig.add_subplot(111)
        axes.plot(x,y)
        return fig

    def figureDailyPosRate(self):
        x = self._USData["date"]
        y = self._USData["percentPos"]
        fig = Figure()
        axes = fig.add_subplot(111)
        axes.plot(x,y)
        return fig

    def addFigure(self, figure):
        fig = Figure(figsize=(5,4))
        ax = fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(figure, master = self.root)

    def show(self):
        self.canvas.get_tk_widget().pack(side=tk.TOP, fill=tk.BOTH, expand=1)
        self.canvas.draw()
        self.root.mainloop()


