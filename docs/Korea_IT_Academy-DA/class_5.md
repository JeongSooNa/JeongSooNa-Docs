# Class 5 - R Basic Plot

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

- barplot()을 사용한 간단한 막대그래프 생성

```r
barplot(iris$Petal.Length)
barplot(iris$Species)
```

- par 함수를 사용해 한번에 여러 개의 그래프를 띄울 수 있다.

```r
# 3행 1열의 그래프 표시
par(mfrow=c(3,1))

# 관측치 별 막대그래프
barplot(iris$Petal.Length) 
# RColorBrewer 패키지의 색상 적용
barplot(iris$Sepal.Length,col  = brewer.pal(3,"Set1"))
# 품종 별 분포를 누적그래프 적용
barplot(table(iris$Species,iris$Sepal.Length),col  = brewer.pal(3,"Set1"))
```

- 시계열 데이터를 활용한 다양한 막대 그래프 활용

```r
# 영국 호흡기 질환 월별 사망자 수 (ts:Time Siries Data)
ldeaths
# matrix 형태로 변환
ld <- matrix(ldeaths, nrow=6, byrow=T) 
colnames(ld) <- month.abb
rownames(ld) <- 1974:1979
ld

par(mfrow=c(2,2))

# 1월달 막대그래프
barplot(ld[,"Jan"]) 
# 각 월별로 년도 하위 그룹 막대 그래프
barplot(ld, beside=T)
# 위의 그래프와 동일하나 각 년도 별 쌓아서 표현
barplot(ld, beside=F)
# 위의 그래프를 아래에서 위 방향 > 좌에서 우방향
barplot(ld, beside=F, horiz=T, density=5)
```

### Histogram

- hist()는 연속형 자료의 그래프로 많이 사용되며, 주로 통계적 분포를 파악하는데 유용하다.

- mtcars 데이터셋을 활용해 그래프를 그려보자. 32종 차들의 10가지 특성(연비, 무게 등)을 정리한 데이터

```r
head(mtcars)
str(mtcars)
```

- 4분할 히스토그램

```r
par(mfrow=c(2,2))

# 기본적인 히스토그램
hist(mtcars$mpg) # mpg는 Miles per Gallon으로 연비를 의미한다.
# 히스토그램의 막대를 12개로 설정
hist(mtcars$mpg, breaks=12)
# y축의 값을 빈도가 아닌 비율로 하고 막대의 색을 빨강과 파랑이 교차로 나오게 설정
hist(mtcars$mpg, breaks=12, freq=FALSE, col=c("red", "blue"))
# 막대가 25%, 50%, 75%, 100% 가 되는 값
hist(mtcars$mpg, breaks=quantile(mtcars$mpg))
```
