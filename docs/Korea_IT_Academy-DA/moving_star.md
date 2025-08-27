# R Moving Star

```r
#움직이는 그림

#2개의 별
n.cycle<-36
theta<-c(0,pi/4)
x<-cos(theta)
y<-sin(theta)
circle<-seq(0,pi/4,pi/32)
x.circle<-cos(circle)
y.circle<-sin(circle)            

par(mar=rep(6,4),bg="darkblue",col.axis="white",
    col.lab="white",fg="white",lwd=2)
color<-c("cyan","yellow")
plot(x,y,type="n",xlim=c(-1.2,1.2),ylim=c(-1.2,1.2))
text(x,y,"*",col=color,cex=4)
par(new=T)
plot(x.circle,y.circle,xlim=c(-1.2,1.2),ylim=c(-1.2,1.2),
     xlab="",ylab="",col="magenta")

alpha<-2*pi/n.cycle

for(r in 1:(2*n.cycle)){
  x<-cos(theta+alpha*r)
  y<-sin(theta+alpha*r)
  x.circle<-cos(circle+alpha*r)
  y.circle<-sin(circle+alpha*r)
  plot(x,y,type="n",xlim=c(-1.2,1.2),ylim=c(-1.2,1.2))
  text(x,y,"*",col=color,cex=4)
  par(new=T)
  plot(x.circle,y.circle,xlim=c(-1.2,1.2),ylim=c(-1.2,1.2),
       xlab="",ylab="",col="magenta")
  Sys.sleep(0.2)
}
```