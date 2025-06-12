# Class 5 - Python 조건문 & 반복문

### 조건문 if

- 특정 조건을 만족했을 때 실행할 수 있도록 조건을 주는 방법으로, if 뒤에 오는 값의 True / False 여부에 따라 내부 코드가 실행된다.
```py
a = 1
if a > 0:
    print("a는 양수 입니다.")
```

- 위와 같이 if 문에서는 조건연산자와 논리연산자를 활용하는 경우가 많다.
    - A > B : A가 B보다 크다.
    - A >= B : A가 B보다 크거나 같다.
    - A == B : A와 B가 같다.
    - A is B : A와 B가 같다.
    - A != B : A와 B가 같지 않다.
    - A is not B : A와 B가 같지 않다.
    - A in B : A가 B(리스트) 안에 포함된다.

- 중요한 것은 if 우측에 있는 조건문의 True or False 어떤 것인지 확실히 인지하는 것.

```py
a = 10
b = 20
l = [10,30,50]

if a == 10:
    print("a는 10 입니다.")

if a > b:
    print("a가 b보다 크다.")
if a < b:
    print("a가 b보다 작다.")

if a != b:
    print("a는 b와 다르다.")

if a in l:
    print("a는 l list에 포함된다.")

if a:
    print("참이다.")
if 0:
    print("거짓이다.")
# 파이썬에서 숫자의 경우 0은 False로, 0이 아닌 다른 숫자는 True로 판단한다.
```

- and 나 or 를 통해 여러 조건문을 합쳐 사용할 수 있다.

```py
if a == 10 and b == 20:
    print("a는 10이고 b는 20이다.")

if a == 10 or b == 10:
    print("a와 b 둘 중 10과 같은 것이 있다.)
```

- if 와 함께 elif, else를 사용해 조건을 확장할 수 있다.
    - if 단독으로 사용 가능하다.
    - if - else로 끝나게 사용할 수 있다.(if 조건문이거나 아니거나)
    - if 다음 elif를 사용할 경우 반드시 else가 마지막에 와야한다.

```py
a = 10

if a > 0:
    print("a는 양수입니다.")
elif a < 0:
    print("a는 음수입니다.")
else:
    print("a는 0입니다.")
```

- 꼭 기억해야 할 점은 조건문이 True면 실행, 아니면 그냥 넘어간다는 개념!

### 반복문 while

- 반복문에서는 코드의 흐름을 파악하는 것이 중요하다.
- while문 뒤의 조건문이 True인 경우 내부 코드를 계속해서 반복하는 기능

```py
while True:
    print("!!!")
    # 무한 루프에 걸리게 된다.
```

- 반드시 특정 조건을 통해 while문이 종료될 수 있도록 코드를 작성하는 것이 중요하다.

```py
count = 0

while count == 10:
    print(count)
    count += 1
```

### 반복문 for

```py
for i in range(0,10):
    print(i)

for i in [1,2,3,4,5]:
    print(i)

for i in ["짱구","철수","유리","맹구","훈이"]:
    print(i)
```

- 반복문에서 자주 사용하는 range() 함수는 나열된 숫자 리스트를 생성한다.
```py
# 0 부터 n개의 숫자 생성
range(5) # 0,1,2,3,4

# 첫번째 수 부터 두번째 수 전 까지 숫자 생성
range(0,3) # 0,1,2

# 첫번째 수 부터 두번째 수 전 까지 숫자 생성 (간격(interval) 지정)
range(0,10,2) # 0,2,4,6,8
```


- 반복문의 좌측 변수(i)는 반복문 내부에서만 사용하는 변수이다.

```py
list = [1,2,3,4,5]
for i in list:
    i = list - 1
    print(i)
print(list)
print(i) # Error
```


### 반복문 제어

- 반복문을 알고리즘으로 흐름을 조정할 수 있지만 중간에 강제 중단하거나 넘어가는 기능을 넣을 수 있다.

- continue : 반복문의 조건문으로 넘어간다.
```py
summation = 0
for i in range(1,10):
    if i // 2 == 0:
        continue
    summation += i
summation
```

- break : 반복문을 종료한다.
```py
a = 5
for i in range(0,10):
    if i == a:
        print("a는" + str(i) + "다!")
        break
    print(i)
```

### 이중 반복문

- 반복문을 중첩해 사용할 수 있다.
- 헷갈릴 수 있으나 자주 사용하는 방법으로 알고리즘 구현에 필수적인 요소이다.

```py
for i in range(0,10):
    print("i : " ,i)
    for j in [1,2,3,4,5]:
        print("j : ",j)
```