import TCTP_API
import DataframeBuilder
import Plotter

data = TCTP_API.GetUSDailyJSON()
df = DataframeBuilder.BuildDataframeFromJSON(data)
plot = Plotter.Plotter(df)
plot.addFigure(plot.figureDailyTotalTests())
plot.show()