import requests
import constant as c
import pandas as pd
import json
import logging
import utils as u

def get_raw_data():
    """
    Reteieve raw data by calling Tesla Rest apis
    :return: Data frame
    """
    log = logging.getLogger(__name__)
    sites = u.get_json_data(c.SITE_REQUEST)
    rows_list = []
    if c.SITES in sites:
        for site in sites[c.SITES]:
            data = u.get_json_data(c.SIGNAL_REQUEST+site)
            if data is None:
                continue
            #print(data)
            data[c.SITE_COL] = site  # set site id
            rows_list.append(data)
    else:
        log.warning("No key for sites")

    if len(rows_list) == 0:
        return None
    df = normalize(rows_list)
    return df


def normalize(raw_list):
    """

    :param raw_list:
    :return:
    """

    df = pd.json_normalize(raw_list)
    df[c.DATE_COL] = pd.to_datetime(df[c.TIMESTAMP_COL])
    df.rename(columns={c.OLD_BATTERY_POWER_COL: c.BATTERY_POWER_COL,
                           c.OLD_SITE_POWER_COL: c.SITE_POWER_COL,
                           c.OLD_SOLAR_POWER_COL: c.SOLAR_POWER_COL},
                  inplace=True)
    df = df.loc[:, df.columns.isin(c.HEADER_LIST)]

    return df.round(2)







