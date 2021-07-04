import requests
import constant as c
import json
import logging
import sys
import pandas as pd
import requests
from pathlib import Path
import matplotlib.pyplot as plt
import glob
import seaborn as sns
import datetime


def get_json_data(request):
    """
    Get json data according to the request url
    :param request: url
    :return: json data dict
    """
    log = logging.getLogger(__name__)
    result = None
    try:
        response = requests.get(request)
        if response.status_code != 200:
            log.error("Error in respond: %s", response.text)
            return result
        result = json.loads(response.text)
    except:
        e = sys.exc_info()[0]
        log.warning("<p>Error: %s</p>" % e)

    return result


def get_box_plot_data(labels, bp):
    rows_list = []
    for i in range(len(labels)):
        dict1 = {}
        dict1['label'] = labels[i]
        dict1['lower_whisker'] = bp['whiskers'][i*2].get_ydata()[1]
        dict1['lower_quartile'] = bp['boxes'][i].get_ydata()[1]
        dict1['median'] = bp['medians'][i].get_ydata()[1]
        dict1['upper_quartile'] = bp['boxes'][i].get_ydata()[2]
        dict1['upper_whisker'] = bp['whiskers'][(i*2)+1].get_ydata()[1]
        rows_list.append(dict1)
    return pd.DataFrame(rows_list)


def plot_scatter_chart(data, site, show_solar, show_battery, show_site):
    ax = plt.gca()
    fig = plt.gcf()
    fig.set_size_inches(15.5, 3)
    site_data = data[data.site == site]
    if show_battery:
        site_data.plot(kind='scatter', x='hour', y="battery_power", color='blue', ax=ax)
    if show_site:
        site_data.plot(kind='scatter', x='hour', y="site_power", color='purple', ax=ax)
    if show_solar:
        site_data.plot(kind='scatter', x='hour', y="solar_power", color='green', ax=ax)
    plt.title('site: ' + site )
    plt.xticks(range(0, 24))
    plt.show()

def plot_box_plot(data, site):
    fig, ax = plt.subplots(figsize=(12, 5))
    fig.set_size_inches(15.5, 4)
    site_data = data[data.site == site]
    sns.boxplot(y=site_data["solar_power"], x=site_data["hour"])
    # q1 = site_data[['solar_power','hour']].quantile(0.25)[0]
    # q3 = site_data[['solar_power','hour']].quantile(0.75)[0]
    # a = site_data.loc[site_data['solar_power'] >q3]
    # ax.scatter(a['hour'],a['solar_power'], color='red', label='Anomaly')
    # plt.xticks(range(1,25))
    plt.show()