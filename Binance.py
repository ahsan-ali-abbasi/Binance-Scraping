# -*- coding: utf-8 -*-
"""
Created on Tue Feb 28 23:34:34 2023

"""

import pandas as pd
import requests
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from bs4 import BeautifulSoup
import time
import re


url='https://www.binance.com/en/markets?p=1'
driver=webdriver.Chrome('C:\PythonScrapping\chromedriver.exe')

page=driver.get(url)

soup=BeautifulSoup(driver.page_source,'lxml')

page_no=1

df=pd.DataFrame({
    'Symbol':[],
    'Name':[],
    'Price':[],
    'Change %':[],
    '24h Volume':[],
    'Market Cap':[],
    'URL':[]
    })

Symbols=[]
Names=[]
Prices=[]
Changes=[]
Volumes=[]
MarketCaps=[]
URLs=[]

coins=soup.find_all('div',class_='css-vlibs4')

# No of pages of Binance you want to scrape.
iterations=8

j=0
while j<iterations:
    i=1
    for c in coins:
        c_url="https://www.binance.com"+c.find('a',class_='css-t4pmgu').get('href')
        
        # If you want to save image of each coin.
        image=driver.find_element_by_xpath('//*[@id="tabContainer"]/div[2]/div[2]/div/div[2]/div['+str(i)+']/div/a/div[1]').screenshot('C:/Users/aa255165/OneDrive - Teradata/Desktop/Python WS/Screenshots/Binance'+str(page_no)+'-'+str(i)+'.png')
        
        coin_name=c.find('div',class_='css-1x8dg53').text
        name=c.find('div',class_='css-1ap5wc6').text 
        price=c.find('div',class_='css-ydcgk2').text
        ChangePercentage=c.find('div',class_='css-18yakpx').text    
        Volume=c.find('div',class_='css-102bt5g').text
        MarketCap=c.find('div',class_='css-s779xv').text
        
        Symbols.append(coin_name)
        Names.append(name)
        Prices.append(price)
        Changes.append(ChangePercentage)
        Volumes.append(Volume)
        MarketCaps.append(MarketCap)
        URLs.append(c_url)
         
        #print(page_no,':',i,' ',c_url,' ',coin_name,' ',name,' ',price,' ',ChangePercentage,' ',Volume,' ',MarketCap,'\n')
    
        i+=1
        
    next_page=driver.find_element_by_xpath('//*[@id="next-page"]').click()
    soup=BeautifulSoup(driver.page_source,'lxml')
    coins=soup.find_all('div',class_='css-vlibs4')
    
    j+=1
    page_no+=1


df=pd.DataFrame({
    'Symbol':Symbols,
    'Name':Names,
    'Price':Prices,
    'Change %':Changes,
    '24h Volume':Volumes,
    'Market Cap':MarketCaps,
    'URL':URLs
    })


