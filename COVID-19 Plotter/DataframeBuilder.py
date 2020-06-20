import pandas as pd
import json

def BuildDataframeFromJSON(data):
    data_dict = json.loads(data)
    df = pd.DataFrame(data_dict)
    return df