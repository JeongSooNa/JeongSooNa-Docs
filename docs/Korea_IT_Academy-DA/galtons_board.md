# R Galton Board

### Summary

![jpg](../img/galton_board.png)

- Galton의 상자, 핀볼 등으로 불리는 위 장치는 충분한 표본 크기를 갖는 이항 분포(p=0.5)가 정규분포에 가까워진다는 것을 증명하기 위한 장치로, 정규분포의 생성을 시각적으로 보여준다.

- 이를 R 코드로 구현해보자.

### R Code

```r
#Galton의 핀볼
p<-0.5
sec<-0.05
n.repeat<-100
count<-rep(0,11)

par(yaxt="n",mar=c(2,2,2,2),bg="white")
x1<-c(-10,0,10)
y1<-c(0,10,0)
plot(x1,y1,xlim=c(-11,11),xaxp=c(-10,10,10),ylim=c(-10,10),type="n",xlab="",ylab="",
     main=paste("Quincunx (n=10,p=",p,")"))
segments(-10,0,0,10,lty="dotted",col="red")
segments(10,0,0,10,lty="dotted",col="red")
abline(h=0,col="red",lwd=2)

set.seed(123)
for(r in 1:n.repeat){
  e<-2*rbinom(10,size=1,prob=p)-1
  x<-c(0,cumsum(e))
  y<-10:0
  text(10,10,r-1,col="white")
  text(10,10,r)
 
  for(step in 0:10){
    if(step>0){
      par(new=T)
      plot(x[1:step],y[1:step],xlim=c(-11,11),xaxp=c(-10,10,10),ylim=c(-10,10),xlab="",
           ylab="",pch=19,cex=1.2,col="white")
    }
    par(new=T)
    plot(x[1:(step+1)],y[1:(step+1)],xlim=c(-11,11),xaxp=c(-10,10,10),ylim=c(-10,10),xlab="",
         ylab="",pch=c(rep(1,step),19),cex=1.2,col="red")
    if(step<10){
      segments(x[step+1]-1,y[step+1]-1,x[step+1],y[step+1],lty="dotted")
      segments(x[step+1]+1,y[step+1]-1,x[step+1],y[step+1],lty="dotted")
    }
    Sys.sleep(sec)
  }
  par(new=T)
  plot(x[step+1],y[step+1],xlim=c(-11,11),xaxp=c(-10,10,10),ylim=c(-10,10),xlab="",
       ylab="",pch=19,cex=1.2,col="white")
  par(new=T)
  plot(x[step+1],y[step+1],xlim=c(-11,11),xaxp=c(-10,10,10),ylim=c(-10,10),xlab="",
       ylab="",pch=1,cex=1.2,col="red")
 
  count[x[11]/2+6]<-count[x[11]/2+6]+1
  par(new=T)
  plot(x[11],-10-1/3+(1/3)*count[x[11]/2+6],xlim=c(-11,11),xaxp=c(-10,10,10),ylim=c(-10,10),xlab="",
       ylab="",pch=12,cex=1.2,col="red")
  Sys.sleep(sec)
} 
```