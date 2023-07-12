import requests
from bs4 import BeautifulSoup
import json

br = requests.Session()
br.headers.update({'User-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) \
                AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36 Edg/114.0.1823.67'})

stv_url = 'https://www.gismeteo.ru/weather-stavropol-5141/'

resp = br.get(stv_url)

#print(resp)
#print(f'Status Code: {resp.status_code}')

soupprop = BeautifulSoup(resp.text, "html.parser")
#print(soupprop)

tempdata = soupprop.find_all('span', class_='unit unit_temperature_c')
raindata_full = soupprop.find('div', class_='widget-row widget-row-precipitation-bars row-with-caption')
rains_array = []
for div in raindata_full:
    rains_array.append(div.text)
#print(raindata_full)

temperature = {'Сейчас': tempdata[0].text, '9:00': tempdata[10].text, '12:00': tempdata[11].text, '15:00': tempdata[12].text, '18:00' : tempdata[13].text, 'Ночью': tempdata[4].text, 'Завтра' : tempdata[5].text }
rains = {'9:00': rains_array[4], '12:00': rains_array[5], '15:00': rains_array[6], '18:00': rains_array[7]}

print(rains)
print(temperature['18:00'], rains['18:00'])


