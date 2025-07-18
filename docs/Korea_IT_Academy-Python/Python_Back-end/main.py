# main.py

# Import Flask
from flask import Flask, render_template, request
import lotto


# Flask 웹 호출 정의
app = Flask(__name__)

# Test
@app.route('/test')
def test():
    # 웹 페이지에 띄울 Return
    return render_template("test.html")

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