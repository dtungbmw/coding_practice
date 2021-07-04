import pandas as pd
import os.path
from os import path
import os
import numpy as np
import requests
from pathlib import Path
import glob
import datetime
from utils import *
import time
from data_injection import *


def check_anomaly(ts, site, hour, power, lower, upper ):
    if power < lower or power > upper:
        print("*** Site: "+site+", date= "+str(ts)+", hour= "+str(hour)+", solar= "+str(power)+" has anomaly detected")
        print("===> lower= "+str(lower)+", upper= "+str(upper))


def merge_data():
    sites = get_json_data(c.SITE_REQUEST)['sites']
    data = pd.read_csv('./raw_data.csv') # read history data
    data['hour'] = data['date'].astype('datetime64[ns]').dt.hour
    bp_data = get_box_plot_data(data, sites)
    new_df = get_raw_data()
    new_df['hour'] = new_df['date'].astype('datetime64[ns]').dt.hour
    merged = pd.merge( new_df, bp_data, on=['hour','site'], how = 'inner')
    return merged


while True:
    df = merge_data()
    df.apply(lambda row : check_anomaly(row['date'], row['site'],row['hour'],row['solar_power'],row['lower_quartile'],
                                  row['upper_quartile']), axis = 1)
    time.sleep(c.INTERVAL)  # every minute


