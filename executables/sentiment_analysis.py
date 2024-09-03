import requests
import json

## TASK 1
### GET NEWS INFORMATION ABOUT MAG SEVEN STOCKS AND
### CREATE A TABLE STORING EOD PRICES FOR NEXT 1 WEEK

import requests

url = "https://seeking-alpha.p.rapidapi.com/v2/auto-complete"

querystring = {"query":"apple","type":"people,symbols,pages","size":"5"}

headers = {
	"X-RapidAPI-Key": "85a3c5c463msh76c0bf212394948p14af33jsn7f3bfaabf24c",
	"X-RapidAPI-Host": "seeking-alpha.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)

print(response.json())

## Getting real time quotes
url = "https://seeking-alpha.p.rapidapi.com/market/get-realtime-quotes"

querystring = {"sa_ids":"612888,16123,146,1150"}

headers = {
	"X-RapidAPI-Key": "85a3c5c463msh76c0bf212394948p14af33jsn7f3bfaabf24c",
	"X-RapidAPI-Host": "seeking-alpha.p.rapidapi.com"
}

response = requests.get(url, headers=headers, params=querystring)


response_json = response.json()

# ticker, last price

tick_price = {}

for x in response_json['real_time_quotes']:
	tick_price.update({x['symbol']: x['last']})


# print((response_json['real_time_quotes'][1]['ticker_id']))