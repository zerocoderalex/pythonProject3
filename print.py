import time
import csv
from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://tomsk.hh.ru/vacancies/programmist"

driver.get(url)

time.sleep(3)

vacancies = driver.find_elements(By.CLASS_NAME, 'vacancy-card--H8LvOiOGPll0jZvYpxIF')

print(vacancies)
parsed_data = []
for vacancy in vacancies:
    try:
        title = vacancy.find_elements(By.CSS_SELECTOR, 'span.vacancy-name--SYbxrgpHgHedVTkgI_cA').text
        salary = vacancy.find_elements(By.CSS_SELECTOR, 'span.compensation-text--cCPBXayRjn5GuLFWhGTJ').text
        link = vacancy.find_elements(By.CSS_SELECTOR, 'a.bloko-link').get_attribute('href')
    except:
        print('Произошла ошибка парсинга')
        continue

    parsed_data.append([title, salary, link])

driver.quit()

with open("hh.csv", 'w', newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(['Название вакансии', 'зарплата', 'ссылка на вакансию'])
    writer.writerows(parsed_data)
