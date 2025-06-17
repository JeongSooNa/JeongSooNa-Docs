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

- with as 로 불러오기
  - with와 as를 통해 쉽게 불러오고, 불러온 파일을 변수로 선언할 수 있다.
```py
with open("order.txt","r") as f:
```

- 데이터를 사용한 간단한 분석

- data.txt
```txt
이름  점수
짱구  65
철수  95
유리  80
맹구  85
훈이  70
```

```py
# 파일 불러오기기
with open("data.txt", "r") as file:

# 각 줄 추출
lines = file.readlines()

# 각 줄의 숫자 추출 및 계산
total = 0
for line in lines:
  if line.startswith("이름"):
    continue
  score = line.split()[2]
  total += score

# 평균 계산
average = total / (len(lines) - 1)
print("평균 점수는",average,"점 입니다.")
```


### 문자열 관련 함수

- string.len()
  - 문자열의 길이를 반환

- string.split()
  - 문자열을 ~~로 구분하여 잘라 List로 반환하는 함수
  - Default : 공백

- string.replace("a","b")
  - 문자열에 포함된 모든 "a"를 "b"로 바꿔주는 함수

- string.strip()
  - 문자열의 양쪽 공백을 제거
  - text를 입력할 경우 공백과 함께 끝에 위치한 해당 문자도 제거
  - string.lstrip() : 문자열의 좌측 공백 제거
  - string.rstrip() : 문자열의 우측 공백 제거

- string.upper()
  - 문자열을 대문자로 변환
- string.lower()
  - 문자열을 소문자로 변환

- string.startswith()
  - 문자열이 ~~로 시작하는 문자열인지 확인하는 함수 (True / False로 반환)
- string.endswith()
  - - 문자열이 ~~로 끝나는 문자열인지 확인하는 함수 (True / False로 반환)

- string.find()
  - 문자열에서 특정 부분 문자열이 처음 나타나는 위치의 인덱스를 반환
  - 없을 경우 -1 반환