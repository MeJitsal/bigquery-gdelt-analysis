# bigquery-gdelt-analysis
This project tracks sentiment for the three largest components of the Consumer Price Index (CPI) — Food, Housing, and Transportation. Using BigQuery and Python, it processes GDELT data weekly, calculates percentiles, and extracts key geolocation details to provide insights on media tone and public sentiment for these essential sectors.

GDELT Weekly Tone Analysis Using BigQuery
This repository contains a data pipeline for querying, processing, and analyzing GDELT data using BigQuery and Python. The project focuses on three critical components of the Consumer Price Index (CPI) — Food, Housing, and Transportation — which together account for the largest portions of CPI. By tracking sentiment (AvgTone) for each category, this project aims to offer timely insights into the public discourse and media tone surrounding these essential sectors.

Weekly Aggregation: Extracts the week number from the SQLDATE field to group records by week.
Sentiment Analysis: Uses the AvgTone metric to measure sentiment for each category.
Percentile Calculations: Calculates the 25th and 75th percentiles for the AvgTone values each week.

Geographic Data Parsing: Extracts the first geolocation name (state) from Actor1Geo_Fullname.

**Key Features:**
Data Extraction: Queries GDELT tables for Food, Housing, and Transportation.
Data Transformation: Aggregates data weekly, calculates percentiles, and extracts state information from Actor1Geo_Fullname.
Data Load: Saves the processed DataFrame back to BigQuery for further analysis or visualization.
Sentiment Analysis: Measures sentiment using the GDELT "AvgTone" metric, offering a proxy for public perception.
Technologies Used: BigQuery, Pandas, Python.

**Installation:**
Clone the repository:
```bash
git clone https://github.com/your-username/your-repository-name.git

#Navigate into the project directory:
cd your-repository-name

#Install the required Python libraries:
pip install -r requirements.txt
```
Configure access to Google Cloud BigQuery (ensure you have the necessary credentials and permissions).


```bash
python3 bigquery_gdelt_cpi.py
```
