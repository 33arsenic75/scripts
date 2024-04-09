# import pandas as pd
# from sqlalchemy import create_engine

# # Assuming df is your cleaned DataFrame
# df = pd.read_csv('nssData.csv')
# df.dropna(inplace=True)

# # Convert 'Total Approved Hour' column to integers
# df['Total Approved Hours'] = pd.to_numeric(df['Total Approved Hours'], errors='coerce')

# # Specify the SQLite database file path
# db_file_path = 'nssData.db'

# # Create a SQLite engine
# engine = create_engine(f'sqlite:///{db_file_path}')

# # Save the DataFrame to the SQLite database
# df.to_sql('nssData', engine, index=False, if_exists='replace')

import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv('nssData.csv')
df.dropna(inplace=True)

# Convert 'Total Approved Hour' column to integers
df['Total Approved Hours'] = pd.to_numeric(df['Total Approved Hours'], errors='coerce')

# Sort the DataFrame based on 'Total Approved Hour'
df_sorted = df.sort_values(by='Total Approved Hours', ascending=False)

# Add a new column 'Rank' based on the sorted order
df_sorted['Rank'] = range(1, len(df_sorted) + 1)

# Specify the SQLite database file path
db_file_path = 'nssData.db'

# Create a SQLite engine
engine = create_engine(f'sqlite:///{db_file_path}')

# Save the sorted DataFrame to the SQLite database
df_sorted.to_sql('nssData', engine, index=False, if_exists='replace')
