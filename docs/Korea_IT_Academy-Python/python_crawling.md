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

Selenium은 직접 웹 브라우저를 제어하는 python 모듈로, 다양한 웹 제어, 크롤링에 사용할 수 있습니다.

- 사용 예
    - 실시간 데이터 등 동적 데이터 크롤링
    - 티켓팅 메크로 등 웹 제어를 통한 기능 구현



- Import
    - 주로 사용하는 selenium 모듈, 함수 등을 선언
    - 필요 시 BeautifulSoup를 사용해 페이지 소스를 사용
    - time 함수를 통해 python 동작 시간을 제어, 로딩 interval을 제어한다.

```py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from bs4 import BeautifulSoup
import time
```

- 브라우저 열기

```py
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)
```

- 주소 접속

```py
driver.get("https://www.naver.com")
```

- 검색 창 선택

```py
search_box = driver.find_element(By.CSS_SELECTOR, "input#query.search_input")
```

- 검색 단어 입력

```py
search_box.send_keys("힙합") 
```

- 검색 클릭

```py
search_box.send_keys(Keys.ENTER)
time.sleep(2)
```

- 뉴스 탭 클릭

```py
news_tab = driver.find_element(By.LINK_TEXT, "뉴스")
news_tab.click()
time.sleep(2)
```

- BeautifulSoup를 사용한 소스 제어 및 원하는 데이터 크롤링

```py
html = driver.page_source
soup = BeautifulSoup(html, "lxml")

# 뉴스 제목 span 태그 선택
title_spans = soup.select("span.sds-comps-text-type-headline1")

print(f"총 {len(title_spans)}개의 뉴스 제목을 찾았습니다.\n")

for i, title_span in enumerate(title_spans, 1):
    print(f"{i}. {title_span.get_text(strip=True)}")
```

- 브라우저 닫기

```py
driver.quit()
```

#### Selenium과 BeautifulSoup을 사용한 입력한 키워드 관련 뉴스를 출력하는 프로그램
.py file 형식으로 만들어 최근 기사를 출력하는 스크립트를 만들어 사용할 수 있습니다.

- run
```bash
python main.py "파이썬"
```

- main.py

```py
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time
import sys

search_word = sys.argv[1]

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.implicitly_wait(10)

# 네이버 접속
driver.get("https://www.naver.com")

# 검색창 선택
search_box = driver.find_element(By.CSS_SELECTOR, "input#query")

# 검색어 입력 (script 실행 시 parameter로 입력)
search_box.send_keys(search_word)

# 검색 실행
search_box.send_keys(Keys.ENTER)

# 뉴스 탭 클릭
time.sleep(2)  # 페이지가 전환되는 동안 대기
news_tab = driver.find_element(By.LINK_TEXT, "뉴스")
news_tab.click()

time.sleep(2)  # 뉴스 탭 페이지 로딩 대기

from bs4 import BeautifulSoup

# 현재 페이지 HTML 가져오기
html = driver.page_source
soup = BeautifulSoup(html, "lxml")

# 뉴스 제목 span 태그 선택
title_spans = soup.select("span.sds-comps-text-type-headline1")

print(f"총 {len(title_spans)}개의 뉴스 제목을 찾았습니다.\n")

for i, title_span in enumerate(title_spans, 1):
    print(f"{i}. {title_span.get_text(strip=True)}")

driver.quit()
```