# Class 9 - R Statistical Computing

### 전산통계란?

- 전산통계란 컴퓨터를 활용한 수치적 근사를 목표로, 통계적으로 해석하기 어려운 부분이 많아 이를 극복하기 위한 실험으로 사용되는 기법이다.

- 난수 생성, 최적화, 시뮬레이션 등을 활용하여 전산통계 실습을 진행해보자.

- seed를 활용하면 랜덤한 난수를 생성할 때 재현성을 확보할 수 있다.
```r
set.seed(1)
rnorm(5)
set.seed(1)
rnorm(5)
set.seed(2)
rnorm(5)
```

### 확률분포의 모의실험 (Random number generation)

- rnorm(정규분포), runif(균일분포), rbinom(이항분포) 등 다양한 확률분포 함수 제공
- 여러 확률분포 데이터를 생성할 수 있다.

```r
x <- rnorm(100, mean = 0, sd = 1)
hist(x)
```

- 데이터의 갯수(n)가 커질 수록 목표한 연속확률분포에 가까워지는 것을 확인할 수 있다.

```r
par(mfrow=c(2,2))
x1 <- rnorm(10, mean = 0, sd = 1)
x2 <- rnorm(100, mean = 0, sd = 1)
x3 <- rnorm(1000, mean = 0, sd = 1)
x4 <- rnorm(10000, mean = 0, sd = 1)
hist(x1)
hist(x2)
hist(x3)
hist(x4)
par(mfrow=c(1,1))
```

### 수치적 방법 (Numerical Methods)

- 루트 찾기
    - 함수 생성
    - uniroot의 결과(근, 근의 함숫값, 반복횟수, 추정정밀도) 확인
```r
# f(x) = x² - 2 함수식 선언
f <- function(x) x^2 - 2
# uniroot 방정식의 해를 찾아주는 함수
uniroot(f, interval = c(0, 2))
```

### 시뮬레이션 기반 방법

- 몬테카를로 시뮬레이션
    - 반복된 무작위 추출을 이용하여 함수의 값을 수학적으로 근접하게 만드는 알고리즘
    - 확률분포, 최적화, 수치적분 등에 사용된다.

- 몬테카를로 시뮬레이션을 사용한 pi 값 추정
```r
monte_carlo <- function(n = 100) {
  # 1사분면 내 난점 생성
  x <- runif(n)
  y <- runif(n)
  # 원 내부 여부
  inside <- (x^2 + y^2) <= 1

  # inside 비율 * 4
  pi_hat <- 4 * mean(inside)
  se_hat  <- 4 * sqrt(mean(inside) * (1 - mean(inside)) / n)  # 표준오차 근사

  # 그림: 단위 정사각형 + 사분원 경계 + 점 색상
  plot(x, y,
       pch = 16,
       col = ifelse(inside, "red", "blue"),
       xlim = c(0, 1), ylim = c(0, 1), asp = 1)
  # 사분원 경계 y = sqrt(1 - x^2)
  xs <- seq(0, 1, length.out = 400)
  lines(xs, sqrt(1 - xs^2), lwd = 3)

  title(main = sprintf("Monte Carlo π 추정  (n = %d)  →  π̂ = %.5f (± %.5f)", 
                       n, pi_hat, 1.96 * se_hat))
  legend("bottomleft", pch = 16, col = c("red", "blue"),
         legend = c("원 내부", "원 외부"), bty = "n")

  invisible(list(pi_hat = pi_hat, se = se_hat))
}

simulate_pi_plot(100)
simulate_pi_plot(1000)
simulate_pi_plot(10000)
```

### 예제

- 주사위 던지기 시뮬레이션
    - 난수 생성(sample)을 통해 주사위를 여러번 던질 수록 확률분포가 균일분포에 근접한다.
```r
set.seed(1)
dice <- sample(1:6, size=1000, replace=TRUE)
table(dice) / 1000
barplot(table(dice))
```

- [중심극한정리](./class_4.md)
    - 어떤 분포의 표본평균은 n이 커질 수록 정규분포에 가까워진다.

- 로또
```r
set.seed(1)
lotto <- sort(sample(1:45, 6))
lotto
```

- Random Walk
    - 난수를 사용해 랜덤한 움직임을 시각화
```r
set.seed(1)
steps <- sample(c(-1, 1), size=100, replace=TRUE)  # -1 or +1
pos <- cumsum(steps)
plot(pos, type="l", col="blue", main="1차원 랜덤워크", ylab="위치", xlab="시간")
```