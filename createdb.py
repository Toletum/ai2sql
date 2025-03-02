import sqlite3
import pandas as pd


db = sqlite3.connect("db.db")


df = pd.read_csv('data/clients.csv')
df.to_sql('Client', db, if_exists="replace", index=False)

df = pd.read_csv('data/adresses.csv')
df.to_sql('Address', db,  if_exists="replace", index=False)

df = pd.read_csv('data/postalcodes.csv')
df.to_sql('PostalCode', db, if_exists="replace", index=False)

db.close()