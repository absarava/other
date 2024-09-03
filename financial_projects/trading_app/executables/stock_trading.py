import os
from alpaca.trading.client import TradingClient
from alpaca.trading.requests import MarketOrderRequest
from alpaca.trading.enums import OrderSide, TimeInForce, OrderType
from alpaca.trading.requests import GetAssetsRequest
from alpaca.trading.enums import AssetClass

ALPACA_TRADE_API_KEY = os.environ.get('ALPACA_TRADE_API_KEY')
ALPACA_TRADE_API_SECRET_KEY = os.environ.get('ALPACA_TRADE_API_SECRET_KEY')

trade_client = TradingClient(api_key=ALPACA_TRADE_API_KEY, secret_key=ALPACA_TRADE_API_SECRET_KEY, paper=True)

# Get Account Information
acct = trade_client.get_account()

def get_account_balance():
    print(f"Account Cash Balance: {acct.cash}")
    print(f"Account Buying Power: {acct.buying_power}")
    print(f"Portfolio Value: {acct.portfolio_value}")

def buy_stock(symbol, qty):
    market_order_data = MarketOrderRequest(
        symbol=symbol,
        qty=qty,
        side=OrderSide.BUY,
        time_in_force=TimeInForce.GTC
    )
    trade_client.submit_order(market_order_data)

def sell_stock(symbol, qty):
    market_order_data = MarketOrderRequest(
        symbol=symbol,
        qty=qty,
        side=OrderSide.SELL,
        time_in_force=TimeInForce.GTC
    )
    trade_client.submit_order(market_order_data)

def get_position(symbol):
    return trade_client.get_open_position(symbol)

get_account_balance()
buy_stock('DIS', 2)

#search_params = GetAssetsRequest(asset_class=AssetClass.US_EQUITY)
#assets = trade_client.get_all_assets(search_params)

#print(assets)