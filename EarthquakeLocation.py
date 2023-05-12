import pandas as pd
from collections import Counter
def prefecs():
    locations = pd.DataFrame(pd.read_csv('dataset/japTranslated.csv'))
    print(locations)
    freq = locations.pivot_table(index=['Location of Earthquake'], aggfunc='size')
    print(freq)
    freq.to_csv('EarthquakeFrequency.csv')

prefecs()