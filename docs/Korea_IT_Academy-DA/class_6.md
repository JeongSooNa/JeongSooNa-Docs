# Class 6 - R Statistical Hypothesis Test

### 가설검정
- 가설검정이란 통계적 추론 방법 중 하나로, 집단의 모수를 추정하거나 집단을 비교하는데 주로 사용한다.
- 주로 표본의 정보(데이터)를 사용해 가설이 합당한지를 판단한다.

<br>

- 가설검정의 단계
    1. 귀무가설(H0)과 대립가설(H1) 설정
        - 귀무가설 : 설정한 가설이 참일 확률이 극히 적은 가설로, 기각이 될 것이라 예상하는 가설
        - 대립가설 : 분석 결과 입증되기를 기대할 수 있는(목표하는) 가설로, 연구가설이라고도 한다.
    2. 유의수준 α 설정
        - 유의수준이란? 가설검정에 사용되는 기준값으로, 가설검정 결과의 신뢰도를 정하는 값이다.
        - 일반적으로 0.05값을 사용한다. == 신뢰수준 95%
    3. 검정통계량 계산, 그에 따른 p-value 계산
        - 검정통계량이란? 분석 방법에 따라 도출되는 결과 값으로, 이를 통해 p-value를 구할 수 있다.
        - 분석 결과 t분포를 따르는 t값, F분포를 따르는 F값 등 검정통계량은 다양하게 나올 수 있다.
        - p-value(유의확률)란? 귀무가설이 맞다고 가정할 때 이를 기각할 확률로, p-value가 설정한 유의수준(α)보다 작으면 귀무가설을 기각한다.
    4. p-value < α 이면 귀무가설 기각 (설정한 가설이 맞다고 판단.)

<br>


### 일표본 t Test

- sleep : 수면 시간 증가량

```r
# 데이터 확인
head(sleep)

# 평균이 1과 같은지 검정
t.test(sleep$extra, mu = 1)

# 시각화 (박스플롯 + 평균선)
boxplot(sleep$extra, main="수면시간 증가량",
        ylab="증가시간")
abline(h=1, col="red", lty=2) # 검정 기준선
```

### 이표본 t Test

- 꽃잎 길이 비교

```r
# setosa vs versicolor 꽃잎 길이 차이
t.test(Petal.Length ~ Species, 
       data = subset(iris, Species %in% c("setosa","versicolor")))

# 시각화
boxplot(Petal.Length ~ Species, 
        data = subset(iris, Species %in% c("setosa","versicolor")),
        main="두 종의 꽃잎 길이 비교", col=c("skyblue","pink"))

```

### 분산분석 ANOVA

- 세 종의 꽃받침 길이 비교

```r
# ANOVA
anova_result <- aov(Sepal.Length ~ Species, data=iris)
summary(anova_result)

# 시각화
boxplot(Sepal.Length ~ Species, data=iris,
        main="세 종의 꽃받침 길이 비교", col=c("lightgreen","orange","lightblue"))

```

### 회귀분석

```r
# 단순회귀
model <- lm(mpg ~ wt, data=mtcars)
summary(model)

# 시각화
plot(mtcars$wt, mtcars$mpg, 
     main="무게와 연비 관계", 
     xlab="차 무게", ylab="연비(mpg)")
abline(model, col="red", lwd=2)

```

### 상관분석

```r
# 상관계수
cor(mtcars$hp, mtcars$wt)

# 시각화
plot(mtcars$hp, mtcars$wt, 
     main="마력과 무게의 상관관계",
     xlab="마력", ylab="무게", col="blue", pch=19)
abline(lm(wt ~ hp, data=mtcars), col="red")

```

### 시계열분석

```r
# 데이터 구조
AirPassengers

# 시계열 그래프
plot(AirPassengers, main="항공 여객 수 시계열",
     ylab="승객 수", col="blue")

# 간단한 시계열 분해
ts_data <- decompose(AirPassengers)
plot(ts_data)

# 간단한 예측 (ARIMA)
library(forecast)
fit <- auto.arima(AirPassengers)
forecast_values <- forecast(fit, h=12)
plot(forecast_values)

```