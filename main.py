import requests
from bs4 import BeautifulSoup
import sys
import csv

def car_scrape(search_string):
    resp = requests.get(search_string)
    soup = BeautifulSoup(resp.text, 'lxml')
    car_name = soup.find('h1', attrs = {'class': 'col-8 details-title'})
    car_price = soup.find('div', attrs = {'class': 'price-value'})
    car_power_kw = soup.find('div', attrs = {'id': 'description-power-0'})
    car_power_torque = soup.find('div', attrs = {'id': 'description-torque-0'})
    car_engine_code = soup.find('div', attrs = {'id': 'description-engine-code-0'})
    car_engine_induction = soup.find('div', attrs = {'id': 'description-induction-0'})
    car_engine_cylinders = soup.find('div', attrs = {'id': 'description-cylinders-0'})
    car_drive_type = soup.find('div', attrs = {'id': 'description-drive-0'})
    with open('index.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([car_name.text.strip(),
                         car_price.text.strip().replace("*", ""),
                         car_power_kw.text.strip(),
                         car_power_torque.text.strip(),
                         car_engine_code.text.strip(),
                         car_engine_induction.text.strip(),
                         car_engine_cylinders.text.strip(),
                         car_drive_type.text.strip(),
                         search_string])


if len(sys.argv) == 1:
    car_scrape(input('URL to listing: '))
else:
    car_scrape(sys.argv[1])
