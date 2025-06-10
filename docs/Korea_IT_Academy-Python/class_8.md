# Class 8 - Python 파일 읽고 쓰기

### 파일 위치(PATH) 이해
- python에서 외부 파일을 읽어오기 위해서는 경로에 대한 이해가 필요하다.
- 최상위 경로 : /
- 현재 경로 : ./
- 상위 경로 : ../
- 절대 경로 vs 상대 경로
    - 절대 경로 : 최상위 경로(/)를 기준으로 나타내는 경로
        - ex) "/C:/user/JeongSooNa/Desktop/test/test.py"
    - 상대 경로 : 현재 본인의 경로(./)룰 기준으로 나타내는 경로
        - ex) "test/test.py"

### open
- open을 통해 외부 파일을 읽어올 수 있다.
- test.txt
```txt
Hello World!
```
```py
f = open(test.txt,"r")
text = f.read()
print(text)
```

- open 함수의 옵션에는 