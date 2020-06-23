import matplotlib.pyplot as plt
import pandas as pd


class Plotter(object):
    """description of class"""

    def __init__(self, usdata = pd.DataFrame()):
        self._USData = usdata
        self.y_vars = []
        self.second_y_vars = []

    def plotUSDaily(self):
        self.y_vars.append("positiveIncrease")

    def plotTests(self):
        self.y_vars.append("totalTestResultsIncrease")

    def plotPosRate(self):
        self.y_vars.append("percentPos")

    def show(self):
        self._USData.plot(x = "date", y =self.y_vars, subplots=True,  kind = "line")
        plt.show()


