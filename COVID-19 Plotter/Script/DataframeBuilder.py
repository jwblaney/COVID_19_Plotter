import pandas as pd
import json

def BuildDataframeFromJSON(data):
    data_dict = json.loads(data)
    df = pd.DataFrame(data_dict)
    df["percentPos"] = df["positiveIncrease"]/df["totalTestResultsIncrease"]
    df["date"] = pd.to_datetime(df["date"], format = "%Y%m%d")
    return df