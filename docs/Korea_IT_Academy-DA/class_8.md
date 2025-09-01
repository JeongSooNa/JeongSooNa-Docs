# Class 8 - R Regression Analysis

- 회귀분석 Data 쭉 올린 후 설명 및 분석 결과 해석 예정

```r
library(MASS)
data(cats)
str(cats)
head(cats)
summary(cats)
#몸무게에 따라 신장의 차이가 있는지
attach(cats)
plot(Hwt ~ Bwt)
segments(2,6,4,18)
r <- cor(Bwt,Hwt)
r^2
cor.test(Bwt,Hwt) # 상관계수 검정

install.packages("psych")
library(psych) # 상관계수 분석 시각화에 적합한 패키지
pairs.panels(cats[2:3])

# 회귀분석
lm.wt <- lm(Hwt~Bwt)
lm.wt
summary(lm.wt)
anova(lm.wt)
plot(Hwt~Bwt); abline(lm.wt,col=2)
# 잔차분석
par(mfrow=c(2,2))
plot(lm.wt)

# 회귀분석 결과
# 1. 상관분석
# 2. 회귀계수 검정 (H0 : 회귀계수가 유의하지 않다.)
# 3. 회귀모형에 대한 검정 (H0 : 유의하지 않다.)
# 4. 잔차분석 (독립성, 등분산성, 정규성 만족 여부)
```

```r
####2017.09.29 선형모형론 실습


### 다중회귀모형
# 설명변수의 개수(p)가 2개 이상이고, 관측치의 개수가 n인 경우
# 오차항은 독립성, 정규성, 등분산성을 만족.
# 상관계수 : 다중회귀에서 반응변수에 대한 예측력을 평가하는데 사용
#   R^2=SSR/SST
# 다중공정성 : 분산팽창요인(VIF:variance inflation factor)이 주로 사용
#   VIF=1/(1-R^2)

## multiple linear reg

install.packages("MASS")
library(MASS)
data(Cars93)
cars.a<- Cars93[,c("MPG.highway","EngineSize","Weight","Passengers","Price")]
head(cars.a)
tail(cars.a)

mlr.cars<-lm(MPG.highway ~ ., data=cars.a)
    #앞이 반응변수(MPG), 뒤가 설명변수(.은 반응변수를 제외한 나머지)
summary(mlr.cars) # ***이므로 유의한 회귀계수이다.
                  # 66% 정도의 설명력을 가짐 (R-square )
  #전진선택법(forward selection)
  #후진제거법(backward selection)
  #단계적방법(stepwise)

m.step<-step(mlr.cars,direction = "backward")
summary(m.step)

par(mfrow=c(2,2))
plot(m.step)

install.packages("VIF")
library(VIF)
attach(cars.a)
vif(MPG.highway)


### 다항회귀모형
# 모형 : 회귀모형이 직선이 아니라 곡선형태의 모델이 적합한 경우 사용
#   y = b0 + b1x + b2x^2 + ... +bnx^n

##polynomial reg
year <- c(1959,1960,1961,1962,1963,1964,1965,1966,1967,1968,1969)
population <- c(4835,4970,5085,5160,5310,5260,5235,5255,5235,5210,5175)
sample1<-data.frame(year,population)
sample1

sample1$year <- sample1$year-1964
sample1
par(mfrow=c(1,1))
plot(sample1$year, sample1$population, type="b")

fit1 <- lm(sample1$population ~sample1$year)
fit2 <- lm(sample1$population ~sample1$year +
             I(sample1$year^2))
fit3 <- lm(sample1$population ~sample1$year +
             I(sample1$year^2) + I(sample1$year^3))
fit2b <- lm(sample1$population ~
              poly(sample1$year,2,raw=TRUE))
fit3b <- lm(sample1$population ~
              poly(sample1$year,3,raw=TRUE))

summary(fit1)
summary(fit2) #설명력이 좋게 나옴
summary(fit3) #설명력이 좋게 나옴 (2차나 3차를 이용하는것이 좋다고 판단.)

summary(fit2b)
summary(fit3b)

plot(sample1$population ~ sample1$year)
abline(fit3, col=2)


### 가변수(dummy variable) : 설명변수가 질적변수(숫자가 아닌것.)일 때 사용
```