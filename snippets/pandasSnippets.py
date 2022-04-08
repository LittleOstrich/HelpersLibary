import numpy as np
import pandas as pd

from helpers.pandasTools import dataframeToNumpyArray, readXlsx


def test1():
    d = {'col1': [1, 2], 'col2': [3, 4]}
    df = pd.DataFrame(data=d)

    keys, arr = dataframeToNumpyArray(df)

    print(keys)
    print(arr)


def test2():
    fn = "tmp\\Possible Locations_Accomodations May-June 22.xlsx"
    df: pd.DataFrame = readXlsx(fn)
    print(df.keys())

    df = df[["Mail", "Contacted? They replied?"]]
    df = df.loc[df["Contacted? They replied?"] != "yes"]
    df = df.loc[df["Contacted? They replied?"] != "Yes"]
    mails = df["Mail"].tolist()
    print(mails)
    return df


test2()
