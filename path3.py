import time
from selenium import webdriver
from selenium.webdriver.common.by import By
import csv
import pandas as pd

browser = webdriver.Chrome()
parsed_data = []
url = "https://www.divan.ru/kazan/category/divany-i-kresla"
def append_parsed_data(url):
    browser.get(url)
    time.sleep(10)

    prices = browser.find_elements(By.CSS_SELECTOR, "div._Ud0k")
    for price in prices:
        try:
            price = price.find_element(By.CSS_SELECTOR,"div.q5Uds").find_element(By.TAG_NAME,"span").text
            price = price.strip('руб.') #убираем символы руб
            price = "".join(price.split()) #убираем пробел между разрядами: 20 100 -> 20100
            price = float(price) #переводим в число
        except:
              print("Произошла ошибка при парсинге")
              continue
        parsed_data.append([price])


#Функция для записи в файл
def write_data_to_csv(parsed_data,filename):
    with open(filename,'w',encoding='utf-16') as file:
        writer = csv.writer(file)
        writer.writerow(['Цена'])
        writer.writerows(parsed_data)
    print("File was written")

append_parsed_data(url)

browser.quit()

#Записываем данные в файл
write_data_to_csv(parsed_data,'prices.csv')

#df = pd.read_csv('prices.csv')
#print(f'Средняя цена - {df['Цена'].mean()}')



















# "ui-LD-ZU KIkOH"