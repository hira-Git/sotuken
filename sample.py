import requests
from bs4 import BeautifulSoup
import re

url = "https://morijyobi.ac.jp/"
response = requests.get(url)
# html全文表示
print(response.text[:500])

search = BeautifulSoup(response.text,'html.parser')
result = search.find_all("title")
# result = search.findall(class=re.compile("items-box-name"))
# result = search.find_all('title')
print(result)

url = "https://www.mercari.com/jp/u/952517965/"
response = requests.get(url)
print(response.text)
search = BeautifulSoup(response.text,'html.parser')
result = search.find_all(href=re.compile("/jp/items/m"))
# result = search.findall(class=re.compile("items-box-name"))
# result = search.find_all('title')
print(result)
