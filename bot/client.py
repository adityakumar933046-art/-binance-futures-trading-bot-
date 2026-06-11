# Binance client code goes here
from dotenv import load_dotenv
from binance.client import Client
import os

load_dotenv()

API_KEY = os.getenv("API_KEY")
API_SECRET = os.getenv("API_SECRET")

client = Client(API_KEY, API_SECRET)

client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"
print("API_KEY:", API_KEY)
print("API_SECRET:", API_SECRET)
