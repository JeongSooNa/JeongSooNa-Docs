# Class 10 - R Statistical Simulation

- R을 통해 다양한 통계 모의 실험을 구현
- 대표적인 통계 모의 실험을 통해 실습 진행

### 동전 던지기

- 동전을 던져 앞면과 뒷면이 나올 확률 계산
- 시행 횟수가 많아질 수록 0.5에 가까워진다.

```r
set.seed(10)
n <- 100
coin <- sample(c(0,1), n, replace = TRUE)

ratio <- c(mean(coin == 1), mean(coin == 0))
bp <- barplot(ratio,
              ylim = c(0,1),
              names.arg = round(ratio, 2))
abline(h = 0.5, lwd = 2, lty = 2, col = "red")
```

### Galton의 핀볼

- Francis Galton이 만든 장치로, 위에서 구슬을 떨어뜨리면, 아래로 내려오는 동안 여러 층의 못을 만나 왼쪽 또는 오른쪽으로 무작위로 이동하는 실험
- 각 구슬은 결국 이항분포(왼쪽:0.5 , 오른쪽:0.5)로 바닥에 쌓이는데, 구슬이 많아질수록 전체 모양이 정규분포에 가까워진다.
- 많은 독립적인 무작위 사건들의 합은 정규분포에 근사한다라는 중심극한정리를 직관적으로 보여주는 예

```r
set.seed(2025)
peg <- 10    # 못 배치의 층 수
n   <- 80    # 공 갯수
p   <- 0.5   # 확률

# 못의 좌표 계산
pegs <- do.call(rbind, lapply(0:(peg-1), function(k) 
  cbind(x=seq(-k*0.5, k*0.5, 1), y=-k)
))

# 바닥 칸 좌표(x)과 해당 칸에 쌓인 공 개수를 기록할 벡터
slots <- seq(-peg*0.5, peg*0.5, by=1)
stack <- setNames(integer(length(slots)), as.character(slots))

# 화면 초기화 함수
init_plot <- function(){
  # 현재까지 가장 많이 쌓인 높이에 맞춰 y축 범위를 자동 조정
  max_stack <- max(0L, stack)
  y_min <- -peg - 0.4*(max_stack + 3)
  
  op <- par(mar=c(1,1,2,1)); on.exit(par(op))
  plot(NA, xlim=c(min(slots)-1, max(slots)+1), ylim=c(y_min, 1),
       xlab="", ylab="", axes=FALSE, asp=1,
       main="Galton 핀볼: 공이 하나씩 쌓이는 모습")
  
  # 못(peg) 표시
  points(pegs, pch=16, cex=0.8, col="gray40")
  
  # 이미 쌓인 공 표시
  if (sum(stack) > 0) {
    for (i in seq_along(slots)) if (stack[i] > 0)
      points(rep(slots[i], stack[i]), -peg - 0.4*seq_len(stack[i]),
             pch=21, bg="tomato", col="black", cex=0.9)
  }
}

# 공 하나씩 시뮬레이션
init_plot()
for (b in 1:n) {
  init_plot()         # 새로운 공 시작 → 화면 초기화
  x <- 0              # 시작 위치 (맨 위 중앙)
  
  # 레벨별로 peg을 만나 좌/우 이동
  for (s in 1:peg) {
    step <- if (runif(1) < p) 0.5 else -0.5  # 좌/우 결정
    segments(x, -(s-1), x+step, -s, col="dodgerblue3")  # 이동 경로 선
    x <- x + step
    points(x, -s, pch=16, cex=0.6, col="dodgerblue3")   # 현재 위치 점
    Sys.sleep(0.03)  # 잠깐 멈춰서 "떨어지는" 느낌
  }
  
  # 바닥 칸에 쌓기
  key <- as.character(x)
  stack[key] <- stack[key] + 1L
  
  init_plot()  # 업데이트된 쌓임 반영
  points(x, -peg - 0.4*stack[key], pch=21, bg="tomato", col="black", cex=1)
  Sys.sleep(0.05)
}
```

### 프랙탈 패턴

- 자기유사성(self-similarity) : 확대해도 원래와 비슷한 모양이 반복되는 패턴

- 자연계에서 흔히 보이는 현상 : 나뭇가지, 브로콜리, 번개, 해안선, 혈관 등

- 단순한 규칙을 반복하여 특정 구조가 생성

- 시에르핀스키 삼각형 (Chaos Game)
  - 꼭짓점 하나를 랜덤하게 고르고, 현재 위치와 꼭짓점의 중점으로 이동
  - 단순한 규칙을 무작위 반복을 하면 삼각형 속에 삼각형이 무한히 반복되는 패턴이 생성
```r
set.seed(2025)
N <- 20000   # 점 개수 (많을수록 삼각형이 또렷해짐)

# 정삼각형 꼭짓점 정의
A <- c(0,0); B <- c(1,0); C <- c(0.5, sqrt(3)/2)
verts <- rbind(A,B,C)

# 시작점 (삼각형 안 아무 곳이나 가능)
x <- 0.1; y <- 0.1
xs <- numeric(N); ys <- numeric(N)

for(i in 1:N){
  v <- verts[sample(1:3,1), ]   # 무작위로 꼭짓점 하나 선택
  x <- (x+v[1])/2               # 현재 위치와 꼭짓점의 "중점"으로 이동
  y <- (y+v[2])/2
  xs[i] <- x; ys[i] <- y        # 점 기록
}

plot(xs, ys, pch=".", col="blue", asp=1, axes=FALSE,
     main="Chaos Game: Sierpinski Triangle")

```

- 고사리 패턴 (Barnsley Fern, IFS:Iterated Function System)
  - 확률적으로 네 가지 선형 변환을 반복 적용.
  - 반복만 했는데 실제 자연의 고사리 잎 같은 형태가 생성
  - 자연의 복잡성도 사실은 간단한 규칙의 반복으로 설명될 수 있다는 예
```r
set.seed(2025)
N <- 50000     # 점 개수
x <- 0; y <- 0 # 초기 좌표
xs <- numeric(N); ys <- numeric(N)

for(i in 1:N){
  r <- runif(1)   # [0,1) 구간 무작위 확률
  # 네 가지 아핀 변환 중 하나를 확률적으로 선택
  if(r < 0.01){        # 줄기
    xn <- 0; yn <- 0.16*y
  } else if(r < 0.86){ # 큰 잎
    xn <- 0.85*x + 0.04*y
    yn <- -0.04*x + 0.85*y + 1.6
  } else if(r < 0.93){ # 왼쪽 작은 잎
    xn <- 0.20*x - 0.26*y
    yn <- 0.23*x + 0.22*y + 1.6
  } else {             # 오른쪽 작은 잎
    xn <- -0.15*x + 0.28*y
    yn <- 0.26*x + 0.24*y + 0.44
  }
  x <- xn; y <- yn
  xs[i] <- x; ys[i] <- y
}

plot(xs, ys, pch=".", col="forestgreen", asp=1, axes=FALSE,
     main="Barnsley Fern (Fractal)")

```

### 산불

- 산불 시뮬레이션
- 현재 상태를 시각화
  - 0 : 빈칸
  - 1 : 화재
  - 2 : 화재 종료

```r
par(mar = rep(4, 4))
set.seed(10)

n   <- 21            # 격자 한 변 길이
p   <- 0.5           # 확산 확률

# 초기 상태
V <- matrix(0L, n, n)
V[(n+1)/2, (n+1)/2] <- 1L # 중앙

# 그리기 함수
draw <- function(V, time) {
  image(1:n, 1:n, V, axes = FALSE,
        col = c("white", "red", "black"),
        breaks = c(-0.5, 0.5, 1.5, 2.5),
        xlab = "", ylab = "", main = "산불 시뮬레이션")
  abline(h = 0.5 + 0:n, v = 0.5 + 0:n)
  mtext(side = 1, at = n*0.5, line = 2,
        sprintf("burning=%d  burnt=%d  time=%d",
                sum(V==1L), sum(V==2L), time))
}

# 4방향 이동 벡터 (상,하,좌,우)
dirs <- rbind(c( 1, 0),  # 아래
              c(-1, 0),  # 위
              c( 0, 1),  # 오른쪽
              c( 0,-1))  # 왼쪽

time  <- 0L
draw(V, time)

# 시뮬레이션
while (any(V == 1L)) {
  time <- time + 1L
  V0 <- V  # 이번 스텝

  for (i in 1:n) for (j in 1:n) if (V0[i, j] == 1L) {
    # 4방향으로 확산
    for (k in 1:nrow(dirs)) {
      ni <- i + dirs[k, 1]; nj <- j + dirs[k, 2]
      if (ni >= 1 && ni <= n && nj >= 1 && nj <= n) {
        if (V0[ni, nj] == 0L && runif(1) < p) V[ni, nj] <- 1L
      }
    }
    V[i, j] <- 2L # 현재 칸은 다 탄 것으로 처리
  }

  draw(V, time)
  Sys.sleep(0.2)
}
```