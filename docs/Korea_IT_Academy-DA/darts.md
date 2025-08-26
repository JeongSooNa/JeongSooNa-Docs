### R Darts Game

```r
#양궁 (원형)
color<-heat.colors(5)
for(j in 1:5){
  if(j>=2) par(new=T)
  pie(c(1),radius=1-0.2*(j-1),col=color[j],label=NA,border=NA)
  text(1.1-0.2*j,0,j)
}

n<-10
score<-0
for(i in 1:n){
  x<-runif(2,-1,1)
  points(x[1],x[2],pch=18,cex=1.2)
  r<-sqrt(sum(x*x))
  score<-score+ifelse(r<1,5-floor(r*5),0)
}
text(-1,-1,"score")
text(-0.75,-1,score)

#양궁(원형의 확률로 파이차트 표시(다트))
360/2/pi #57.3도(=1radian)
atan(1/1) #0.7853982(라디안에서의 45도)
atan(1/1)*360/2/pi #45도((1,1)에서의 중심각)

arrow<-rep(0,5)
for(i in 1:5){
  arrow[i]<-(0.2*(6-i))^2-(0.2*(5-i))^2 #((0.2*i)^2-(0.2*(i-1))^2)
}
pie(arrow,radius=1,col=rev(color),labels=c("1","2","3","4","5"),border=NA)

n<-10
score<-0
for(i in 1:n){
  x<-runif(1,-1,1)
  y<-runif(1,-1,1)
  points(x,y,pch=18,cex=1.2)
  r<-sqrt(x^2+y^2)
  score_1<-0
  x<-1
  y<-(-1)
  do<-atan(y/x)*360/2/pi
  do
  if(x<0&&y>=0){
    do<-do+180
  }
  do
  if else(x=<0&&y<0){
    do<-do+180
  }
  do
  if else(x>0&&y=<0){
    do<-do+270
  }
  score<-score+ #ifelse(r<1,5-floor(r*5),0)
}
x<-runif(1,-1,1)
y<-runif(1,-1,1)
x;y
do<-atan(y/x)*360/2/pi
do

##열지도

#끝잇기 알고리즘 (열 정렬)
install.packages("gclus")
library(gclus)
round(cor(iris[1:4]),digits=2)
order<-order.endlink(cor(iris[1:4]))
order

#dist() (행 정렬)
dist(t(iris[,1:4]))
sqrt(sum((iris[,1]-iris[,2])^2))
order<-order.endlink(-dist(t(iris[,1:4])))
order

test.data<-read.table("C:/Users/Administrator/Desktop/test_matrix_1.txt",header=F)
test.data
F<-as.matrix(test.data)

dist(t(F))
order<-order.endlink(-dist(t(F)))
order
```