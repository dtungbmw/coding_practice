
TOKEN = '5812f27391bb286e619af101090d6406'
SITE_REQUEST ='https://te-data-test.herokuapp.com/api/sites?token='+TOKEN
SIGNAL_REQUEST= 'https://te-data-test.herokuapp.com/api/signals?token='+TOKEN+'&site='
INTERVAL = 60 # sec
SITES = 'sites'
SITE_COL = 'site'
OLD_BATTERY_POWER_COL = 'signals.SITE_SM_batteryInstPower'
OLD_SITE_POWER_COL = 'signals.SITE_SM_siteInstPower'
OLD_SOLAR_POWER_COL = 'signals.SITE_SM_solarInstPower'

BATTERY_POWER_COL = 'battery_power'
SITE_POWER_COL = 'site_power'
SOLAR_POWER_COL = 'solar_power'

DATE_COL = 'date'
TIMESTAMP_COL = 'timestamp'

DATA_COLLECTION = 'data_collection'

RAW_DATA_FILE = "./raw_data.csv"

HEADER_LIST = [ SITE_COL, BATTERY_POWER_COL, SITE_POWER_COL,SOLAR_POWER_COL, DATE_COL]
