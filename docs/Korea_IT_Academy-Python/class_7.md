# Class 7 - Python 함수

![jpg](../img/function_ex.png)

### 함수 정의
- 함수는 복잡한 코드를 묶고, 반복되는 코드를 줄이기 위해 사용한다.
- 입력(Input)과 출력(Output)이 가장 중요한 개념

- 기본 함수
- def(definition) : 함수 정의
- 마지막에 ":" 후 들여쓰기로 내부 소스 작성
- 들여쓰기가 틀릴 경우 에러가 발생
- 괄호 () 안에 입력값(Input, Parameter(인자))을 넣어 함수 내부로 전달
```py
def plus_one(a):
    # 함수 내부 기능
    result = a + 1
    # 반환값(Output)
    return result

plus_one(1)
```

- 입력값과 반환값은 생략이 가능하다. (내부 기능 사용만도 가능)
```py
def shouting():
    print("ah!!!!")

shouting()
```

- 함수를 선언할 때 인자의 타입을 특정하거나 기본 값을 명시할 수 있다.
> Default : 지정된 초기값

```py
# 타입 특정
def function_1(a: str, b: int):
    print(a + "의 갯수는 " + str(b) + "개 입니다.")

function_1("사과",10)

# Default 값 명시
def function_2(a = "소주"):
    print(a + "한 병 주문이요")

function_2()
function_2("맥주")

# 동시에 가능
def function_3(a: int = 1, b: int = 2):
    print(a + b)

function_3()
function_3(2,3)
```

### 함수의 출력
- 위의 함수에서 출력되는 print()는 사실 함수 내부 기능의 일부로 실제 출력은 return을 사용한다.
```py
def summation(a,b):
    return a + b

summation(1,2)
```

### 함수 내부의 변수
- 함수 내부와 외부는 구분이 되어 있어 함수 내부에서 정의한 변수는 함수 내부에서만 사용이 가능하다.
```py
def function_4(a,b):
    c = a + b
    return c

print(function_4(1,2))
print(c) # Error (변수 c는 함수 내부에서 정의한 변수이므로 외부에서는 사용 불가능.)
```

- 외부에서 정의한 변수는 함수 내부에서도 사용이 가능하다.
```py
a = 1
def function_5(b):
    c = a + b # 변수 a는 함수 외부에서 정의한 변수로 내부에서도 사용이 가능하다.
    return c

print(function_5(2))
```

- 다음과 같이 함수 내부에서 변수의 값을 새로 정의하더라도 기존 외부에서 정의한 변수에 영향을 끼치지 않는다. (내부 선언 변수는 내부에서만 사용하는 변수로 이름이 같아도 서로 다른 변수로 인식한다.)
```py
a = 1
def function_6():
    a = 2
    print(a)
print(a)
```

### 함수의 사용
- 중복 코드를 줄이기 위해 사용하는 함수는 다른 함수 내부에서도 사용이 가능하다.
```py
def function_7(a,b):
    return a + b

print(function_7(1,2))

def function_8(a,b):
    c = function_7(a,b)
    return c * 2

print(function_8(1,2))
```
- 이렇게 함수 내부에서 다른 함수를 사용하는 것을 참조라고 하는데, 서로 참조를 하여 사용할 경우 무한루프에 걸려 에러가 발생할 수 있다. (조심!)
```py
def function_9():
    function_10()

def function_10():
    function_9()

function_9() # Error
# function_9 실행 시 function_9 > function_10 > function_9 > ... 이렇게 무한루프에 걸릴 수 있다.