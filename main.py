import yfinance as yf
import pandas as pd
from datetime import datetime, timedelta
import os

# Liste der DAX 40-Ticker auf Yahoo Finance (Stand 2025)
dax_tickers = [
    "ADS.DE", "AIR.DE", "ALV.DE", "BAS.DE", "BAYN.DE", "BEI.DE", "BMW.DE", "BNR.DE", "CBK.DE", "1COV.DE",
    "DHER.DE", "DB1.DE", "DBK.DE", "DTE.DE", "EOAN.DE", "ENR.DE", "FME.DE", "FRE.DE", "HEN3.DE", "IFX.DE",
    "HEI.DE", "LIN.DE", "MRK.DE", "MBG.DE", "MTX.DE", "MUV2.DE", "NDA.DE", "PAH3.DE", "PUM.DE", "QIA.DE",
    "RWE.DE", "SAP.DE", "SIE.DE", "SHL.DE", "SY1.DE", "VNA.DE", "VOW3.DE", "VOW.DE", "ZAL.DE", "HNR1.DE"
]

# Zeitraum definieren
end_date = datetime.today()
start_date = end_date - timedelta(days=365)

# Verzeichnis für CSVs erstellen
output_dir = "dax_data"
os.makedirs(output_dir, exist_ok=True)

# Daten abrufen und speichern
for ticker in dax_tickers:
    print(f"Lade Daten für {ticker} ...")
    try:
        data = yf.download(ticker, start=start_date.strftime("%Y-%m-%d"), end=end_date.strftime("%Y-%m-%d"), interval="1d")
        if not data.empty:
            data.to_csv(f"{output_dir}/{ticker}.csv")
        else:
            print(f"⚠️ Keine Daten für {ticker}.")
    except Exception as e:
        print(f"❌ Fehler bei {ticker}: {e}")

print("✅ Fertig.")
