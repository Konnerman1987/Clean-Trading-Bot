import os
import alpaca_trade_api as tradeapi
from dotenv import load_dotenv
import time

load_dotenv()

API_KEY = os.getenv("APCA_API_KEY_ID")
SECRET_KEY = os.getenv("APCA_API_SECRET_KEY")
BASE_URL = "https://paper-api.alpaca.markets"

api = tradeapi.REST(API_KEY, SECRET_KEY, BASE_URL, api_version='v2')

def run_bot():
    print("Starting trading bot...")

    while True:
        clock = api.get_clock()
        if clock.is_open:
            print("Market is open. Checking for trades...")

            # Example strategy: Buy if cash is available and we don’t already own
            account = api.get_account()
            cash = float(account.cash)

            position = None
            try:
                position = api.get_position("SPY")
            except:
                pass  # No position found

            if cash > 10 and not position:
                print("Buying SPY...")
                api.submit_order(
                    symbol="SPY",
                    qty=1,
                    side="buy",
                    type="market",
                    time_in_force="gtc"
                )
            else:
                print("No action taken.")

        else:
            print("Market is closed.")

        time.sleep(60)  # Wait 1 minute before next check
