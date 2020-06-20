import TCTP_API
import DataframeBuilder

data = TCTP_API.GetUSDailyJSON()
print(DataframeBuilder.BuildDataframeFromJSON(data))