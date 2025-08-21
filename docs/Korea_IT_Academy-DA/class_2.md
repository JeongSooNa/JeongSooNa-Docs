# Class 2 - R Package 사용하기

R은 자체적으로 내장 된 함수 및 패키지들을 사용해 다양한 작업을 수행할 수 있으나, 여러 개발자로부터 다양한 패키지를 제공받아 유용하게 사용할 수 있다.  
이는 Open Source Platform, 프로그래밍 언어의 특징이기도 하며, 사용자의 필요에 따라 손쉽게 설치 및 사용할 수 있다.  
패키지들에 대한 정보는 [R Packages](https://cran.r-project.org/web/packages/available_packages_by_name.html)에서 확인 가능하며, 필요에 따라 원하는 패키지를 검색하여 설치 및 사용하는 것을 추천한다.

### 패키지 설치

```r
install.packages("readxl")
```

### 패키지 불러오기

```r
library(readxl)
```

### 패키지 사용

```r
a <- read_excel("test.xlsx")
print(a)
```

### 패키지 업데이트

```r
update.packages("readxl")
```

### 패키지 삭제

```r
remove.packages("readxl")
```