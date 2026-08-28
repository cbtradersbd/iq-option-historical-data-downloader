# Sample Data Exporter
import requests

def fetch_candles(asset="EURUSD", count=100):
    url = "https://api1.api.cbtraderbd.xyz/api/iqoption/candles"
    print(f"Fetching {count} historical candles for {asset} from {url}...")

if __name__ == "__main__":
    fetch_candles()
