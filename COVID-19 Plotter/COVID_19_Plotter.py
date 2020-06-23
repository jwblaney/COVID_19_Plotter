import TCTP_API
import DataframeBuilder
import Plotter
import tkinter

data = TCTP_API.GetUSDailyJSON()
df = DataframeBuilder.BuildDataframeFromJSON(data)
plot = Plotter.Plotter(df)
plot.plotUSDaily()
plot.plotTests()
plot.plotPosRate()
plot.show()
