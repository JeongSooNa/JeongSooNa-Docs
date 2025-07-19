import requests
from bs4 import BeautifulSoup
import sys

input = sys.argv[1]
# ex) 파이썬, 커피, 공부

url = 'https://ko.wikipedia.org/wiki/'+input
response = requests.get(url)

soup = BeautifulSoup(response.content, 'html.parser')
data = soup.find('p')

print(input)
print(data.text)
