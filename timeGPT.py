import os
import pandas as pd
from nixtlats import TimeGPT
from dotenv import load_dotenv

load_dotenv()

# TimeGPT Instanz wird erstellt Beeb Boop 🤖
timegpt = TimeGPT(token=os.environ['NIXTLAT_TOKEN'])

# Daten werden geladen und vorbereitet Beeb Boop 🤖
df = pd.read_csv('https://raw.githubusercontent.com/nyxb/data/main/Solana%20Prices.csv')

df_low = df[['Date', 'Low']].copy()
df_low['unique_id'] = 'Low'
df_low.rename(columns={'Date': 'ds', 'Low': 'y'}, inplace=True)

df_high = df[['Date', 'High']].copy()
df_high['unique_id'] = 'High'
df_high.rename(columns={'Date': 'ds', 'High': 'y'}, inplace=True)

df = pd.concat([df_low, df_high], ignore_index=True)

# Prognose wird erstellt... Beeb Boop 🤖
forecast_df = timegpt.forecast(df=df, h=12, freq='D')

# Ergebnisse werden angezeigt Beeb Boop 🤖
print(forecast_df.head())
