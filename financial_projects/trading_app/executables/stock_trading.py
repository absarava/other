from datetime import datetime, timedelta
import alpaca
import os
from alpaca.data.historical.stock import StockHistoricalDataClient, StockLatestTradeRequest, StockLatestQuoteRequest
from alpaca.trading.client import TradingClient, GetAssetsRequest
from alpaca.trading.requests import GetOptionContractsRequest, LimitOrderRequest, MarketOrderRequest, GetOrdersRequest
from alpaca.trading.enums import AssetStatus, ContractType, OrderSide, OrderType, TimeInForce, QueryOrderStatus, AssetClass

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
    trade_client.submit_order(symbol=symbol, qty=qty, side='buy', type='market', time_in_force='gtc')

def sell_stock(symbol, qty):
    trade_client.submit_order(symbol=symbol, qty=qty, side='sell', type='market', time_in_force='gtc')

def get_position(symbol):
    return trade_client.get_position(symbol)


get_account_balance()
buy_stock('DIS',2)


search_params = GetAssetsRequest(asset_class=AssetClass.US_EQUITY)
assets = trade_client.get_all_assets(search_params)


print(assets)
