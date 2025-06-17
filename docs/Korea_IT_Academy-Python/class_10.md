# Class 10 - Python 라이브러리

### os
Operating System의 약자로 운영체제에서 제공되는 여러 기능을 파이썬에서 수행할 수 있게 해줍니다.

- PATH 및 파일, 폴더 관리
```py
import os

# 운영 체제 확인
# posix : Unix 계열(Linux)
# nt : Window 계열
os.name

# 현재 경로 확인
os.getcwd()

# 해당 위치의 파일 및 폴더 리스트로 반환
os.listdir()

# 폴더(디렉토리) 생성
os.makedirs("new_directory")

# 폴더(디렉토리) 삭제
os.rmdir("new_directory")

# 파일 삭제
os.remove("file")

# 파일 또는 디렉토리 이름 변경
os.rename("old_name","new_name")

# 경로 존재 확인
# True / False 로 반환
os.path.exists("path")

# 경로 내 파일, 폴더 존재 유무 확인
# True / False 로 반환
os.path.isdir("path")
```

- OS 내 시스템 명령어 실행(CMD)
```py
os.system("echo Hello World")
```

### sys
파이썬 실행을 제어하는 기본 모듈

```py
import sys

# OS 플랫폼 확인
# win32 : Windows OS
# darwin : mac OS
# linux : Linux OS
sys.platform

# Get input parameter
# ex) python test.py "JeongSooNa" 10
sys.argv[0] # test.py
sys.argv[1] # "JeongSooNa"
sys.argv[2] # 10

# Python 종료
sys.exit()

```

### numpy
Numpy란 Python 연산을 위한 기본적인 라이브러리 중 하나입니다.  
Numeric Python의 약자로 대규모 데이터, 배열과 행렬 연산 등에 필요한 다양한 함수를 제공합니다.

- 설치
```bash
pip install numpy
```

- Import
```py
# 다수의 프로젝트 및 실무에서 np라는 약어로 numpy를 사용합니다.
import numpy as np
```

- 배열
```py
# 1차원 배열
a1 = np.array([1,2,3])

# 2차원 배열
a2 = np.array([[1,2,3],[4,5,6]])

# 3차원 배열
a3 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])

# 배열의 크기
a1.shape
a2.shape
a3.shape

# 배열 연산
a = np.array([1,2,3])
b = np.array([4,5,6])
a + b
a + 1
a * b
a = np.array([[1,2],[3,4]])
b = np.array([[1,2],[3,4]])
a + b
a * b

# 배열 제공 함수
a = np.array([1,2,3])
np.sum(a)
np.min(a)
np.max(a)
np.mean(a)
a = np.array([1,2,3],[4,5,6])
np.sum(a)
np.min(a)
np.max(a)
np.mean(a)
np.mean(arr, axis=1) # 행 별 평균
np.mean(arr, axis=0) # 열 별 평균

# 배열 인덱스
a = np.array([1, 2, 3, 4, 5])
a[0] # list indexing과 동일
a[2]
a[1:4]
a[:3]
a[3:]

# 배열 형태 변경
a = np.array([[1, 2], [3, 4], [5, 6]])
a.reshape((2, 3))  # [[1, 2, 3], [4, 5, 6]]
a.T  # 행렬의 전치 : [[1, 3, 5], [2, 4, 6]]

# 배열의 병합과 분리
a = np.array([1, 2, 3])
b = np.array([4, 5, 6])
np.concatenate((a, b))  # 단순 병합 : [1, 2, 3, 4, 5, 6]
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
c = np.concatenate((a, b), axis=0)  # 행 기준 병합 : [[1, 2], [3, 4], [5, 6]]
a = np.array([1, 2, 3, 4, 5, 6])
b, c = np.split(a, [3])  # 배열 분리 : [1, 2, 3], [4, 5, 6]
a = np.array([[1, 2, 3], [4, 5, 6]])
b, c = np.split(a, [1], axis=0)  # [[1, 2, 3]], [[4, 5, 6]]
```
- 그 외 함수
    - np.zeros() : 모든 원소가 0인 배열을 생성
    - np.ones() : 모든 원소가 1인 배열을 생성
    - np.arange() : 범위 내의 일정 간격을 가진 배열을 생성
    - np.linspace() : 범위 내에서 균등 간격으로 원하는 개수의 배열을 생성
    - np.random.random() : 0부터 1사이의 난수를 가지는 배열을 생성
    - np.random.randn() : 평균이 0이고 표준편차가 1인 정규 분포를 따르는 난수를 가지는 배열을 생성

- 수학(통계) 관련 함수
    - np.sum() : 배열 전체 합
    - np.mean() : 평균
    - np.cumsum() : 배열 누적 합
    - np.cumprod() : 누적 곱
    - np.std() : 표준편차
    - np.var() : 분산
    - np.min() : 최소값
    - np.max() : 최대값
    - np.argmin() : 최소 원소의 index 값
    - np.argmax() : 최대 원소의 index 값
    - np.random.seed() : 난수 발생기의 seed를 지정
    - np.random.permutation() : 임의의 순열을 반환
    - np.random.shuffle() : 리스트나 배열의 순서 섞기
    - np.random.rand() : 균등분포에서 표본을 추출
    - np.random.randint() : 주어진 최소/최대 범위 안에서 임의의 난수를 추출
    - np.random.randn() : 표준편차가 1이고 평균값이 0인 정규분포에서 표본을 추출
    - np.random.binomial() : 이항분포에서 표본을 추출
    - np.random.normal() : 정규분포(가우시안)에서 표본을 추출
    - np.random.beta() : 베타분포에서 표본을 추출
    - np.random.chisquare() : 카이제곱분포에서 표본을 추출
    - np.random.gamma() : 감마분포에서 표본을 추출
    - np.random.uniform() : 균등(0,1)에서 표본을 추출

###  pandas
pandas란 파이썬 데이터 분석 라이브러리로, 데이터 핸들링, 분석, 시각화 등 다양한 기능을 제공합니다.  
기본적으로 시리즈(Series)와 데이터프레임(DataFrame) 자료형을 사용하여 데이터를 처리합니다.

- 설치
```py
pip install pandas
```

- Import
```py
# 다수의 프로젝트 및 실무에서 pd라는 약어로 pandas를 사용합니다.
import pandas as pd
```

- DataFrame : 행과 열로 이루어진 2차원 데이터로, 열은 변수, 행은 관측치를 나타냅니다.

- DataFrame 생성
```py
# list > DataFrame
data = [['a',10],['b',20],['c',30]]
df = pd.DataFrame(data, columns=['name', 'age'])
print(df)

# dictionary > DataFrame
data = {'name':['a','b','c'],'age':[10,20,30]}
df = pd.DataFrame(data)
print(df)
```

- CSV 파일을 사용한 DataFrame 생성
- data.csv
```
name    age
a   1
b   2
c   3
```
```py
df = pd.read_csv('data.csv')
print(df)
```

### UPDATING...