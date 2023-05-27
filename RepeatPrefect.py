import pandas as pd

repPref = pd.DataFrame(pd.read_csv("dataset/EarthquakeFrequency.csv"))


def detectRepeat():
    print(repPref)


detectRepeat()
