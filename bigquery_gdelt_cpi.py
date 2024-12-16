 


# Running this code will query a table in BigQuery and download
# Learn more here: https://cloud.google.com/bigquery/docs/visualize-jupyter

%%bigquery food --project sincere-pen-442701-r8
SELECT * FROM `sincere-pen-442701-r8.gdelt.food` #this table name was set based on the table you chose to query

# %%
food=pd.DataFrame(food)

# %%
import pandas as pd
from datetime import datetime

# %%
# Convert SQLDATE to datetime and extract week number
food['week_number'] = pd.to_datetime(food['SQLDATE'], format='%Y%m%d').dt.isocalendar().week

# %%
food['category'] = 'food'

# %%
destination_table = "gdelt.food"  # Use only dataset and table name

# Save the DataFrame to BigQuery
to_gbq(food, destination_table=destination_table, if_exists='replace')


# %%
# Running this code will query a table in BigQuery and download
# the results to a Pandas DataFrame named `results`.
# Learn more here: https://cloud.google.com/bigquery/docs/visualize-jupyter

%%bigquery housing --project sincere-pen-442701-r8
SELECT * FROM `sincere-pen-442701-r8.gdelt.housing` #this table name was set based on the table you chose to query

# %%
housing=pd.DataFrame(housing)

# %%
housing['week_number'] = pd.to_datetime(housing['SQLDATE'], format='%Y%m%d').dt.isocalendar().week
housing['category'] = 'housing'

# %%
destination_table = "gdelt.food"  # Use only dataset and table name

# Save the DataFrame to BigQuery
to_gbq(food, destination_table=destination_table, if_exists='replace')

# %%
%%bigquery transportation --project sincere-pen-442701-r8
SELECT * FROM `sincere-pen-442701-r8.gdelt.transportation` #this table name was set based on the table you chose to query

# %%
transportation=pd.DataFrame(transportation)

# %%
transportation['week_number'] = pd.to_datetime(transportation['SQLDATE'], format='%Y%m%d').dt.isocalendar().week
transportation['category'] = 'transportation'

# %%
df = pd.concat([food, housing, transportation], ignore_index=True)

# %%
df['date'] = pd.to_datetime(df['SQLDATE'], format='%Y%m%d')

# %%
grouped_by_week = df.groupby('week_number', group_keys=False)

# %%
df['Percentile_25'] = grouped_by_week['AvgTone'].transform(lambda x: x.quantile(0.25))
df['Percentile_75'] = grouped_by_week['AvgTone'].transform(lambda x: x.quantile(0.75))

# %%
gdelt = df.sort_values(by='week_number')

# %%
max_commas = gdelt['Actor1Geo_Fullname'].fillna('').str.split(',').apply(len).max()

# Split the 'Actor1Geo_Fullname' by commas and expand it into multiple columns
gdelt[[f'name_{x}' for x in range(max_commas)]] = gdelt['Actor1Geo_Fullname'].fillna('').str.split(',', expand=True)

# %%
gdelt=gdelt[['Year','SQLDATE', 'Actor1Geo_CountryCode', 'AvgTone','SOURCEURL','week_number','category','date','Percentile_25', 'Percentile_75','name_1']].rename(
    columns={'name_1':'state'}
)

# %%
destination_table = "gdelt.df"  # Use only dataset and table name

# Save the DataFrame to BigQuery
to_gbq(gdelt, destination_table=destination_table, if_exists='replace')

# %%



