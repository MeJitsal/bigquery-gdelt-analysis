# bigquery-gdelt-analysis
This project tracks sentiment for the three largest components of the Consumer Price Index (CPI) — Food, Housing, and Transportation. Using BigQuery and Python, it processes GDELT data weekly, calculates percentiles, and extracts key geolocation details to provide insights on media tone and public sentiment for these essential sectors.

GDELT Weekly Tone Analysis Using BigQuery
This repository contains a data pipeline for querying, processing, and analyzing GDELT data using BigQuery and Python. The project focuses on three critical components of the Consumer Price Index (CPI) — Food, Housing, and Transportation — which together account for the largest portions of CPI. By tracking sentiment (AvgTone) for each category, this project aims to offer timely insights into the public discourse and media tone surrounding these essential sectors.

Key Features:

Data Extraction: Queries GDELT tables for Food, Housing, and Transportation.
Data Transformation: Aggregates data weekly, calculates percentiles, and extracts state information from Actor1Geo_Fullname.
Data Load: Saves the processed DataFrame back to BigQuery for further analysis or visualization.
Sentiment Analysis: Measures sentiment using the GDELT "AvgTone" metric, offering a proxy for public perception.
Technologies Used: BigQuery, Pandas, Python.
