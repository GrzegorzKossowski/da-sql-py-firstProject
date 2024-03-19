import pandas as pd
import matplotlib.pylab as plt
import colors
from db.sqlalhemy_db import DatabaseConnection

# params
hostname = 'localhost'
port = "5432"
database = 'northwind'
username = 'northwind'
password = 'northwind'

# create URI
database_uri = f"postgresql://{username}:{password}@{hostname}:{port}/{database}"

# db connection
db_connection = DatabaseConnection(database_uri)

# get data from db to DataFrame, close connection
query = "SELECT * FROM customers"
df = pd.read_sql_query(query, db_connection.engine)

# Data Analisys
top_cities = df['city'].value_counts().head(5)
top_cities_names = top_cities.index.tolist()
top_cities_counts = top_cities.values.tolist()

# generate plots
fig, axes = plt.subplots(1,2, figsize=(12,6))

plt.suptitle('Top 5 cities per customer', fontsize=20.0, fontweight='semibold')

# bar
axes[0].bar(top_cities_names, top_cities_counts, color='skyblue')
axes[0].set_title('Top 5 cities')
axes[0].set_xlabel('City')
axes[0].set_ylabel('Customers')
axes[0].tick_params(axis='x', rotation=45)

# pie
axes[1].pie(top_cities_counts, labels=top_cities_names, autopct='%1.1f%%', explode=(0.04,0.02,0,0,0))
axes[1].set_title('Top 5 cities distribution')
fig

# save to file
plt.tight_layout()
plt.savefig('./plots/top_cities_chart.jpg', dpi=200)
plt.close()

colors.prCyan('Done')