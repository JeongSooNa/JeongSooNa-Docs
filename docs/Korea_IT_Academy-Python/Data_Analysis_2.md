# Data Analysis - 식품의약품안전처 식품영양성분 데이터베이스 활용

### Summary

- 분석 목표 : 식품의약품안전처의 음식 DB 활용 음식의 영양성분 분석

- 세부 목표

  - Python Pandas를 사용한 데이터 요약
  - 음식의 조회하면 해당 음식의 식품대분류명, 대표식품명, 에너지(kcal) 컬럼에 해당하는 데이터 정보 출력
  - 음식의 열량을 출력하고 DB 등록 음식 중 상위 몇 % 에 해당하는 음식인지 출력하기

- 자료 출처 : [식품의약품안전처 식품영양성분 데이터베이스 - 영양성분 DB 내려받기](https://various.foodsafetykorea.go.kr/nutrient/general/down/historyList.do)


- 데이터 불러오기

```py
import pandas as pd

df = pd.read_csv('20250408_음식DB.xlsx', encoding='cp949')
print(df)
```

### 데이터프레임 요약

- 데이터프레임 정보

```py
df.info()
```

- 데이터프레임 상단 출력

```py
df.head(3)
```

- 데이터프레임 컬럼 출력

```py
df.columns
```

### 데이터 정보 출력

```py
# 식품코드, 식품명, 식품대분류명, 대표식품명, 에너지(kcal)
input_food = input("정보를 알고싶은 음식명을 입력하세요 : ")
df[df['식품명'].str.contains(input_food)][['식품코드','식품명','식품대분류명','대표식품명','에너지(kcal)']]
```

### 열량구하기

- 입력받을 input
    - input_food : 정보를 알고 싶은 음식명 검색
    - input_index : 입력한 음식명을 포함한 전체 리스트 중 선택할 index
    - input_weight : 최종 선택 한 음식의 열량을 구할 g 무게 입력

```py
input_food = input("정보를 알고싶은 음식명을 입력하세요 : ")

search_info = df[df['식품명'].str.contains(input_food)][['식품명', '에너지(kcal)']]

for i in range(len(search_info)):
    print("index:", search_info.index[i])
    print("식품명:", search_info.iloc[i]['식품명'])
    # print("에너지(kcal):", search_info.iloc[i]['에너지(kcal)'])
    print("---")

input_index = input("선택 할 식품의 index를 입력하세요 : ")
result_kcal = search_info.iloc[int(input_index)]['에너지(kcal)']
input_weight = input("선택 할 식품의 g 수를 입력하세요 : ")
final_kcal = int(result_kcal)*int(input_weight)/100
print("검색한 음식의 100g당 열량은",result_kcal,"kcal 이며,")
print("입력하신 ",input_weight,"g 의 총 열량은",final_kcal,"kcal 입니다.")
```