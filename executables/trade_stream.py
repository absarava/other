import os
from alpaca.trading.stream import TradingStream

# Access environment variables
ALPACA_TRADE_API_KEY = os.environ.get('ALPACA_TRADE_API_KEY')
ALPACA_TRADE_API_SECRET_KEY = os.environ.get('ALPACA_TRADE_API_SECRET_KEY')

# Ensure the environment variables are set
if not ALPACA_TRADE_API_KEY or not ALPACA_TRADE_API_SECRET_KEY:
    raise ValueError("Alpaca API key and secret key must be set as environment variables.")

trade_stream_client = TradingStream(
    api_key=ALPACA_TRADE_API_KEY,
    secret_key=ALPACA_TRADE_API_SECRET_KEY,
    paper=True
)

async def trade_updates_handler(data):
    print(data)

trade_stream_client.subscribe_trade_updates(trade_updates_handler)
trade_stream_client.run()