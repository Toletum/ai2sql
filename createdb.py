import sqlite3
import pandas as pd


db = sqlite3.connect("db.db")


df = pd.read_csv('data/clientes.csv')
df.to_sql('Cliente', db, if_exists="replace", index=False)

df = pd.read_csv('data/direcciones.csv')
df.to_sql('Direccion', db,  if_exists="replace", index=False)

df = pd.read_csv('data/codpostal.csv')
df.to_sql('CodigoPostal', db, if_exists="replace", index=False)

db.close()