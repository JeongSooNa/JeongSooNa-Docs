# Class 12 - Python 라이브러리 - Pandas

### pandas
pandas란 파이썬 데이터 분석 라이브러리로, 데이터 핸들링, 분석, 시각화 등 다양한 기능을 제공합니다.  
기본적으로 시리즈(Series)와 데이터프레임(DataFrame) 자료형을 사용하여 데이터를 처리합니다.

### 설치
```py
pip install pandas
```

### Import
```py
# 다수의 프로젝트 및 실무에서 pd라는 약어로 pandas를 사용합니다.
import pandas as pd
```

### DataFrame
행과 열로 이루어진 2차원 데이터로, 열은 변수, 행은 관측치를 나타냅니다.

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

- DataFrame 데이터 조회(index)
```py
# 열 선택
df['name']
df[['name','age']]

# 행 선택
df.loc[0]
df.loc[[0, 1, 2]]
```

- DataFrame 수정
```py
# 열 추가
df['score'] = [4, 5, 6]

# 열 삭제
df.drop('score', axis=1, inplace=True)

# 행 추가
df.loc[3] = ['d', 4, 5]

# 행 삭제
df.drop(3, inplace=True)

# 열 이름 변경
df.rename(columns={'name': 'id'}, inplace=True)

df
```

### Series
index & 값으로 이루어진 1차원 데이터로, 데이터 프레임의 열을 사용해서 만들 수도 있다.

```py
# Series 생성 (using list)
data = [1,2,3]
s = pd.Series(data,index=["a","b","c"])
s

# Series 생성 (using dictionary)
data = {'a':1,'b':2,'c':3}
s = pd.Series(data)
s
```

### 데이터 불러오기
Pandas에서는 다양한 형태의 외부 데이터를 불러올 수 있다.  
ex) CSV, Excel, SQL 등

- data.csv
```csv
이름,나이,도시
김철수,30,서울
이영희,25,서울
박상현,40,대전
최지우,28,서울
정민수,35,세종
김민지,22,대전
장동건,45,서울
한가인,32,세종
강감찬,50,대전
이순신,27,대전
```

- CSV 파일 불러오기
```py
df = pd.read_csv('data.csv')
```

- Excel 파일 불러오기
```py
df = pd.read_excel('data.xlsx')
```

- SQL 불러오기
```py
import pandas as pd
from sqlalchemy import create_engine  # SQLAlchemy Import

# 데이터베이스 연결 (예: SQLite)
engine = create_engine('sqlite:///mydatabase.db')

# SQL 쿼리
query = "SELECT * FROM my_table"  # 'my_table' 테이블에서 모든 데이터 선택

# 데이터 불러오기
df = pd.read_sql(query, con=engine)
```

### 데이터 사용

- DataFrame 정보 확인
```py
df.info()
```

- 윗부분 확인
    - Default : 5
```py
df.head(3)
```

- DataFrame Summary 확인
```py
df.describe()
```

### 데이터 선택
DataFrame 생성 후 데이터를 조회 해 사용할 수 있습니다.

```py
# 열 선택하기
df['이름']

# 여러 개의 열 선택하기
df[['이름', '나이']]

# 행 선택하기
df.loc[2]

# 여러 개의 행 선택하기
df.loc[[1,2,3]]
```

### 데이터 필터링
연산자와 조건식을 통해 원하는 데이터만 추출할 수 있습니다.

```py
# 조건 필터링
df['나이' < 30]
df[df['나이'] >= 30]

df[(df['나이'] < 30) & (df['도시'] == '대전')]
df[(df['나이'] >= 30) | (df['도시'] == '세종')]

# isin()
df[df['도시'].isin(['대전','세종'])]
```

### 데이터 그룹화
열에 따라 데이터를 그룹화 하여 핸들링할 수 있습니다.

- groupby() : 그룹화한 데이터, 각 그룹에 대한 정보를 담고 있는 객체.
```py
g = df.groupby('도시')
```

- 집계 함수 : 그룹화된 데이터에 대해 집계 함수를 이용하여 다양한 처리를 수행.
    - 그룹화된 데이터.집계함수()
    - count() : 데이터의 개수를 세는 함수
    - sum() : 데이터의 합을 구하는 함수
    - mean() : 데이터의 평균을 구하는 함수
    - median() : 데이터의 중앙값을 구하는 함수
    - min() : 데이터의 최소값을 구하는 함수
    - max() : 데이터의 최대값을 구하는 함수
    - std() : 데이터의 표준편차를 구하는 함수
    - var() : 데이터의 분산을 구하는 함수
```py
g.count()
g.sum()
g.mean()
g.median()
g.min()
g.max()
g.std()
g.var()
```

### 데이터 정렬
```py
# 오름차순 정렬
df.sort_values('나이')

# 내림차순 정렬
df.sort_values('나이', ascending=False)
```

- 데이터 정렬의 경우 알고리즘 학습을 통해 구현해보자.
    - [Algorithm_study-sorting](./Algorithm_study-sorting.md)

### 인덱스 초기화
인덱스 초기화를 통해 기존 DataFrame에 순서대로 index를 새로 부여할 수 있습니다.

```py
df.reset_index()
```