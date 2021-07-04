
# **Tesla Energy Data Test**

## ETL pipeline
- Run : python3 data_loader.py
### Data extraction


- Invoke simulated Rest API provided by Tesla data test:

     a. Retrieve sites info 
     
     b. Retrieve singals info with each site id from #a
     
     c. Convert signal json result to python dictionary object with site id 
     

### Data transformation

- Extracted data is normalized and flatterned

- Unused columes are removed and Columne names are renamed for easy reference

- Timestamp colume is added based on date time string

## Data Loading

- Data is loaded into cvs file 

- Loader had been running for 2 days and continuously append into csv file


## Historical data analysis

- Run: jupyter notebook: history_data_view.ipynb

- Hourly boxplot and scatter plot time series charts are used for historical data analysis for each site


- Anomaly analysis based on visual analysis:

    a. 

    b. Sites without data: 2b33a48d, 90791ae9

    c. 

## Realtime anomaly analysis

- Run: python3 anomaly_dector.py
