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

- sleep data
    - R 내장 데이터로, 약물복용(group) 시 수면 증가량(extra)이 피실험자(ID)에 따라 어떻게 달라지는가에 대한 데이터이다.

- 데이터 확인
```r
sleep
```

- 평균이 1과 같은지 검정
```r
t.test(sleep$extra, mu = 1)
```
- 결과 해석
    - 출력된 분석 결과를 통해 해석
    - 분석 방법 : One Sample t-test
    - 사용한 데이터 : sleep$extra
    - 검정통계량 : t = 1.1968
    - 자유도 : df = 19 (n-1)
    - 유의확률 : p-value = 0.2461 (유의 확률이 유의수준 α = 0.05보다 작으면 귀무가설을 기각한다.(대립가설을 채택한다.))
    - 대립가설 : true mean is not equal to 1
    - 신뢰구간 : 95 percent confidence interval : 0.5955845 2.4844155 (추정한 평균의 95% 신뢰구간 : 평균은 95% 유의수준으로 해당 구간에 속한다.)
    - 추정 값 : sample estimates : mean of x  1.54 

- 시각화 (박스플롯 + 평균선)
```r
boxplot(sleep$extra)
abline(h=1, col="red", lty=2) # 평균=1 선 추가
```

### 이표본 t Test

- iris 데이터 사용

- setosa vs versicolor 두 종의 꽃잎 길이 차이
```r
t.test(Petal.Length ~ Species, 
       data = subset(iris, Species %in% c("setosa","versicolor")))
```
- 결과 해석
    - 이 표본 t-test에서의 자유도는 두 집단의 추정 자유도를 사용하기 때문에 n-1으로 나타나지 않는다.

- 시각화
```r
boxplot(Petal.Length ~ Species, 
        data = subset(iris, Species %in% c("setosa","versicolor")))
```

### 분산분석 ANOVA

- 세 종의 꽃받침 길이 비교

- 일원분산분석(One-way ANOVA)
    - iris 데이터의 종에 따라 꽃받침의 길이가 다를까?
    - 분산분석 등 R 통계분석 함수는 분석 모델(모형)의 형태로 반환되는 경우가 많아 다음과 같이 summary로 결과를 출력할 수 있다.
```r
anova_result <- aov(Sepal.Length ~ Species, data=iris)
summary(anova_result)
```
- 분산분석표 해석
    - 자유도
    - 제곱합
    - 평균합
    - 검정통계량(F값)
    - 유의확률(p-value)
```
             Df Sum Sq Mean Sq F value Pr(>F)    
Species       2  63.21  31.606   119.3 <2e-16 ***
Residuals   147  38.96   0.265  
```

- 시각화
    - boxplot에서 보여지는 동그란 점의 경우 이상값([Q1,3±1.5*IQR] 외 범위)
```r
boxplot(Sepal.Length ~ Species, data=iris)
```

### 회귀분석

- 단순회귀분석
```r
model <- lm(mpg ~ wt, data=mtcars)
summary(model)
```
- 결과 해석
    - Intercept와 wt에 따른 회귀식과 해당 회귀식이 유의한지
    - y = -5.3445*x + 37.2851 이라는 회귀식을 나타낸다.
    - 잔차 표준 오차 Residual standard error
    - 결정계수 R-Squared : 설명력 (독립변수 x가 종속변수 y를 얼마나 잘 설명하는가?)
    - 회귀식 전체가 유의한가?

- 시각화
```r
plot(mtcars$wt, mtcars$mpg)
abline(model, col="red", lwd=2)
```

### 상관분석

- 자동차의 마력과 무게 간 상관관계가 있는가?
- 상관계수
```r
cor(mtcars$hp, mtcars$wt)
```

- 시각화
```r
plot(mtcars$hp, mtcars$wt)
```

- 회귀분석과의 관계
    - 상관분석은 두 집단 간 어떠한 상관관계가 있는가?를 분석하기 위함이고, 회귀분석은 회귀방정식을 구함으로서 데이터를 예측할 수 있는 특징이 있다.
```r
abline(lm(wt ~ hp, data=mtcars), col="red")
```

- 강한 양의 상관관계
    - iris 데이터에서 꽃받침의 길이가 길어질 수록 꽃잎의 길이도 길어질까?
```r
cor(iris$Sepal.Length,iris$Petal.Length)
```


### 시계열분석

- AirPassengers 데이터
    - ts(time series, 시계열) 데이터
    - 1949.01~0960.12 월별 항공사 여객 수에 대한 데이터
```r
AirPassengers
```

- 시계열 그래프
```r
plot(AirPassengers)
```

- 시계열 분해
    - observed : 시계열 그래프
    - trend : 장기적인 증가 경향 (추세)
    - seasonal : 반복되는 패턴 (계절성)
    - random : 나머지 불규칙한 요인 (노이즈)
```r
ts_data <- decompose(AirPassengers)
plot(ts_data)
```

- ARIMA Model
    - AutoRegressive Integrated Moving Average
    - 과거의 값, 오차 등을 이용해 미래를 예측하는 모델
    - ARIMA( p , d , q)
        - p (AR) : 자기회귀 모형으로, 과거 시점의 값을 활용
        - d (Integrated) : 차분 횟수
            - 차분 : 2차 함수를 1차 함수로 차분한다는 개념. 차수가 낮아지면서 추세가 없어진다.
            - 변환 : 로그 변환을 의미하며, 분산이 클 경우 분산을 줄일 수 있다.
        - q (MA) : 이동평균 모형으로, 과거 오차를 활용
    - SARIMA(2,1,1)(0,1,0)[12] : ARIMA(2,1,1) Model에 계절성(0,1,0)을 반영한 모델
```r

- forecast 라이브러리를 사용해 ARIMA Model 분석
```r
install.packages("forecast")
library(forecast)
```

- 자동으로 ARIMA Model 선택
```r
fit <- auto.arima(AirPassengers)
```

- 12개월 만큼 미래 예측
```r
forecast_values <- forecast(fit, h=12)
```

- 시각화
```r
plot(forecast_values)
```

- ARIMA Model을 직접 설정해 분석을 진행하는 방법
```r
fit <- Arima(AirPassengers, 
    order = c(2, 1, 1), 
    seasonal = list(order = c(0, 1, 0), period = 12))
```