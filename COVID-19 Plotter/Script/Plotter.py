import matplotlib.pyplot as plt
import pandas as pd


class Plotter(object):
    """description of class"""

    def __init__(self, data = pd.DataFrame()):
        self._data = data
        self.y_vars = []

    def plotDailyCases(self):
        self.y_vars.append("positiveIncrease")

    def plotDailyTests(self):
        self.y_vars.append("totalTestResultsIncrease")

    def plotDailyPosRate(self):
        self.y_vars.append("percentPos")

    def clearStats(self):
        self.y_vars = []

    def addDailyStats(self):
        self.clearStats()
        self.plotDailyCases()
        self.plotDailyTests()
        self.plotDailyPosRate()

    def show(self, state):
        plt.close()
        self._data.plot(x = "date", y =self.y_vars, subplots=True,  kind = "line")
        plt.title = state + " COVID-19 Statistics"
        plt.show()

    def SetData(self, df):
        self._data = df