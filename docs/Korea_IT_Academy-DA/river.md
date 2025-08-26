### R River Time Series Data Analytics

- 1807~1956년도 스웨덴 강 수위 데이터(시계열 데이터)를 활용한 시계열 분석

```r
install.packages('forecast')
#install.packages("lmtest")

#auto.arima
library('forecast')
#library("lmtest")
# libray 호출 error
riv <- read.csv("gota-river-near-sjotopvannersbur.csv",header=T)
riv <- riv[,2]
riv <- riv[-151]
riv <- riv[-151]
riv <- ts(riv) # time series data 시계열 data로 변환
plot.ts(riv,main="plot for riv")

lriv <- log(riv)
#plot.ts(lriv,main="plot for log(riv)")
# Error in log(riv) : non-numeric argument to mathematical function
```