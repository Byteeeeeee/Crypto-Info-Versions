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

webpage_in7 = requests.get("https://coinmarketcap.com/currencies/xrp/")
webpage7 = webpage_in7.content
htmldataforwebpage7 = BeautifulSoup(webpage_in7.content, "html.parser")
current_xrp_price = htmldataforwebpage7.td
print(str(current_xrp_price) + " is the current XRP price (in USD)")

webpage_in8 = requests.get("https://coinmarketcap.com/currencies/dogecoin/")
webpage8 = webpage_in8.content
htmldataforwebpage8 = BeautifulSoup(webpage_in8.content, "html.parser")
current_dogecoin_price = htmldataforwebpage8.td
print(str(current_dogecoin_price) + " is the current Dogecoin price (such crypto, very wow)")

webpage_in9 = requests.get("https://coinmarketcap.com/currencies/polkadot/")
webpage9 = webpage_in9.content
htmldataforwebpage9 = BeautifulSoup(webpage_in9.content, "html.parser")
current_dot_price = htmldataforwebpage9.td
print(str(current_dot_price) + " is the current Polkadot price (in USD)")

webpage_in0 = requests.get("https://coinmarketcap.com/currencies/usd-coin/")
webpage0 = webpage_in0.content
htmldataforwebpage0 = BeautifulSoup(webpage_in0.content, "html.parser")
current_usdcoin_price = htmldataforwebpage0.td
print(str(current_usdcoin_price) + " is the current USD Coin price (in USD, obviously)")

webpage_in01 = requests.get("https://coinmarketcap.com/currencies/uniswap/")
webpage01 = webpage_in01.content
htmldataforwebpage01 = BeautifulSoup(webpage_in01.content, "html.parser")
current_uniswap_price = htmldataforwebpage01.td
print(str(current_uniswap_price) + " is the current Uniswap price (in USD)")

webpage_in02 = requests.get("https://coinmarketcap.com/currencies/chainlink/")
webpage02 = webpage_in02.content
htmldataforwebpage02 = BeautifulSoup(webpage_in02.content, "html.parser")
current_usdcoin_price = htmldataforwebpage02.td
print(str(current_usdcoin_price) + " is the current Chainlink price (in USD)")

webpage_in03 = requests.get("https://coinmarketcap.com/currencies/terra/")
webpage03 = webpage_in03.content
htmldataforwebpage03 = BeautifulSoup(webpage_in03.content, "html.parser")
current_terra_price = htmldataforwebpage03.td
print(str(current_terra_price) + " is the current Terra price (in USD)")

webpage_in04 = requests.get("https://coinmarketcap.com/currencies/litecoin/")
webpage04 = webpage_in04.content
htmldataforwebpage04 = BeautifulSoup(webpage_in04.content, "html.parser")
current_litecoin_price = htmldataforwebpage04.td
print(str(current_litecoin_price) + " is the current Litecoin price (in USD)")

webpage_in05 = requests.get("https://coinmarketcap.com/currencies/binance-usd/")
webpage05 = webpage_in05.content
htmldataforwebpage05 = BeautifulSoup(webpage_in05.content, "html.parser")
current_binanceusd_price = htmldataforwebpage05.td
print(str(current_binanceusd_price) + " is the current Binance USD price (in USD)")

webpage_in06 = requests.get("https://coinmarketcap.com/currencies/bitcoin-cash/")
webpage06 = webpage_in06.content
htmldataforwebpage06 = BeautifulSoup(webpage_in06.content, "html.parser")
current_btccash_price = htmldataforwebpage06.td
print(str(current_btccash_price) + " is the current Bitcoin Cash price (in USD)")

webpage_in07 = requests.get("https://coinmarketcap.com/currencies/avalanche/")
webpage07 = webpage_in07.content
htmldataforwebpage07 = BeautifulSoup(webpage_in07.content, "html.parser")
current_ava_price = htmldataforwebpage07.td
print(str(current_ava_price) + " is the current Avalanche price (in USD)")