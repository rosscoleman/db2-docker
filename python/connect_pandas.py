from sqlalchemy import *
import pandas as pd

db2 = create_engine("db2+ibm_db://db2inst1:password@localhost:60000/testdb")

df = pd.read_sql("select * from syscat.tables where type = 'T'", db2)
print(df.head())
print({col: df[col].dtype for col in df.columns})