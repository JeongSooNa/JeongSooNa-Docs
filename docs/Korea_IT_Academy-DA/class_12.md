# Class 12 - R Analysis of Public Data

### PATH

- 경로 확인
  - 외부 데이터, 파일을 다루기 전 현재 내가 R을 실행시키고 있는 위치와 폴더 경로를 확인하는 것이 좋다.
```r
getwd() # 현재 경로 확인
setwd() # workspace 경로 설정
list.files() # 현재 경로의 파일 확인
```

### 범죄 데이터 활용 분석

- [경찰청_범죄 발생 지역별 통계](https://www.data.go.kr/data/3074462/fileData.do)를 활용한 범죄 발생 지역 확인 및 시각화
    - 2023년 기준 경찰청에서 집계한 범죄 발생 지역별 통계를 제공하는 공공데이터
    - 강력범죄, 지능범죄, 절도, 폭력 등 다양한 범죄 유형이 시군구 단위로 세분화
    - 외국인 범죄자에 대해서는 국적별(중국, 베트남, 러시아 등) 범죄 발생 수치도 포함
- 범죄 발생 통계량 확인
- 지역 별 데이터를 활용한 지도 시각화

- 파일 불러오기
  - 사용할 csv file을 R workspace 경로에 옮기거나 해당 file의 경로를 절대 혹은 상대 경로로 입력하여 명시
```r
data <- read.csv("criminal_zone_20231231.csv", fileEncoding = "euc-kr")
```

- 데이터 구조 확인
```r
head(data)
str(data)
```

- 지역별 총 범죄 건수 구하기
  - dplyr 패키지 사용
    - %>% (파이프) : 해당 변수를 다음 함수의 인자로 넘겨 결과를 할당하는데에 사용
    - select : 필요한 열만 선택
    - summarise : 열 별 합계
    - across : 결과를 테이블로 반환
```r
install.packages("dplyr ")
library(dplyr)

# 특정 지역들만 뽑아서 합산 (예: 서울 각 구)
loc_sum <- data %>%
  select(범죄대분류, 범죄중분류, 서울종로구:서울강남구) %>%  # 범죄대분류, 범죄중분류를 골라낸 귀 서울시 구만 추출
  summarise(across(서울종로구:서울강남구, sum, na.rm = TRUE)) # 추출된 데이터를 합계 계산 / na.rm : 결측값(NA)은 무시

loc_sum
```

- 대전에서 발생한 범죄
```r
loc_daejeon <- data %>%
  select(범죄대분류, 범죄중분류, 대전동구:대전대덕구) %>% 
  summarise(across(대전동구:대전대덕구, sum, na.rm = TRUE))

loc_daejeon
```

- long 자료형으로 변환해 막대그래프 형태로 데이터를 시각화 할 수 있다.
```r
install.packages("tidyr")
library(tidyr)
loc_long <- loc_sum %>%
  pivot_longer(cols = everything(), names_to = "서울구", values_to = "총범죄")
loc_long
library(ggplot2)
ggplot(loc_long, aes(x = 서울구, y = 총범죄)) + geom_col()
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
  - ggmap 구글 지도 API를 활용한 시각화가 활용도나 호환성이 좋아 널리 알려져 있으나, API 라이센스 발급이 필요해 R 지도 시각화에 적합한 leaflet 패키지 사용.
  - ggmap의 경우 도시 이름을 넣으면 위경도를 자동으로 찾아줘 지도에 표시 등 다양한 기능을 제공하니 조금 더 전문화 된 지도 시각화를 경험하고 싶을 경우 추천.
  - leaflet 패키지의 경우 위경도를 직접 입력해주어야 하는 번거로움이 있다.
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

- 데이터 불러오기
```r
data <- read.csv("income_percentage_20241231.csv", fileEncoding = "euc-kr")
```

- 데이터 구조 확인
```r
head(data)
str(data)
```

- 데이터 앞 뒤 공백 제거
```r
data$구분 <- trimws(data$구분)
```

- 데이터 비교
```r
# 상위 1% 데이터
top1 <- subset(data, 구분 == "상위 1.0%")
# 상위 90% 데이터
top90 <- subset(data, 구분 == "상위 90%")

top1
top90
```

- 평균 급여 : 총 급여와 인원을 활용한 소득 분위 별 평균 소득 계산
```r
data$평균급여 <- data$총급여 / data$인원
data[,c("구분","평균급여")]
```

- 위 평균 급여 데이터를 활용한 본인의 소득 입력 시 상위 몇 % 계산
```r
본인소득 <- 0.5  # 본인 소득 입력
# 본인 소득보다 평균급여가 작은 분위 수
upper_data <- sum(data$평균급여 < 본인소득)
# 상위 퍼센트 계산
result <- (upper_data / nrow(data)) * 100
result
```

- ggplot으로 시각화 해 본인 소득 위치 표시 그래프
```r
# 구분을 숫자 변수로 만들기 위해 문자 제거
data$구분_num <- as.numeric(gsub("상위 |%", "", data$구분)) # gsub 함수를 사용해 문자 대체

ggplot(data, aes(x = 구분_num, y = 평균급여)) +
  geom_col(fill = "skyblue") +  # 막대 그래프
  geom_hline(yintercept = 본인소득, color = "red", size = 1) + # 본인 소득 선
  geom_text(aes(x = nrow(data)/2, y = 본인소득, 
    label = paste0("본인 소득: ", 본인소득)), 
      vjust = -1, color = "red", size = 4) +
  labs(title = "분위별 평균급여와 본인 소득 위치",
    x = "구분_num",
    y = "평균급여") +
  theme_minimal()
```

- 소득 대비 세금 부담률
```r
# 세금부담률 계산: (결정세액 / 총급여) * 100
data$세금부담률 <- (data$결정세액 / data$총급여) * 100

# 세금 부담률 확인
head(data[, c("구분", "총급여", "결정세액", "세금부담률")])

# 데이터 확인
head(data)

# 데이터 시각화
library(ggplot2)

ggplot(data, aes(x = 구분_num, y = 세금부담률)) +
  geom_line(color = "blue") +
  geom_point(color = "red") +
  #theme_minimal() +
  labs(title = "소득분위 별 세금부담률",
    x = "소득 구간 (%)", y = "세금부담률 (%)")
```

- 소득공제 비율 분석
  - 소득공제란? 세금을 계산할 때 법적으로 인정되어 총급여에서 제외할 수 있는 금액
  - 인적공제, 보험료 공제, 기부금 공제 등 연말정산을 생각하면 된다.

기타 공제: 주택자금, 교육비 등
```r
# 소득공제 비율 = 소득공제액 / 총급여
data$소득공제비율 <- (data$소득공제액 / data$총급여) * 100

# 그래프로 확인
ggplot(data, aes(x = 구분_num, y = 소득공제비율, group = 1)) +
  geom_line(color = "blue") +
  geom_point(color = "red") +
  theme_minimal() +
  theme(axis.text.x = element_text(angle = 90, hjust = 1)) +
  labs(title = "소득분위 별 소득공제 비율",
    x = "소득 구간 (백분위)", y = "소득공제 비율 (%)")
```