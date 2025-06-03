# Class 3 - Python 자료형

### 변수 선언과 정의
- 선언 : 새로운 변수 생성
- 정의 : 변수의 값 지정

```py
# 파이썬에서는 변수 선언과 함께 정의가 동시에 이뤄진다.
# 변수명은 영문자 혹은 언더바(_)로 시작
a = 1

print(a)
```

```py
a = 1
a = 10
print(a)
```

```py
a = 1
b = a
a = 2
print(a,b)

# 마지막으로 정의 된 값이 어떤 값인지에 따라 변수는 변할 수 있다.
```

- 대문자와 소문자를 반드시 구분하여 사용한다.
- 변수의 선언은 다른 사용자 혹은 공동 개발자가 알아볼 수 있도록 정확히 명시하는 것이 좋다.
    - ex)
    ```py
    # 학번을 나타내는 변수
    studentID = 2013016032
    # 이름을 나타내는 변수
    student_name = "JeongSoo Na"
    ```


### 기본 타입
- 변수의 종류, 자료형
- 파이썬에서는 어떤 값을 정의하냐에 따라 타입이 자동으로 결정.

- 정수형
```py
# int(integer)
a = 1
```
- 실수형
```py
# float
b = 1.2
```
- 문자형
```py
# str(string, character)
c = "Python"
```
- 논리형
```py
# bool(Boolean, True/False)
d = True
```
- 빈 값
```py
# NoneType
e = None
```

- 변수의 타입을 알고 싶을 때는 type 함수를 사용한다.
```py
print("a의 타입은 : ",type(a))
print("b의 타입은 : ",type(b))
print("c의 타입은 : ",type(c))
print("d의 타입은 : ",type(d))
print("e의 타입은 : ",type(e))
```

### 형변환
- 정의 된 변수의 타입을 변환할 수 있다.

```py
a = 1 # 숫자형
b = "1" # 문자형

c = str(a) # 숫자 > 문자
d = int(b) # 문자 > 숫자
```

### 리스트
- List란 여러 값을 담을 수 있는 변수이다.
```py
a = [1,2,3,4,5]
```

- List 안의 값들은 서로 다른 타입을 가질 수 있다.
```py
a = [1,1.2,"Hello",True, None]
```

- List 안에 List를 넣을 수 있다.
```py
students = [[1,"짱구"],[2,"철수"],[3,"맹구"],[4,"유리"],[5,"훈이"]]
```

- 인데스(index)를 사용해 리스트 값에 접근할 수 있다.
- index는 List의 첫번째가 0 부터 시작한다.
```py
print(students[0])
print(students[1])
print(students[-1])

print(students[0][0])
print(students[0][1])
print(students[2][1])
```

- index를 사용해 List의 값을 수정할 수있다.
```py
student[4][1] = "수지"

print(students)
```

- 슬라이싱(:)을 통해 범위 값을 모두 볼 수 있다.
- 슬라이싱의 범위는 시작 index는 포함하나 끝 index는 포함하지 않는다.
```py
print(students[2:4]) # 2,3 출력
```

### 리스트 관련 함수
```py
a = [1,2,3,4,5]

# 합계
sum(a)

# 최솟값
min(a)

# 최댓값
max(a)

# 리스트의 길이
len(a)

# 리스트끼리 합칠 수 있다.
b = a + [6,7]
b

# 리스트의 평균
avg = sum(a) / len(a)
# numpy package에 포함 된 mean 함수를 사용할 수도 있다.
import numpy
numpy.mean(a)

# 리스트 맨 뒤에 값 추가
a.append(6)
a

# 지정한 위치(index)에 값 추가
a.insert(0,7)
a

# 지정한 위치(index) 삭제
del a[5]
a
deleted_value = a.pop(0) # pop()은 삭제한 값을 반환하는 특징이 있어, 삭제한 값을 저장해둘 수 있다.
a
a.pop() # index를 생략할 경우 맨 뒤의 값이 삭제된다.
a

# 지정한 값 삭제
# index가 아닌 List안의 특정 값을 삭제
# 여러 개가 있을 경우 가장 먼저 오는 값만 삭제한다.
b = [1,2,3,1,2,3]
b.remove(2)
b

# 리스트 초기화 : []의 상태로 만들어준다.
a.clear()
a

```

### 튜플
- 튜플(Tuple)은 리스트와 비슷하나 수정이 불가능하다는 특징을 갖고 있다.
- 리스트와 동일하게 인덱스로 접근이 가능하나 추가, 삭제 등이 불가능하다.
```py
a = (1,2,3,4)
a[1]
```

### 세트
- 세트(set)는 중복 값이 없다는 특징을 갖고 있다.
- 요소의 추가, 삭제가 가능하다.
- 중복 요소 없이 순서대로 나열되기 된다.
```py
a = {1,3,2,4,5}
a
```

### 딕셔너리
- 딕셔너리(Dictionary)는 키(key)와 값(value)로 이루어진 자료 구조이다.
- 리스트의 인덱스는 순자로 접근하나 딕셔너리의 경우 특정 key를 통해 값에 접근할 수 있다.
- 중복된 값을 가질 수 있으나 값을 조회하는 키(key)의 경우 중복될 수 없다.
```py
students = {\
    "id" : [1,2,3],\
    "name" : ["짱수","철수","유리"],\
    "favorite" : ["액션가면", "모에피", "토끼"]\
    } # 위와 같이 많은 데이터를 코딩해야하는 경우 "\"를 사용해 코드를 띄워 쓸 수 있다.

students
students["name"]
students["name"][1]

# key(), values() 함수를 통해 어떤 key와 value들을 갖고 있는지 확인이 가능하다.
students.key()
students.values()
```