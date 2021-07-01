import constant as c
import data_injection as di
import pandas as pd


def store_signal_data():

    # get raw data every m mins
    df = di.get_raw_data()
    df.to_csv(c.RAW_DATA_FILE,index=False, header=False, mode='a')
    return



store_signal_data()