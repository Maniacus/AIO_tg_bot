import socks
import socket
import ssl
from urllib.request import Request, urlopen

r = requests.get('https://www.gismeteo.ru/weather-stavropol-5141/')

print(f'Status Code: {r.status_code}')
