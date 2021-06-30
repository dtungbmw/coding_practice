import requests
import constant as c
import pandas as pd
import json
import logging

##

## return data frame of signal data with site ids
def get_raw_data():
    log = logging.getLogger("data_collection")
    response = requests.get(c.SITE_REQUEST)
    sites = json.loads(response.text)
    df = None
    if c.SITES in sites:
        for site in sites[c.SITES]:
            log.info(site)
            response = requests.get(c.SIGNAL_REQUEST+site)
            data = json.loads(response.text)
            df = pd.json_normalize(data)
            df.rename(columns={c.OLD_BATTERY_POWER_COL: c.BATTERY_POWER_COL,
                               c.OLD_SITE_POWER_COL: c.SITE_POWER_COL,
                               c.OLD_SOLAR_POWER_COL: c.SOLAR_POWER_COL},
                      inplace=True)
            df[c.SITE_COL] = site # set site id
    else:
        log.warning("No key for sites")
    return df



