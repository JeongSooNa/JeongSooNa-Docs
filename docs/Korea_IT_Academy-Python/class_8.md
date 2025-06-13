# Class 8 - Python 클래스 & 모듈

### Class

-  Class란 #####

```py
class Count:
    def __init__(self):
        self.num = 0
    def increment(self):
        self.num += 1
        return self.num

cnt = Count()

# Class의 변수 사용
print(cnt.num)
# Class의 함수 사용
print(cnt.increment())
```

### Module

자료형, 함수에 대한 학습과 기초적인 알고리즘 프로그래밍 능력을 갖춘 경우 이제 실제 프로그램 개발, 툴을 제작하는데 기초가 되는 개념이 모듈(Module)입니다.  

모듈이란 함수나 변수, 클래스 등이 정의 된 하나의 파이썬 파일(.py)혹은 내부의 함수 등 기능을 의미합니다.

- 표준 모듈 : 파이썬에서 제공하는 모듈
    - 라이브러리 ⊃ 패키지 ⊃ 모듈
    - [파이썬 표준 라이브러리](https://docs.python.org/ko/3.13/library/index.html)
    - ex)
        - os.listdir() 이라는 기능인 모듈을 사용할 때
        - 라이브러리 : 파이썬 표준 라이브러리
        - 패키지 : os
        - 모듈 : os.listdir()

- 사용 방법

```python
import os

file_list = os.listdir()
print(file_list)
```

- 사용자 정의 모듈 : 사용자, 개발자가 직접 만든 파이썬 파일(.py)

- 두 개의 파이썬 파일(.py)을 만들어 불러와 사용해보자.

- test.py

```py
def hello():
    print("This is test.py")

# 입력받은 숫자가 짝수인가 홀수인가 확인
def function(num):
    result = ""
    if num % 2 == 0:
        result = "짝수"
    elif num % 2 == 1:
        result = "홀수"
    else:
        result = "입력받은 숫자가 정수가 아닙니다."
    return result
```

- main.py

```py
import test

test.hello()

print(test.function(3))
print(test.function(4))
print(test.function(1.5))
```

- 다양한 기능을 목표로 개발을 진행할 경우 위와 같이 파일을 구분하요 사용에 용이하게 구성하는 것이 바람직하다.