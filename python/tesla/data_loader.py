import constant as c
import data_injection as di
import pandas as pd
import time
import os.path
from os import path

def store_signal_data():
    while True:
        # get raw data every m mins
        df = di.get_raw_data()
        if path.exists(c.RAW_DATA_FILE):
            df.to_csv(c.RAW_DATA_FILE,index=False, header=False, mode='a')
        else:
            df.to_csv(c.RAW_DATA_FILE, index=False, header=True, mode='a')
        time.sleep(c.INTERVAL) # every minute



store_signal_data()