import pandas as pd

df = pd.read_json("data/dump.json")
df = df.transpose()

df = df[df["Realm"] != "7"]

def date_conv(ms):
    x = ms / 1000
    x /= 60 # Minutes
    x /= 60 # Hours
    x /= 24 # Days
    days = x

    return days
date = df["LastUpdated"]
last_updated = date.apply(min(date_conv))
print("The dataset was updated {0} days ago.".format(round(last_updated), 2))

df.to_csv("data/dump.csv")
