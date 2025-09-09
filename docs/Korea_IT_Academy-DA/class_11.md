# Class 11 - R Visualization

### 데이터 시각화 기초

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

- ggplot2는 다양한 옵션을 갖고있다. 이를 보다 쉽게 사용하기 위한 ggThemeAssist를 활용할 수 있다.
```r
install.packages("ggThemeAssist")
library(ggThemeAssist)
gg <- ggplot(mtcars, aes(x = hp, y = mpg, colour = as.factor(cyl))) + geom_point()
ggThemeAssist(gg)
```

### 다변량 데이터 시각화

- Scatterplot Matrix
    - 여러 변수 간 산점도 확인
```r
# Base
pairs(iris[1:4])

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

### 범주형 데이터 시각화

- Barplot
    - 단일 범주형 자료 분포 확인
    - barplot(table(x))
    - 기초 그래프로 범주형 데이터를 테이블로 만들어 각 빈도를 확인하기에 유용하다.

- Mosaic Plot
    - 교차표(다차원 분할표) 시각화
    - 블록 면적 = 빈도
```r
data(Titanic)
mosaicplot(Titanic, color=c("red","blue"))

install.packages("vcd")
library(vcd)
install.packages("vcdExtra")
library(vcdExtra)

mosaic(Titanic, shade=TRUE, legend=TRUE)

data("Bartlett")
mosaic3d(Bartlett, shade=TRUE) # 3차원 모자이크 plot
```

- Association Plot (assocplot)
    - 기대빈도와의 차이를 시각화, 잔차를 표시하는 특징이 있다.
```r
mt1 <- margin.table(Titanic, c(1,4))
assocplot(mt1)
```

- Fourfold Plot
    - 2x2 교차표에 특화
    - 독립성, 비율 차이 확인
```r
mt2 <- margin.table(Titanic, c(2,4))
fourfoldplot(mt2)
```

### 공간 데이터 시각화
- 3차원 시각화
    - scatterplot3d: 정적 3D 산점도
    - rgl: 회전/확대가 가능한 동적 3D 그래프
    - car::scatter3d: 회귀면 포함한 3D 산점도
```r
# 정적 3D
install.packages("scatterplot3d")
library(scatterplot3d)
scatterplot3d(iris[,1:3], color=as.numeric(iris$Species),
              pch=19, main="3D Scatterplot")

# 동적 3D
install.packages("rgl")
library(rgl)
plot3d(iris$Sepal.Length, iris$Sepal.Width, iris$Petal.Length,
       col=as.numeric(iris$Species), size=5)
```

- 표면 그래프 (Surface plots)
    - contour(): 등고선
    - filled.contour(): 색상 등고선
    - persp(): 3차원 표면
    - lattice::wireframe, levelplot: 세련된 격자형 시각화
```r
volcano

# 등고선
contour(volcano, col="grey40")

# 색상 등고선
filled.contour(volcano, color=terrain.colors)

# 3D 투시도
persp(volcano, theta=30, phi=20, col="lightblue", expand=0.5)

# Lattice
library(lattice)
wireframe(volcano, drape=TRUE, colorkey=TRUE)
levelplot(volcano, col.regions=terrain.colors(100))
```

- 공간 데이터 시각화
    - ggmap: 지도 API 불러오기
    - 좌표 위 도형 표시
```r
install.packages("ggmap")
library(ggmap)

# 지도 가져오기
map1 <- get_map(location="Seoul", zoom=12, maptype="roadmap")
g <- ggmap(map1)

# 위치 표시
g + geom_point(aes(x=126.9780, y=37.5665), color="red", size=4) +
    labs(title="GwangHwaMoon")
```
