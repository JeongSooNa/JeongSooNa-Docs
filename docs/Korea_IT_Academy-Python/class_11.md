# Class 11 - Python 라이브러리 - Numpy

### numpy
Numpy란 Python 연산을 위한 기본적인 라이브러리 중 하나입니다.  
Numeric Python의 약자로 대규모 데이터, 배열과 행렬 연산 등에 필요한 다양한 함수를 제공합니다.

### 설치
```bash
pip install numpy
```

### Import
```py
# 다수의 프로젝트 및 실무에서 np라는 약어로 numpy를 사용합니다.
import numpy as np
```

### 배열 선언
```py
# 1차원 배열
a1 = np.array([1,2,3])

# 2차원 배열
a2 = np.array([[1,2,3],[4,5,6]])

# 3차원 배열
a3 = np.array([[[1,2],[3,4]],[[5,6],[7,8]]])
```

### 배열 다루기

- 배열의 크기
```py
a1.shape
a2.shape
a3.shape
```

- 배열 연산
```py
a = np.array([1,2,3])
b = np.array([4,5,6])
a + b
a + 1
a * b
a = np.array([[1,2],[3,4]])
b = np.array([[1,2],[3,4]])
a + b
a * b
```

- 배열 제공 함수
```py
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
```

- 배열 인덱스
```py
a = np.array([1, 2, 3, 4, 5])
a[0] # list indexing과 동일
a[2]
a[1:4]
a[:3]
a[3:]
```

### 배열 변환

- 배열 형태 변경
```py
a = np.array([[1, 2], [3, 4], [5, 6]])
a.reshape((2, 3))  # [[1, 2, 3], [4, 5, 6]]
a.T  # 행렬의 전치 : [[1, 3, 5], [2, 4, 6]]
```

- 배열의 병합과 분리
```py
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
### 그 외 함수
- np.zeros() : 모든 원소가 0인 배열을 생성
- np.ones() : 모든 원소가 1인 배열을 생성
- np.arange() : 범위 내의 일정 간격을 가진 배열을 생성
- np.linspace() : 범위 내에서 균등 간격으로 원하는 개수의 배열을 생성
- np.random.random() : 0부터 1사이의 난수를 가지는 배열을 생성
- np.random.randn() : 평균이 0이고 표준편차가 1인 정규 분포를 따르는 난수를 가지는 배열을 생성

### 수학(통계) 관련 함수
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