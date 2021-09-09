import requests as requests
from bs4 import BeautifulSoup

webpage_in = requests.get("https://coinmarketcap.com/currencies/bitcoin/")
webpage = webpage_in.content
htmldataforwebpage = BeautifulSoup(webpage_in.content, 'html.parser')
current_bitcoin_price = htmldataforwebpage.td
print(str(current_bitcoin_price) + " is the current Bitcoin price (in USD)")

webpage_in2 = requests.get("https://coinmarketcap.com/currencies/ethereum/", "html.parser")
webpage2 = webpage_in2.content
htmldataforwebpage2 = BeautifulSoup(webpage_in2.content, 'html.parser')
current_ethereum_price = htmldataforwebpage2.td
print(str(current_ethereum_price) + " is the current Ethereum price (in USD)")

webpage_in3 = requests.get("https://coinmarketcap.com/currencies/cardano/",)
webpage3 = webpage_in3.content
htmldataforwebpage3 = BeautifulSoup(webpage_in3.content, "html.parser")
current_cardano_price = htmldataforwebpage3.td
print(str(current_cardano_price) + " is the current Cardano price (in USD)")

webpage_in4 = requests.get("https://coinmarketcap.com/currencies/binance-coin/")
webpage4 = webpage_in4.content
htmldataforwebpage4 = BeautifulSoup(webpage_in4.content, "html.parser")
current_binancecoin_price = htmldataforwebpage4.td
print(str(current_binancecoin_price) + " is the current Binance Coin price (in USD)")

webpage_in5 = requests.get("https://coinmarketcap.com/currencies/tether/")
webpage5 = webpage_in5.content
htmldataforwebpage5 = BeautifulSoup(webpage_in5.content, "html.parser")
current_tether_price = htmldataforwebpage5.td
print(str(current_tether_price) + " is the current Tether price (in USD)")

webpage_in6 = requests.get("https://coinmarketcap.com/currencies/solana/")
webpage6 = webpage_in6.content
htmldataforwebpage6 = BeautifulSoup(webpage_in6.content, "html.parser")
current_solana_price = htmldataforwebpage6.td
print(str(current_solana_price) + " is the current Solana price (in USD)")