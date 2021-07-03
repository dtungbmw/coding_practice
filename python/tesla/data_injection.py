import requests
import constant as c
import pandas as pd
import json
import logging


def get_raw_data():
    """
    Reteieve raw data by calling Tesla Rest apis
    :return: Data frame
    """
    log = logging.getLogger(__name__)
    try:
        response = requests.get(c.SITE_REQUEST)
    except ValueError:
        log.warning("Connection error for site request")
    sites = json.loads(response.text)
    rows_list = []
    if c.SITES in sites:
        for site in sites[c.SITES]:
            try:
                response = requests.get(c.SIGNAL_REQUEST+site)
                data = json.loads(response.text)
                data[c.SITE_COL] = site  # set site id
                rows_list.append(data)
            except ValueError:
                log.warning("Connection error")
    else:
        log.warning("No key for sites")

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







