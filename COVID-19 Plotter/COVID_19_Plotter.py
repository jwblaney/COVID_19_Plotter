import TCTP_API
import DataframeBuilder
import Plotter
import tkinter as tk
from tkinter import ttk

_stateAbbr = ["All US", "AL", "AK", "AZ", "AR", "CA", "CO", "CT", "DC", "DE", "FL", "GA", 
          "HI", "ID", "IL", "IN", "IA", "KS", "KY", "LA", "ME", "MD", 
          "MA", "MI", "MN", "MS", "MO", "MT", "NE", "NV", "NH", "NJ", 
          "NM", "NY", "NC", "ND", "OH", "OK", "OR", "PA", "RI", "SC", 
          "SD", "TN", "TX", "UT", "VT", "VA", "WA", "WV", "WI", "WY"]

class MainWindow(object):

    def __init__(self, *args, **kwargs):
        self.plot = Plotter.Plotter()

        self.root = tk.Tk()
        self.root.title("State selection")

        self.labelTop = tk.Label(self.root, text = "Select state to display data.")
        self.labelTop.pack()

        self.comboStateAbbr = ttk.Combobox(self.root, values = _stateAbbr, textvariable = "All US")
        self.comboStateAbbr.set("All US")
        self.comboStateAbbr.pack()

        self.btnUpdate = tk.Button(self.root, text = "Update", command = self.updateCallBack)
        self.btnUpdate.pack()

        self.updateCallBack()
        self.Show()

    def Show(self):
        self.root.mainloop()

    def updateCallBack(self):
        state = self.comboStateAbbr.get()
        if(state == "All US"):
            data = TCTP_API.GetUSDailyJSON()
        else:
            data = TCTP_API.GetStateDailyJson(state)
        df = DataframeBuilder.BuildDataframeFromJSON(data)
        self.plot.SetData(df)
        self.plot.addDailyStats()
        self.plot.show(state)

window = MainWindow()
window.Show()