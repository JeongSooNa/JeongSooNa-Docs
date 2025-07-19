# Python Crawling

### Summary

- requests, BeautifulSoup, Selenium 등을 활용해 웹 URL과 소스 데이터를 가져와 활용할 수 있다.

### Install

```sh
pip install requests bs4 selenium webdriver-manager
```

### BeautifulSoup를 활용한 정적 크롤링

- Basic

```py
import requests
from bs4 import BeautifulSoup

url = ''
response = requests.get(url) # GET 메소드를 사용하여 url 정보 가져오기

soup = BeautifulSoup(response.content, 'html.parser')  # HTML 정보 파싱 :: 데이터 파싱이란? 필요한 정보를 추출하여 구조화된 형태로 변환하는 과정
data = soup.select('')  # 파싱한 데이터에서 class, id 등을 활용해 데이터 추출

print(data)
```

### 파이썬 크롤링을 활용한 Wiki 개요 가져오기

- crawling_wiki.py

```py
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

```

- 실행

```sh
python crawling.py 파이썬
```

### Selenium을 활용한 동적 크롤링
