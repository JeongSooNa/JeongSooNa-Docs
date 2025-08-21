# Class 3 - R Plot

시각화는 데이터 분석 결과를 보여줌에 있어서 중요한 요소로 자리잡고 있다.  
R은 시각화에 특화된 프로그래밍 언어로, 다양한 패키지와 함께 그래프를 제공


### Plot

- R 내장 데이터셋인 iris 데이터를 사용
    - iris는 꽃의 정보를 담고 있는 데이터로, 5개의 변수로 구성된 데이터 셋이다.
    - Sepal.Length : 꽃받침 길이
    - Sepal.Width : 꽃받침 넓이
    - Petal.Length : 꽃잎 길이
    - Petal.Width : 꽃잎 넓이
    - Species : 품종

```r
library(datasets) # 내장 데이터셋을 불러오지 못할 경우 R 데이터셋 불러오기
summary(iris)
head(iris)
```

- plot()은 그래프의 가장 기초적인 산점도를 출력하는 함수이다.

```r
plot(iris)
```

- 데이터셋 중 특정 원하는 변수의 그래프만 확인하고 싶을 경우

```r
plot(iris$Sepal.Length)
```

- 두 변수 간 산점도

```r
plot(iris$Sepal.Length, iris$Sepal.Width)
```

- 다양한 시각화를 위한 그래프의 옵션을 조정할 수 있다.
```r
plot(iris$Sepal.Length, iris$Sepal.Width,
    col = "#980000", # 점의 색상 조정
    type = "p", # 그래프의 종류 설정. p:punctuation, l:line, b:both
    pch = 7, # 점(포인터)의 모양 (0~25)
    cex = 1.5, # 점의 크기
    main = "Length vs Width", # 타이틀
    xlab = "Length", # x축 이름
    ylab = "Width", # y축 이름
    cex.lab = 1.2, # 축 이름의 크기
    xlim = c(0,10), # x축 범위
    ylim = c(0,5) # y축 범위
    )
```

- 그래프 구현 시 변수와 데이터셋을 조금 더 직관적으로 표현하여 코딩을 할 수 있다.

```r
plot(Sepal.Length ~ Sepal.Width, data = iris)
```

- pch table

![jpg](../img/r_plot_pointer.png)


### Bar Plot

- ldeaths 데이터셋 사용 (영국 호흡기 질병 월별 사망자 수)

```r
ldeaths
```
