# Class 14 - Python 유용한 내장 함수

### abs
숫자를 입력받았을 때 그 숫자의 절댓값을 리턴
```py
abs(3)
abs(-3)
abs(-1.2)
```

### all
요소가 모두 참이면 True, 거짓이 하나라도 있으면 False를 리턴
```py
all([1, 2, 3]) # True
all([1, 2, 3, 0]) # False
all([]) # True
```

### any
요소 중 하나라도 참이 있으면 True를 리턴하고 x가 모두 거짓일 때만 False를 리턴 (all(x)의 반대)
```py
any([1, 2, 3, 0]) # True
any([0, ""]) # False
any([]) # False
```

### chr
유니코드 숫자 값을 입력받아 그 코드에 해당하는 문자를 리턴하는 함수
- 유니코드 : 전 세계의 모든 문자를 컴퓨터에서 일관되게 표현하고 다룰 수 있도록 설계된 산업 표준 코드
```py
chr(97) # 'a'
chr(44032) # '가'
```

### dir
객체가 지닌 변수나 함수를 보여 주는 함수
```py
dir([1, 2, 3]) # ['append', 'count', 'extend', 'index', 'insert', 'pop',...]
dir({'1':'a'}) # ['clear', 'copy', 'get', 'has_key', 'items', 'keys',...]
```

### divmod
a, b 입력 시, a를 b로 나눈 몫과 나머지를 튜플로 리턴
```py
divmod(7, 3) # (2, 1)
7 // 3 # 2
7 % 3 # 1
```

### enumerate
enumerate는 ‘열거하다’라는 뜻으로, 순서가 있는 데이터(리스트, 튜플, 문자열)를 입력으로 받아 인덱스 값을 포함하는 enumerate 객체를 리턴한다.  
보통 for 문과 함께 사용한다.
```py
for i, name in enumerate(['body', 'foo', 'bar']):
    print(i, name)
# 0 body
# 1 foo
# 2 bar
```
- 출력으로 보이는 것과 같이 자료의 index와 값을 쉽게 알 수 있다.

### eval
문자열로 구성된 표현식을 입력으로 받아 해당 문자열을 실행한 결괏값을 리턴
```py
eval('1+2') # 3
eval("'hi' + 'a'") # 'hia'
eval('divmod(4, 3)') # (1, 1)
```

### filter
filter(함수, 반복_가능한_데이터) : 함수, 두 번째 인수로 그 함수에 차례로 들어갈 반복 가능한 데이터를 받는다. 그리고 반복 가능한 데이터의 요소 순서대로 함수를 호출했을 때 리턴값이 참인 것만 묶어서(걸러 내서) 리턴한다.
```py
# positive.py 
def positive(l): 
    result = [] 
    for i in l: 
        if i > 0: 
            result.append(i) 
    return result

print(positive([1,-3,2,0,-5,6]))

# filter1.py
def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))

# using lambda
list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6]))
```

### hex
hex(x)는 정수를 입력받아 16진수(hexadecimal) 문자열로 변환하여 리턴하는 함수이다.
```py
hex(234) # '0xea'
hex(3) # '0x3'
```

### id
id(object)는 객체를 입력받아 객체의 고유 주솟값(레퍼런스)을 리턴하는 함수이다.
```py
a = 3
id(3) # 135072304
id(a) # 135072304
b = a
id(b) # 135072304
id(4) # 135072292
```
- 3, a, b가 모두 같은 객체를 가리키고 있다.

### list
list(iterable)은 반복 가능한 데이터를 입력받아 리스트로 만들어 리턴하는 함수이다.
```py
list("python") # ['p', 'y', 't', 'h', 'o', 'n']
list((1,2,3)) # [1, 2, 3]
```
- list 함수에 리스트를 입력하면 똑같은 리스트를 복사하여 리턴한다.

### oct
oct(x)는 정수를 8진수 문자열로 바꾸어 리턴하는 함수이다
```py
oct(34) # '0o42'
oct(12345) # '0o30071'
```

### ord
ord(c)는 문자의 유니코드 숫자 값을 리턴하는 함수이다.  
ord 함수는 chr 함수와 반대로 동작한다.
```py
ord('a') # 97
ord('가') # 44032
```

### pow
pow(x, y)는 x를 y제곱한 결괏값을 리턴하는 함수이다.
```py
pow(2, 4) # 16
pow(3, 3) # 27
```

### round
round(number)는 숫자를 입력받아 반올림해 리턴하는 함수이다.
```py
round(4.6) # 5
round(4.2) # 4
```
다음과 같이 실수 5.678을 소수점 2자리까지만 반올림하여 표시할 수 있다.
```py
round(5.678, 2)
5.68
```

### sorted
sorted(iterable)는 입력 데이터를 정렬한 후 그 결과를 리스트로 리턴하는 함수이다.
```py
sorted([3, 1, 2]) # [1, 2, 3]
sorted(['a', 'c', 'b']) # ['a', 'b', 'c']
sorted("zero") # ['e', 'o', 'r', 'z']
sorted((3, 2, 1)) # [1, 2, 3]
```

### tuple
tuple(iterable)은 반복 가능한 데이터를 튜플로 바꾸어 리턴하는 함수이다. 만약 입력이 튜플인 경우에는 그대로 리턴한다.
```py
tuple("abc") # ('a', 'b', 'c')
tuple([1, 2, 3]) # (1, 2, 3)
tuple((1, 2, 3)) # (1, 2, 3)
```

### zip
zip(*iterable)은 동일한 개수로 이루어진 데이터들을 묶어서 리턴하는 함수이다.  
여기서 사용한 *iterable은 반복 가능한 데이터를 여러 개 입력할 수 있다는 의미이다.  
```py
list(zip([1, 2, 3], [4, 5, 6])) # [(1, 4), (2, 5), (3, 6)]
list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))  #[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
list(zip("abc", "def")) # [('a', 'd'), ('b', 'e'), ('c', 'f')]