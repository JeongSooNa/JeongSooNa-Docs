# Class 11 - R Visualization

### 그래픽 시스템

- Base
    - plot, hist, boxplot 등 R에서 기본적으로 제공하는 시각화 기초
    - lines, points, text 등을 사용해 그래프 내 옵션을 추가할 수 있으며, par를 사용해 여러 그래프를 한눈에 볼  수 있다.
    ```r
    par(mfrow=c(2,2))  
    hist(iris$Sepal.Length)
    boxplot(iris$Sepal.Length)
    plot(iris$Sepal.Length, iris$Sepal.Width)
    plot.ts(Nile)
    par(mfrow=c(1,1)) 
    ```

- Lattice
    - lattice 패키지 기반
    ```r
    install.packages("lattice")
    library(lattice)
    ```
    - 입력한 변수에 따른 패널 분리에 강점이 있으며, 함수 한번에 완성된 그래프를 얻을 수 있다.
    ```r
    xyplot(Sepal.Length ~ Sepal.Width | Species, data=iris)
    ```

- ggplot2
    - grammar of graphics
    - 다양한 확장성이 있으며, 복잡한 그래프도 작성이 가능하다.
    ```r
    install.packages("ggplot2")
    library(ggplot2)
    ggplot(iris, aes(x=Sepal.Width, y=Sepal.Length, color=Species)) +
        geom_point(size=2) +
        theme_minimal() +
        labs(title="ggplot2 Scatter Plot")
    ```

- 그래프 특징 비교
```r
# Base
plot(iris$Sepal.Width, iris$Sepal.Length, col=iris$Species, pch=19,main="Base")

# Lattice
library(lattice)
xyplot(Sepal.Length ~ Sepal.Width, group=Species, data=iris,auto.key=TRUE, main="Lattice")

# ggplot2
library(ggplot2)
ggplot(iris, aes(Sepal.Width, Sepal.Length, color=Species)) +
    geom_point(size=2) +
    theme_bw() +
    labs(title="ggplot2")
```

- 그래프 배치 비교
```r
# Base
par(mfrow=c(1,2))
hist(iris$Sepal.Length)
boxplot(iris$Sepal.Length)
par(mfrow=c(1,1))

# Lattice
histogram(~ Sepal.Length | Species, data=iris)

# ggplot2
ggplot(iris, aes(Sepal.Length)) +
    geom_histogram(binwidth=0.3, fill="steelblue", color="white") +
    facet_wrap(~Species)
```

### 다변량 자료 시각화

- Scatterplot Matrix
    - 여러 변수 간 산점도 확인
```r
# Base
pairs(iris[1:4], main="Pairs plot of Iris")

# Lattice
splom(~iris[1:4] | Species, data=iris, groups=Species, auto.key=TRUE)

# GGally
install.packages("GGally")
library(GGally)
ggpairs(iris, columns=1:4, aes(color=Species))
```

- Stars Plot
    - 각 관측치를 다각형 형태로 표현(변수 수가 많을수록 효과적이다.)
```r
stars(mtcars[,1:7],
    key.loc=c(14,2), draw.segments=TRUE, col.lines=NA)
```

- Radar Chart
    - 원형 좌표계에 변수들을 배치 (성능 비교에 적합)
```r
install.packages("fmsb")
library(fmsb)

# set data
df <- as.data.frame(rbind(
    max=apply(mtcars[,1:5], 2, max),
    min=apply(mtcars[,1:5], 2, min),
    mtcars[1:3,1:5]   # 3개 data example
))
radarchart(df, axistype=1, pcol=1:3, plty=1, cglcol="grey")
```

- Chernoff Faces
    - 다변량 데이터를 얼굴 특징에 매핑 (직관적인 패턴 파악)
```r
install.packages("aplpack")
library(aplpack)

bball <- read.csv("http://datasets.flowingdata.com/ppg2008.csv")
faces(bball[,2:16], labels=bball$Name, face.type=2)
```
