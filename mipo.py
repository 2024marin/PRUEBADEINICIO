import pandas as pd
import numpy as np

#ruta = "C:\Users\MAO\Desktop\MIPOARCH\dump-mipo.09072024.sql"
#pd.read_sql_query("SELECT * FROM mipo_asientos", con=ruta)
#print(df.head())


# Leer el archivo SQL
sql_file_path = r"C:\Users\MAO\Desktop\MIPOARCH\dump-mipo.09072024.sql"
with open(sql_file_path, 'r', encoding='utf-8') as sql_file:
    sql_script = sql_file.read()

for statement in sql_script.split(';'):
    if statement.strip():
        cursor.execute(statement)
