# Class 9 - Python 파일 읽고 쓰기

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

- open 함수의 옵션에는 r, w, a 가 있다.
    - r : 파일 읽기
    - w : 파일 쓰기
    - a : 파일 마지막에 내용 추가

- Text file을 만들어 실습에 사용

- test.txt

```txt
My name is JeongSoo Na
```

```py
f = open(test.txt,"r")
text = f.read()
print(text)
f.close()
```

```py
f = open(test.txt,"w")
f.write("My name is ")
f.close()
```

```py
f = open(test.txt,"a")
f.write("JeongSoo Na")
f.close()
```

- 여러 줄을 읽고 구별할 수 있어 데이터 분석에도 사용이 가능

- order.txt
```txt
id  menu    price
1   pizza   10$
2   chicken 15$
3   hamburger   5$
```

- 전체 데이터를 한번에 읽기

```py
f = open("order.txt","r")
full = f.read()
print(full)

text_list = full.split("\n")
print(text_list)

header = text_list[0]
contents = text_list[1:]



f.close()
```


- 한줄 씩 읽어오기

```py
f = open("order.txt","r")
line = f.readline()
print(line)
line = f.readline()
print(line)
line = f.readline()
print(line)
line = f.readline()
print(line)
f.close()
```

- 여러 줄의 리스트로 읽기

```py
f = open("order.txt","r")
lines = f.readlines()
print(lines)
f.close()
```


- 데이터를 사용한 간단한 분석

```py
# read()를 사용한 전체 데이터를 활용한 데이터 분석

# readline()을 사용한 

```