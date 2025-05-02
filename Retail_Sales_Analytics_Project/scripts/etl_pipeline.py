
import pandas as pd
from sqlalchemy import create_engine

# Extraction
data = pd.read_csv('../data/business.retailsales.csv')

# Transformation: cleaning and summary metrics
data.dropna(inplace=True)

# Compute additional analytical columns if needed
data['Net Revenue per Item'] = data['Total Net Sales'] / data['Net Quantity']

# Save processed data
data.to_csv('../output/retail_sales_processed.csv', index=False)

# Loading into SQLite database
engine = create_engine('sqlite:///retail_sales.db')
data.to_sql('retail_sales', con=engine, if_exists='replace', index=False)

print("ETL process completed successfully.")
