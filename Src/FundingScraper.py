from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from time import sleep
import random

options = Options()
#options.headless = True
driver = webdriver.Chrome()
driver.get('https://www.viewbase.com/funding')

def getBTCFunding():
    string = "```USD/USDT futures: \nBinance\tBybit\t  FTX\t    Huobi\t  Okex   \n"
    element = driver.find_element_by_id('Binance-BTCUSDT')
    string += element.text + "\t"
    element = driver.find_element_by_id('Bybit-BTCUSDT')
    string += element.text + "\t"
    element = driver.find_element_by_id('FTX-BTC-PERP')
    string += element.text + "\t"
    element = driver.find_element_by_id('Huobi-BTC-USDT')
    string += element.text + "\t"
    element = driver.find_element_by_id('Okex-BTC-USDT-SWAP')
    string += element.text + "\n"

    string += "Coin futures: \nBinance\t Bybit\t   Bitmex\t Huobi\t  Okex   \n"
    element = driver.find_element_by_id('Binance-BTCUSD_PERP')
    string += element.text + "\t "
    element = driver.find_element_by_id('Bybit-BTCUSD')
    string += element.text + "\t "
    element = driver.find_element_by_id('Bitmex-BTCUSD')
    string += element.text + "\t"
    element = driver.find_element_by_id('Huobi-BTC-USD')
    string += element.text + "\t"
    element = driver.find_element_by_id('Okex-BTC-USD-SWAP')
    string += element.text + "\n```"
    return string

def getETHFunding():
    string = "```USD/USDT futures: \nBinance\tBybit\t  FTX\t    Huobi\t  Okex   \n"
    element = driver.find_element_by_id('Binance-ETHUSDT')
    string += element.text + "\t"
    element = driver.find_element_by_id('Bybit-ETHUSDT')
    string += element.text + "\t"
    element = driver.find_element_by_id('FTX-ETH-PERP')
    string += element.text + "\t"
    element = driver.find_element_by_id('Huobi-ETH-USDT')
    string += element.text + "\t"
    element = driver.find_element_by_id('Okex-ETH-USDT-SWAP')
    string += element.text + "\n"

    string += "Coin futures: \nBinance\t Bybit\t  Bitmex\t Huobi\t  Okex   \n"
    element = driver.find_element_by_id('Binance-ETHUSD_PERP')
    string += element.text + "\t "
    element = driver.find_element_by_id('Bybit-ETHUSD')
    string += element.text + "\t"
    element = driver.find_element_by_id('Bitmex-ETHUSD')
    string += element.text + "\t"
    element = driver.find_element_by_id('Huobi-ETH-USD')
    string += element.text + "\t"
    element = driver.find_element_by_id('Okex-ETH-USD-SWAP')
    string += element.text + "\n```"
    return string

def getLiquidations():
    driver.get('https://www.viewbase.com/liquidation')
