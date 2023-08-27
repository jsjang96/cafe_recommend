import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs
import time
from selenium.webdriver import ChromeOptions

url = 'https://composecoffee.com/findstore'
options = ChromeOptions()
# options.add_argument('--headless')
driver = webdriver.Chrome(options=options)
driver.get(url)
compose = {}

for i in range(1,10):
    try:
        driver.find_element(By.CSS_SELECTOR,f'#content > div > section.storemap > div.right_info > ul > div > a:nth-child({i})').click()
        time.sleep(0.5)
        a = bs(driver.page_source).find('ul',class_='item_list')
        b = a.find_all('div',class_='item_title')
        c = a.find_all('div',class_='item_address')
        for j in zip(b,c):
            compose[j[0].text] = j[1].text
        print(i)
        time.sleep(1)
    except:
        pass
driver.get(url)
while True:
    try:
        driver.find_element(By.CSS_SELECTOR,f'#content > div > section.storemap > div.right_info > ul > div > a:nth-child(7)').click()
        time.sleep(0.5)
        a = bs(driver.page_source).find('ul',class_='item_list')
        b = a.find_all('div',class_='item_title')
        c = a.find_all('div',class_='item_address')
        for j in zip(b,c):
            compose[j[0].text] = j[1].text
        time.sleep(0.5)
    except:
        print('pause')
        break

compose_total=pd.DataFrame(compose.items(),columns=['매장명', '주소'])
compose_total.to_csv('./data/compose_2.csv',encoding='utf-8-sig')


