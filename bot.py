import os
import alpaca_trade_api as tradeapi
from dotenv import load_dotenv

# Load the .env file
load_dotenv()

# Get keys from environment variables
API_KEY = os.getenv("APCA_API_KEY_ID")
API_SECRET = os.getenv("APCA_API_SECRET_KEY")
BASE_URL = "https://paper-api.alpaca.markets"

# Connect to Alpaca
api = tradeapi.REST(API_KEY, API_SECRET, BASE_URL, api_version='v2')

# Check your account info
account = api.get_account()
print(f"Account status: {account.status}")
