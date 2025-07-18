# Python Back-end

### Summary
- Flask Library를 통한 파이썬 웹 프로그래밍으로 간단한 웹 제작 및 통신을 할 수 있다.

- 세부 목표
    - Flask 사용 python script 포함 파일 구성 및 간단한 웹 페이지 구현
    - 웹 기능 구현
        - 비동기 웹 페이지 구현
            - 웹 페이지 연결 시 현재 상태 출력
        - 동기 웹 페이지 구현
            - 웹 페이지에서 받은 Input을 통해 기능 script를 활용한 웹 페이지 Output 출력
            - 실시간 데이터를 활용한 웹 페이지 출력

### Flask

flask 란 웹 개발을 위해 제공되는 Python Library(특정 형식으로 구성되며, 기능을 제공하는 프레임워크 라고도 한다.)로, Python 웹 개발(주로 스타트업) 혹은 간단한 서비스 제공을 위한 실무에서 많이 사용된다.

- Install

```sh
pip install flask
```

- Import & Setting (main.py)

```py
# main.py

# Import Flask
from flask import Flask

# Flask 웹 호출 정의
app = Flask(__name__)

# "/" 최 상위 경로 웹 페이지 지정
@app.route('/')
def index():
    # 웹 페이지에 띄울 Return
    return "Hello World!"

# main python script 동작 시 웹 호출 변수 동작 선언
if __name__ == '__main__':
    # app.run() # Default : 127.0.0.1:5000
    app.run(host='0.0.0.0',port=9999)
    # IP 0.0.0.0으로 설정 시 같은 네트워크의 모든 서버에서 접근이 가능
    # port 설정도 가능하다.
```

- run

```sh
python app.py
```

- 위의 기본적인 구성 및 스크립트를 실행 후 ```localhost:5000``` 혹은 ```127.0.0.1:5000```을 통해 웹을 열 경우 return되는 데이터를 확인할 수 있다.

- python script 실행 중일때만 웹 접근이 가능한 것을 확인

---

### 비동기 웹페이지 구현

- 일방적인 자료 전달, 포스팅 등 보여주기만을 위해 사용되는 방식으로, 움직임, 동작이 있지 않음.
- 주로 포트폴리오, 데이터 전달, 공시 등에 쓰이며 사용에 제한이 있다.

- 간단한 HTML file을 연결해 웹에 띄워보자.

```py
# main.py
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("test.html")

if __name__ == '__main__':
    app.run()
```

---

### 동기 웹페이지 구현

- 일반적인 파이썬 백앤드 환경의 경우 HTTP Request Method를 사용해 프론트(웹)와 백앤드 환경 간 통신을 한다.
    - HTTP Request Method
        - GET : 리소스 조회, 데이터를 가져올 때 사용 (서버 > 웹)
        - POST : 서버로 데이터 전송 (웹 > 서버)
        - PUT : 요청 데이터를 사용해 새로운 리소스, 데이터 생성
        - PATCH : 리소스, 데이터 변경
        - DELETE : 리소스, 데이터 삭제

- index.html을 만들어 동기 웹 페이지를 만들어보자.

#### 웹 페이지에서 받은 Input을 통해 기능 script를 활용한 웹 페이지 Output 출력

- templates 등 트리 구조를 잘 구성 해야 동작한다.

- Python script

```py
# main.py

# Import Flask
from flask import Flask, render_template, request

# Flask 웹 호출 정의
app = Flask(__name__)

# "/" 최 상위 경로 웹 페이지 지정
@app.route('/')
def index():
    # index.html을 return
    return render_template("index.html")

# 웹 데이터 불러오기
@app.route('/data', methods=['POST'])
def get_data():
    input_data = request.form.get("input_data") # 입력받은 데이터
    return f"<h3>입력된 데이터: {input_data}</h3>"

# main python script 동작 시 웹 호출 변수 동작 선언
if __name__ == '__main__':
    # app.run() # Default : 127.0.0.1:5000
    app.run(host='0.0.0.0',port=9999)
    # IP 0.0.0.0으로 설정 시 같은 네트워크의 모든 서버에서 접근이 가능
    # port 설정도 가능하다.
```

- HTML

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Python Flask Back-end Web Developments</title>
</head>
<body>
  <!-- 입력란 -->
  <input id="input_data" type="text" />
  <!-- 전송 버튼 -->
  <button onclick="send()">전송</button>
  <!-- 파이썬에서 가져온 데이터를 출력 할 영역 -->
  <div id="result"></div>

  <script>
    // 버튼 클릭 시 작동 함수
    function send() {
      // data 변수 선언
      const data = new FormData();
      // id input_data를 data에 저장
      data.append('input_data', document.getElementById('input_data').value);
      // /data 에 input_data를 전송하여 python 서버로 전달
      fetch('/data', {
        method: 'POST', // POST method로 전송
        body: data
      })
      .then(response => response.text()) // 서버 응답 시 text로 처리
      .then(text => {
        document.getElementById('result').innerHTML = text; // 전달 받은 데이터를 id result에 넣기
      });
    }
  </script>
</body>
</html>
```

#### 기능 script를 사용한 로또 번호 추천 기능 구현하기

- 로또 번호를 랜덤하게 추출하여 뽑는 lotto.py를 구현한 후 main.py에서 불러와 웹과 통신하여 로또 번호를 추첨하는 웹 서비스 제공

- main.py

```py
# main.py

# Import Flask
from flask import Flask, render_template, request
import lotto

# Flask 웹 호출 정의
app = Flask(__name__)

# 로또 페이지
@app.route('/lotto')
def lotto_index():
    return render_template("lotto.html")

@app.route('/lotto_data')
def get_lotto():
    numbers = lotto.lotto_number()
    return '추천 번호: ' + ', '.join(map(str, numbers))

# main python script 동작 시 웹 호출 변수 동작 선언
if __name__ == '__main__':
    # app.run() # Default : 127.0.0.1:5000
    app.run(host='0.0.0.0',port=9999)
    # IP 0.0.0.0으로 설정 시 같은 네트워크의 모든 서버에서 접근이 가능
    # port 설정도 가능하다.
```

- lotto.py

```py
import random

def lotto_number():
    lotto_li = list(range(1,46))
    lotto = sorted(random.sample(lotto_li, 6))
    return lotto
```

- lotto.html

```html
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lotto</title>
</head>
<body>
  <h1>로또 번호를 추천합니다.</h1>
  <button onclick="run()">추첨</button>
  <div id="result"></div>

  <script>
    function run() {
      fetch('/lotto_data')
        .then(response => response.text())
        .then(text => {
          document.getElementById('result').innerHTML = text;
        });
    }
  </script>
</body>
</html>

```

#### 심화 과정

- 웹 개발
    - HTML
    - CSS
    - JS(Javascript)

- Jinja2 템플릿을 활용한 웹 개발
    - Python으로 HTML 코드 제어
    - 반복문, 조건문, 변수 등을 구성하고 제어하는데 효율적이다.