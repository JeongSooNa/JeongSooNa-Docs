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

다음 예를 살펴보자.

# positive.py 
def positive(l): 
    result = [] 
    for i in l: 
        if i > 0: 
            result.append(i) 
    return result

print(positive([1,-3,2,0,-5,6]))
[실행 결과]

[1, 2, 6]
위에서 만든 positive는 리스트를 입력으로 받아 각각의 요소를 판별해서 양수 값만 리턴하는 함수이다.

filter 함수를 사용하면 위 내용을 다음과 같이 간단하게 작성할 수 있다.

# filter1.py
def positive(x):
    return x > 0

print(list(filter(positive, [1, -3, 2, 0, -5, 6])))
[실행 결과]

[1, 2, 6]
filter(positive, [1, -3, 2, 0, -5, 6])은 [1, -3, 2, 0, -5, 6]의 각 요솟값을 순서대로 positive 함수에 적용하여 리턴값이 참인 것만 묶어서 리턴한다. 즉, 1, 2, 6 요소만 x > 0 문장에 참이 되므로 [1, 2, 6]이라는 결괏값이 출력된다.

list 함수는 filter 함수의 리턴값을 리스트로 출력하기 위해 사용했다.

이 예제는 lambda를 사용하면 더욱 간단해진다.


>>> list(filter(lambda x: x > 0, [1, -3, 2, 0, -5, 6]))
[1, 2, 6]
hex
hex(x)는 정수를 입력받아 16진수(hexadecimal) 문자열로 변환하여 리턴하는 함수이다.

>>> hex(234)
'0xea'
>>> hex(3)
'0x3'
id
id(object)는 객체를 입력받아 객체의 고유 주솟값(레퍼런스)을 리턴하는 함수이다.

>>> a = 3
>>> id(3)
135072304
>>> id(a)
135072304
>>> b = a
>>> id(b)
135072304
위 예의 3, a, b는 고유 주솟값이 모두 135072304이다. 즉, 3, a, b가 모두 같은 객체를 가리키고 있다.

만약 id(4)라고 입력하면 4는 3, a, b와 다른 객체이므로 당연히 다른 고유 주솟값이 출력된다.

>>> id(4)
135072292
input
input([prompt])는 사용자 입력을 받는 함수이다. 입력 인수로 문자열을 전달하면 그 문자열은 프롬프트가 된다.

[]는 괄호 안의 내용을 생략할 수 있다는 관례 표기법이라는 것을 기억하자.

>>> a = input()
hi
>>> a
'hi'
>>> b = input("Enter: ")
Enter: hi
>>> b
'hi'
int
int(x)는 문자열 형태의 숫자나 소수점이 있는 숫자를 정수로 리턴하는 함수이다. 만약 정수가 입력되면 그대로 리턴한다.

>>> int('3')
3
>>> int(3.4)
3
int(x, radix)는 radix 진수로 표현된 문자열 x를 10진수로 변환하여 리턴한다. 예를 들어 2진수로 표현된 '11'의 10진수 값은 다음과 같이 구할 수 있다.


>>> int('11', 2)
3
16진수로 표현된 '1A'의 10진수 값은 다음과 같이 구할 수 있다.

>>> int('1A', 16)
26
isinstance
isinstance(object, class) 함수는 첫 번째 인수로 객체, 두 번째 인수로 클래스를 받는다. 입력으로 받은 객체가 그 클래스의 인스턴스인지를 판단하여 참이면 True, 거짓이면 False를 리턴한다.

>>> class Person: pass
...
>>> a = Person()
>>> isinstance(a, Person)
True
위 예는 a 객체가 Person 클래스에 의해 생성된 인스턴스라는 것을 확인시켜 준다.

>>> b = 3
>>> isinstance(b, Person)
False
b는 Person 클래스로 만든 인스턴스가 아니므로 False를 리턴한다.

len
len(s)는 입력값 s의 길이(요소의 전체 개수)를 리턴하는 함수이다.

>>> len("python")
6
>>> len([1,2,3])
3
>>> len((1, 'a'))
2
list
list(iterable)은 반복 가능한 데이터를 입력받아 리스트로 만들어 리턴하는 함수이다.

>>> list("python")
['p', 'y', 't', 'h', 'o', 'n']
>>> list((1,2,3))
[1, 2, 3]
list 함수에 리스트를 입력하면 똑같은 리스트를 복사하여 리턴한다.

>>> a = [1, 2, 3]
>>> b = list(a)
>>> b
[1, 2, 3]
map

map(f, iterable)은 함수(f)와 반복 가능한 데이터를 입력으로 받는다. map은 입력받은 데이터의 각 요소에 함수 f를 적용한 결과를 리턴하는 함수이다.

다음 예를 살펴보자.

# two_times.py
def two_times(numberList):
    result = []
    for number in numberList:
        result.append(number*2)
    return result

result = two_times([1, 2, 3, 4])
print(result)
two_times는 리스트를 입력받아 리스트의 각 요소에 2를 곱해 리턴하는 함수이다. 실행 결과는 다음과 같다.

[2, 4, 6, 8]
위 예제는 map 함수를 사용하여 다음처럼 바꿀 수 있다.

>>> def two_times(x): 
...     return x*2
...
>>> list(map(two_times, [1, 2, 3, 4]))
[2, 4, 6, 8]
이 예제를 해석해 보자. 먼저 리스트의 첫 번째 요소인 1이 two_times 함수의 입력값으로 들어가고 1 * 2의 과정을 거쳐서 2가 된다. 다음으로 리스트의 두 번째 요소인 2가 2 * 2의 과정을 거쳐 4가 된다. 따라서 결괏값은 이제 [2, 4]가 된다. 총 4개의 요솟값이 모두 수행되면 [2, 4, 6, 8]이 된다. 이것이 map 함수가 하는 일이다.

map 함수의 결과를 리스트로 출력하기 위해 list 함수를 사용했다. map 함수는 map 객체를 리턴한다.

앞의 예는 lambda를 사용하여 다음처럼 간략하게 만들 수 있다.

>>> list(map(lambda a: a*2, [1, 2, 3, 4]))
[2, 4, 6, 8]
max
max(iterable)은 인수로 반복 가능한 데이터를 입력받아 그 최댓값을 리턴하는 함수이다.

>>> max([1, 2, 3])
3
>>> max("python")
'y'
min
min(iterable)은 max 함수와 반대로, 인수로 반복 가능한 데이터를 입력받아 그 최솟값을 리턴하는 함수이다.

>>> min([1, 2, 3])
1
>>> min("python")
'h'
oct

oct(x)는 정수를 8진수 문자열로 바꾸어 리턴하는 함수이다

>>> oct(34)
'0o42'
>>> oct(12345)
'0o30071'
open
open(filename, [mode])은 ‘파일 이름’과 ‘읽기 방법’을 입력받아 파일 객체를 리턴하는 함수이다. 읽기 방법(mode)을 생략하면 기본값인 읽기 모드(r)로 파일 객체를 만들어 리턴한다.

mode	설명
w	쓰기 모드로 파일 열기
r	읽기 모드로 파일 열기
a	추가 모드로 파일 열기
b	바이너리 모드로 파일 열기
b는 w, r, a와 함께 사용한다. 예를 들어 rb는 ‘바이너리 읽기 모드’를 의미한다.

>>> f = open("binary_file", "rb")
ord
ord(c)는 문자의 유니코드 숫자 값을 리턴하는 함수이다.

ord 함수는 chr 함수와 반대로 동작한다.

>>> ord('a')
97
>>> ord('가')
44032
pow
pow(x, y)는 x를 y제곱한 결괏값을 리턴하는 함수이다.

>>> pow(2, 4)
16
>>> pow(3, 3)
27
range
range([start,] stop [,step])은 for 문과 함께 자주 사용하는 함수이다. 이 함수는 입력받은 숫자에 해당하는 범위 값을 반복 가능한 객체로 만들어 리턴한다.

인수가 하나일 경우
시작 숫자를 지정해 주지 않으면 range 함수는 0부터 시작한다.

>>> list(range(5))
[0, 1, 2, 3, 4]
인수가 2개일 경우
입력으로 주어지는 2개의 인수는 시작 숫자와 끝 숫자를 나타낸다. 단, 끝 숫자는 해당 범위에 포함되지 않는다는 것에 주의하자.

>>> list(range(5, 10))
[5, 6, 7, 8, 9]
인수가 3개일 경우
세 번째 인수는 숫자 사이의 거리를 말한다.

>>> list(range(1, 10, 2))
[1, 3, 5, 7, 9]
>>> list(range(0, -10, -1))
[0, -1, -2, -3, -4, -5, -6, -7, -8, -9]
round
round(number [,ndigits])는 숫자를 입력받아 반올림해 리턴하는 함수이다.

[,ndigits]는 ndigits가 있을 수도 있고, 없을 수도 있다는 의미이다.

>>> round(4.6)
5
>>> round(4.2)
4
다음과 같이 실수 5.678을 소수점 2자리까지만 반올림하여 표시할 수 있다.

>>> round(5.678, 2)
5.68
round 함수의 두 번째 인수는 반올림하여 표시하고 싶은 소수점의 자릿수(ndigits)를 의미한다.

sorted
sorted(iterable)는 입력 데이터를 정렬한 후 그 결과를 리스트로 리턴하는 함수이다.

>>> sorted([3, 1, 2])
[1, 2, 3]
>>> sorted(['a', 'c', 'b'])
['a', 'b', 'c']
>>> sorted("zero")
['e', 'o', 'r', 'z']
>>> sorted((3, 2, 1))
[1, 2, 3]
리스트 자료형에도 sort 함수가 있다. 하지만 리스트 자료형의 sort 함수는 리스트 객체 그 자체를 정렬만 할 뿐, 정렬된 결과를 리턴하지는 않는다.

str
str(object)는 문자열 형태로 객체를 변환하여 리턴하는 함수이다.

>>> str(3)
'3'
>>> str('hi')
'hi'
sum
sum(iterable)은 입력 데이터의 합을 리턴하는 함수이다.

>>> sum([1,2,3])
6
>>> sum((4,5,6))
15
tuple
tuple(iterable)은 반복 가능한 데이터를 튜플로 바꾸어 리턴하는 함수이다. 만약 입력이 튜플인 경우에는 그대로 리턴한다.

>>> tuple("abc")
('a', 'b', 'c')
>>> tuple([1, 2, 3])
(1, 2, 3)
>>> tuple((1, 2, 3))
(1, 2, 3)
type
type(object)는 입력값의 자료형이 무엇인지 알려 주는 함수이다.

>>> type("abc")
<class 'str'>
>>> type([ ])
<class 'list'>
>>> type(open("test", 'w'))
<class '_io.TextIOWrapper'>
zip
zip(*iterable)은 동일한 개수로 이루어진 데이터들을 묶어서 리턴하는 함수이다.

여기서 사용한 *iterable은 반복 가능한 데이터를 여러 개 입력할 수 있다는 의미이다.

다음 예제로 사용법을 확인해 보자.

>>> list(zip([1, 2, 3], [4, 5, 6]))
[(1, 4), (2, 5), (3, 6)]
>>> list(zip([1, 2, 3], [4, 5, 6], [7, 8, 9]))
[(1, 4, 7), (2, 5, 8), (3, 6, 9)]
>>> list(zip("abc", "def"))
[('a', 'd'), ('b', 'e'), ('c', 'f')]


##### UPDATING...