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
