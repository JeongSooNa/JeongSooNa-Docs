# Class 6 - Python 입출력

### input

- input() 함수를 통해 사용자로부터 변수의 값을 입력받을 수 있습니다.

- input()으로 입력받은 값은 모두 문자(str)로 인식.

```py
name = input()
print("저의 이름은 " + name + "입니다.")
```

```py
apple = input("사과는 몇 개?")
banana = input("바나나는 몇 개?")
orange = input("오렌지는 몇 개?")
sum = int(apple) + int(banana) + int(orange)
print("과일은 총 " + str(sum) + "개 입니다.")
```

### argv

- 실제로는 쓰이는 일이 많지 않으나 웹이나 OS시스템, 다른 프로그램과 연동되지 않은 python 단독 서비스에 가끔 사용됩니다.
- 실제 직무 및 서비스에서는 input() 함수를 사용하는 것 보다 미리 정해진 parameter(인자)를 받아 동작하는 방식을 선호합니다.
- main.py
```py
import sys
name = sys.argv[1]
print("저의 이름은 " + name + "입니다.")
```
- 실행
```sh
python main.py JeongSooNa
```

### argparse

- python으로 개발한 툴의 경우 사용자의 편의와 확장성을 위해 argparse를 사용합니다.
- argparse는 단순히 parameter(인자)를 받는 기능 외에 다양한 기능을 제공합니다.
    - Default 지정 기능
        > Default란? 기본값, 초깃값 등 따로 값을 지정하지 않으면 제공하는 값을 의미
    - help 기능
    - parameter(인자) name 지정
    - 다양한 옵션 및 설명 기능 제공
- main.py
```py
import argparse

parser = argparse.ArgumentParser(description='나의 정보')
parser.add_argument('name', help='이름을 입력하세요')
parser.add_argument('-a', '--age', help='나이를 입력하세요', default=20, type=int)
args = parser.parse_args()

print("제 이름은 " + args.name + "이고, 나이는 " + str(args.age) + "살 입니다.")
```
- 실행
```sh
main.py --name "나정수" -a 32
```


### print

- pen pineapple apple pen 출력해보기
```py
print("pen pineapple apple pen")
print("pen""pineapple""apple""pen")
print("pen","pineapple","apple","pen")
print("pen"+"pineapple"+"apple"+"pen")

print("pen")
print("pineapple")
print("apple")
print("pen")

print("pen", end=' ')
print("pineapple", end=' ')
print("apple", end=' ')
print("pen", end=' ')

print("pen", end='\n')
print("pineapple", end='\n')
print("apple", end='\n')
print("pen", end='\n')
```