# Class 14 - R Map Visualization

### leaflet 패키지를 활용한 지도 시각화

- [서울시 공공와이파이 서비스 데이터](https://data.seoul.go.kr/dataList/OA-20883/S/1/datasetView.do) 사용

- 패키지 불러오기
```r
install.packages("leaflet")
library(leaflet)
```

- 데이터 불러오기
```r
wifi <- read.csv("seoul_wifi.csv", fileEncoding = "euc-kr")

head(wifi, 3)
names(wifi)
```

- 기본 지도 띄우기
```r
leaflet() %>%
  addTiles() %>%                                        # 기본 배경지도
  setView(lng = 126.9784, lat = 37.5667, zoom = 11)     # 서울 시청 근처
```

- 2000개 wifi 데이터 지도 상에 띄우기
```r
wifi_2000 <- head(wifi, 500)   # 처음 500개만 써서 가볍게 연습

leaflet(wifi_2000) %>%
  addTiles() %>%
  addCircleMarkers(~lon, ~lat, radius = 4, stroke = FALSE, fillOpacity = 0.8)
  # 원크기(radius), 테두리(stroke), 원 투명도(fillOpacity) 설정
```

- 팝업 설정
    - 커서 올릴 시 이름 확인
    - 클릭 시 상세 정보 확인

```r
wifi_2000$popup <- paste0(
  wifi_2000$와이파이명,"<br>",
  wifi_2000$도로명주소,"<br>",
  wifi_2000$자치구
)

leaflet(wifi_2000) %>%
  addTiles() %>%
  addCircleMarkers(
    ~lon, ~lat, radius = 4, stroke = FALSE, fillOpacity = 0.85,
    label = ~와이파이명, # Hover
    popup = ~popup # Click
  )
```

- 지역 별 데이터가 많을 때 묶기
    - clusterOptions 옵션을 사용하면 가까운 위치 별 데이터를 자동으로 묶어준다.
```r
leaflet(wifi_2000) %>%
  addTiles() %>%
  addCircleMarkers(
    ~lon, ~lat, radius = 4, stroke = FALSE, fillOpacity = 0.85,
    label = ~와이파이명, popup = ~popup,
    clusterOptions = markerClusterOptions()
  )
```

- 다른 테마의 지도
```r
leaflet(small) %>%
  addProviderTiles(providers$CartoDB.Positron) %>%
  addCircleMarkers(~lon, ~lat, radius = 4, stroke = FALSE, fillOpacity = 0.85)
```