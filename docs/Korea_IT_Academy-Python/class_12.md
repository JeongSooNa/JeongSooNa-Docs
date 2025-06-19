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

