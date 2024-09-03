paper = True

from datetime import datetime,timedelta
import alpaca
from alpaca.data.historical.option import OptionHistoricalDataClient, OptionLatestQuoteRequest
from alpaca.data.historical.stock import  StockHistoricalDataClient, StockLatestTradeRequest, StockLatestQuoteRequest
from alpaca.trading.client import TradingClient, GetAssetsRequest
from alpaca.trading.requests import GetOptionContractsRequest, LimitOrderRequest, MarketOrderRequest, GetOrdersRequest
from alpaca.trading.enums import AssetStatus, ContractType, OrderSide, OrderType, TimeInForce, QueryOrderStatus

ALPACA_TRADE_API_KEY = os.environ.get('ALPACA_TRADE_API_KEY')
ALPACA_TRADE_API_SECRET_KEY = os.environ.get('ALPACA_TRADE_API_SECRET_KEY')


trade_client = TradingClient(api_key=alpaca_keys["TRADE_API_KEY"], secret_key=alpaca_keys["TRADE_API_SECRET_KEY"], paper=True)

stock_data_client = StockHistoricalDataClient(api_key=alpaca_keys["TRADE_API_KEY"], secret_key=alpaca_keys["TRADE_API_SECRET_KEY"])

option_data_client = OptionHistoricalDataClient(api_key=alpaca_keys["TRADE_API_KEY"], secret_key=alpaca_keys["TRADE_API_SECRET_KEY"])


# Get Account Information
acct = trade_client.get_account()

print(f"Options Approved Level: {acct.options_approved_level}")
print(f"Options Trading Level: {acct.options_trading_level}")
print(f"Options Buying Power: {acct.options_buying_power}")

acct_config = trade_client.get_account_configurations()
#acct_config.max_options_trading_level = 1
print(f"Max Options Trading Level: {acct_config.max_options_trading_level}")


req = GetAssetsRequest(
    status = AssetStatus.ACTIVE,
    attributes = "options_enabled"
)

options_enabled_underlyings = trade_client.get_all_assets