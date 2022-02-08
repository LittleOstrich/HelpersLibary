import pandas as pd

from helpers.pandasTools import dataframeToNumpyArray


def test1():
    d = {'col1': [1, 2], 'col2': [3, 4]}
    df = pd.DataFrame(data=d)

    keys, arr = dataframeToNumpyArray(df)

    print(keys)
    print(arr)


test1()
