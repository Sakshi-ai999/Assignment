import pandas as pd
df=pd.read_csv("table.csv")
df_india=df[df.Country=="India"]
df_austrial=df[df.Country=="Austrial]
df_india.to_csv("table_india.csv")
df_austrial.to_csv("table_austrial.csv")