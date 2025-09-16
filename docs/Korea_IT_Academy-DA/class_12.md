# Class 12 - R Analysis of Public Data

### 범죄 데이터 활용 분석

- [경찰청_범죄 발생 지역별 통계](https://www.data.go.kr/data/3074462/fileData.do)를 활용한 범죄 발생 지역 확인 및 시각화
    - 2023년 기준 경찰청에서 집계한 범죄 발생 지역별 통계를 제공하는 공공데이터
    - 강력범죄, 지능범죄, 절도, 폭력 등 다양한 범죄 유형이 시군구 단위로 세분화
    - 외국인 범죄자에 대해서는 국적별(중국, 베트남, 러시아 등) 범죄 발생 수치도 포함
- 범죄 발생 통계량 확인
- 지역 별 데이터를 활용한 지도 시각화

- 데이터 불러오기 & 확인
```r
# CSV 파일 불러오기
data <- read.csv("criminal_zone_20231231.csv", fileEncoding = "euc-kr")

# 데이터 구조 확인
head(data)
str(data)
```

- 지역별 총 범죄 건수 구하기
```r
# dplyr
install.packages("dplyr")
library(dplyr)

# 특정 지역들만 뽑아서 합산 (예: 서울 각 구)
loc_sum <- data %>%
  select(범죄대분류, 범죄중분류, 서울종로구:서울강남구) %>%  # 서울 구만 추출
  summarise(across(서울종로구:서울강남구, sum, na.rm = TRUE))

loc_sum
```

- 범죄 유형별 발생 건수 비교
```r
install.packages("ggplot2")
library(ggplot2)

# 범죄 유형별 합계 구하기 (전국 기준)
cri_sum <- data %>%
  group_by(범죄대분류) %>%
  summarise(총범죄 = sum(across(where(is.numeric)), na.rm = TRUE))

# 막대그래프로 시각화
ggplot(cri_sum, aes(x = 범죄대분류, y = 총범죄)) +
  geom_bar(stat = "identity", fill = "skyblue") +
  theme_minimal() +
  labs(title = "범죄 유형별 발생 건수", x = "범죄 유형", y = "건수")
```

- 특정 범죄 기준 상위/하위 지역
```r
# 예: 강도 범죄만 추출
s_data <- data %>%
  filter(범죄중분류 == "강도") %>%
  select(서울종로구:서울강남구)

# 상위 5개 지역
sort(colSums(s_data), decreasing = TRUE)[1:5]

# 하위 5개 지역
sort(colSums(s_data), decreasing = FALSE)[1:5]
```

##### UPDATING...

- 지도 시각화 (leaflet)
```r
# leaflet 패키지 설치 & 불러오기
library(leaflet)

# 예시 데이터: 서울 구별 위도/경도 좌표를 준비해야 함
# (csv 파일로 좌표 데이터를 미리 제공하면 좋음)
coords <- data.frame(
  지역 = c("서울종로구", "서울중구"),
  위도 = c(37.573, 37.563),
  경도 = c(126.979, 126.997),
  범죄수 = c(500, 700)   # 예시 값
)

# 지도에 표시
leaflet(coords) %>%
  addTiles() %>%
  addCircleMarkers(
    lng = ~경도, lat = ~위도,
    radius = ~범죄수 / 100,  # 범죄 수에 비례해 원 크기 결정
    popup = ~paste(지역, ":", 범죄수, "건")
  )
```


### 근로소득 데이터 활용 분석

- [국세청_근로소득 백분위(천분위) 자료](https://www.data.go.kr/data/15082063/fileData.do)
    - 근로소득 : 고용관계나 이와 유사한 계약에 의하여 근로를 제공하고 지급받는 대가
    - 사업소득 : 고용관계 없이 독립된 자격으로 계속적으로 용역을 제공하고 지급받는 대가
    - 기타소득 : 일시적으로 용역을 제공하고 지급받는 대가
    - 퇴직소득 : 사용자 부담금을 기초로 하여 현실적인 퇴직을 원인으로 지급받는 소득 등
    - 인원(명)
    - 총급여액(억 원)
    - 근로소득금액(억 원)
    - 소득공제액(억 원)
    - 과세표준(억 원)
    - 결정세액(억 원)
- 데이터를 활용한 근로소득 분위 조회