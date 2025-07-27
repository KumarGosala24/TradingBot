# src/binance_client.py
from binance.client import Client

API_KEY = 'YOUR_API_KEY'
API_SECRET = 'YOUR_SECRET_KEY'

client = Client(API_KEY, API_SECRET)
client.FUTURES_URL = 'https://fapi.binance.com'
