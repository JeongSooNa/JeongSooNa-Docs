# Class 8 - R Regression Analysis

### 회귀분석이란?

- 회귀분석이란 둘 이상의 변수 사이의 관계를 나타내는 선형 모델링 분석 방법으로, 독립변수로 구성된 회귀방정식을 통해 종속변수를 예측할 수 있다.

![jpg](../img/lm_image.png)

### 단순회귀분석

1. 상관분석
2. 회귀계수 검정 (H0 : 회귀계수가 유의하지 않다.)
3. 회귀모형에 대한 검정 (H0 : 유의하지 않다.)
4. 잔차분석 (독립성, 등분산성, 정규성 만족 여부)

- 상관분석은 상관계수를 통해 두 변수 간 어떤 상관 관계를 갖는지 확인하는 분석으로, 회귀분석과 유사하나, 종속변수의 값을 예측할 수는 없다는 특징을 갖고있다.
- 하지만, 변수가 적거나 단순할 수록 상관계수의 절댓값이 크면 유의한 회귀분석 결과를 얻을 확률이 커진다.

<br>

- MASS 패키지에 내장된 cats 데이터셋 활용
  - 고양이의 성별(Sex), 몸무게(Bwt), 심장무게(Hwt) 데이터

```r
library(MASS)
data(cats)
str(cats)
head(cats)
summary(cats)
```

- 그래프로 확인
```r
attach(cats) # attach 함수를 통해 변수를 데이터셋 선언 필요 없이 사용할 수 있다.
plot(Hwt ~ Bwt)
segments(2,6,4,18) # (2,6)(4,18)을 잇는 직선 (회귀선과는 무관)
```

- 상관계수
```r
r <- cor(Bwt,Hwt)
```

- 결정계수
  - 몸무게가 심장의 무게를 얼마나 잘 설명하는가
```r
r^2
cor.test(Bwt,Hwt) # 상관계수 검정
```

- 상관계수 분석 시각화
```r
install.packages("psych")
library(psych) # 상관계수 분석 시각화에 적합한 패키지
pairs.panels(cats[2:3])
```

- 회귀분석 진행

```r
lm.wt <- lm(Hwt~Bwt)
lm.wt
summary(lm.wt)
```

- 분산분석(ANOVA)으로 회귀모형이 유의한지 확인
```r
anova(lm.wt)
```

- 시각화
```r
plot(Hwt~Bwt); abline(lm.wt,col=2)
```

- 잔차분석
  - 잔차 vs 적합값 (선형성 가정 검토)
  - 정규 Q-Q 플롯 (잔차 정규성 검토)
  - Scale-Location (등분산성 확인)
  - 잔차 vs 레버리지 (영향치 확인)

```r
par(mfrow=c(2,2))
plot(lm.wt)
```

### 다중회귀분석

- Multiple Linear Regression
- 설명변수의 개수(p)가 2개 이상이고, 관측치의 개수가 n인 경우
- 오차항은 독립성, 정규성, 등분산성을 만족.
- 상관계수
  - 다중회귀에서 반응변수에 대한 예측력을 평가하는데 사용
  - R^2=SSR/SST
- 다중공정성 : 분산팽창요인(VIF:variance inflation factor)이 주로 사용
  - VIF=1/(1-R^2)

- MASS 패키지의 Cars93 데이터셋을 사용한 다중회귀분석 진행
```r
library(MASS)
data(Cars93)
```

- Cars93데이터 중 연비(MPG.highway)와 연관이 있을 것 같은 데이터셋 추출
  - EngineSize(엔진 크기)
  - Weight(무게)
  - Passengers(승차 인원)
  - Price(가격)

```r
cars.a<- Cars93[,c("MPG.highway","EngineSize","Weight","Passengers","Price")]
head(cars.a)
tail(cars.a)
```

- 다중회귀분석 진행
  - 앞이 반응변수(MPG.highway), 뒤가 설명변수(.란 반응변수를 제외한 나머지)
  - 회귀계수가 유의한지, R-square를 통해 설명력 확인
```r
mlr.cars<-lm(MPG.highway ~ ., data=cars.a)
summary(mlr.cars)
```

- 변수 선택법에 따른 방법 확인
  - 전진선택법(forward selection)
  - 후진제거법(backward selection)
  - 단계적방법(stepwise)
```r
m.step<-step(mlr.cars,direction = "backward")
summary(m.step)
```

- 모델 진단 Plot 확인
  - Residuals vs Fitted: 잔차 패턴 확인 (비선형성 여부 점검)
  - Normal Q-Q: 잔차가 정규분포를 따르는지 확인
  - Scale-Location: 등분산성 여부 확인
  - Residuals vs Leverage: 영향력이 큰 관측치(outlier) 확인
```r
par(mfrow=c(2,2))
plot(m.step)
```

- 다중공선성(VIF) 확인
  - 다중공선성 : 회귀분석에서 독립변수(설명변수)들 끼리 상관관계가 너무 커 독립성 가정을 위배하는 상황
  - 1에 가까우면 다중공선성이 없음
  - 5 이상이면 약간 문제 있음
  - 10 이상이면 심각한 다중공선성
```r
install.packages("VIF")
library(VIF)
attach(cars.a)
vif(MPG.highway)
```

### 다항회귀분석

- Polynomial Regression
- 회귀모형이 직선이 아니라 곡선형태의 모델이 적합한 경우 사용
- y = b0 + b1x + b2x^2 + ... +bnx^n

- 년도 별 인수 수 데이터 임의 생성
```r
year <- c(1959,1960,1961,1962,1963,1964,1965,1966,1967,1968,1969)
population <- c(4835,4970,5085,5160,5310,5260,5235,5255,5235,5210,5175)
sample<-data.frame(year,population)
sample
```

- 시각화
```r
sample$year <- sample$year-1964
sample
par(mfrow=c(1,1))
plot(sample$year, sample$population, type="b")
```

- 다항회귀분석 진행
```r
fit1 <- lm(sample$population ~sample$year)
fit2 <- lm(sample$population ~sample$year +
             I(sample$year^2))
fit3 <- lm(sample$population ~sample$year +
             I(sample$year^2) + I(sample$year^3))
fit2b <- lm(sample$population ~
              poly(sample$year,2,raw=TRUE))
fit3b <- lm(sample$population ~
              poly(sample$year,3,raw=TRUE))

summary(fit1)
summary(fit2) #설명력이 좋게 나옴
summary(fit3) #설명력이 좋게 나옴 (2차나 3차를 이용하는것이 좋다고 판단.)
summary(fit2b)
summary(fit3b)
```

- 시각화
```r
plot(sample$population ~ sample$year)
abline(fit3, col=2)
```

- 가변수(dummy variable) : 설명변수가 질적변수(숫자가 아닌것.)일 때 사용