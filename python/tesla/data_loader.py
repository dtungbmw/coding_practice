import constant
import data_injection as di
import pandas as pd


def store_signal_data():

    # get raw data every m mins
    df = di.get_raw_data()

    print(df)
    return



store_signal_data()