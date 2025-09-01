# R Statistical Simulation

- R을 통해 다양한 통계 모의 실험을 구현

### 2개의 별

```r
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

### 중심극한정리

```r
n<-10
sec<-0.2
n.repeat<-200
set.seed(124)
x<-rep(0,n.repeat)
x11()
for(r in 1:n.repeat){
  u<-runif(n,-1,1)
  z1<-mean(u)
  #par(new=T)
 
  hist(x[1:r],freq=T,ylim=c(0,60),xlim=c(-1,1),xlab="mean",
       breaks=seq(-1,1,0.1),main=paste("CLT : mean of ",n,"observations"))
  x[r]<-z1
  rug(x[1:r],col="blue")
  text(0.9,60,r)
  #Sys.sleep(sec)
}

par(new=T)
z<-seq(-1,1,0.1)
m<-0
s<-sqrt(4/12/n)
p.norm<-pnorm(z,m,s)
d.norm<-(p.norm[2:21]-p.norm[1:20])*n.repeat
z.1<-seq(-0.95,0.95,0.1)
plot(d.norm~z.1,col="red",type="p",lwd=2,xlim=c(-1,1),xlab="",ylim=c(0,60),
     ylab="",main="")
```

### Galton의 핀볼

```r
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


### 프랙탈 패턴

```r
x0<-c(-1.5,1.5)
y0<-c(-1,1.6)
plot(x0,y0,type="n",xlab="",ylab="",main="TriangleEverywhere")
core<-matrix(0,3,2)
list<-matrix(0,243*9,2)
list.1<-matrix(0,243*9,2)
center<-c(0,0)
core[1,]<-c(0,2/3)
core[2,]<-c(-1/sqrt(3),-1/3)
core[3,]<-c(1/sqrt(3),-1/3)
#polygon(core,col="red")
triangle<-function(center,f){
  p.1<-center+f*core[1,]
  q.1<-center+f*core[2,]
  r.1<-center+f*core[3,]
  polygon(rbind(p.1,q.1,r.1),border="red",lwd=2)
}
triangle(center,1)
for(j in 1:3) list[j,]<-core[j,]

for(i in 1:6){
  triangle(list[i,],0.5^i)
  for(k in 1:3){
    list.1[count,]<-list[j,]+(0.5^i)&core[k,]
    count<-count+1
  }
  list<-list.1
  Sys.sleep(1)
}

trianlge_rec<-function(center,f,death)

# 포함 확률
n<-100
d<-0.5
set.seed(123)
x<-runif(n,-2,2)
y<-runif(n,-2,2)
r<-d/2

circle<-matrix(0,nrow=37,ncol=2)

par(mar=rep(6,4),bg="white",col.axis="black",col.lab="black",fg="black",lwd=2)
plot(c(-2,2),c(2,2),xlab="",ylab="",xaxs="i",yaxs="i",xlim=c(-2,2),ylim=c(-2,2),
     color.axis="white",type="n",main="")

for(i in 1:37){
  thete[i]<-i*2*pi/36
  circle[i,1]<-r*cos(theta[i])
  circle[i,2]<-r*sin(theta[i])
}
for(i in 1:n){
  par(new=T)
  plot(cbind(x[i]+circle[,1],y[i]+circle[,2]),xlab="",ylab="",
       xlim=c(-2,2),ylim=c(-2,2),type="l",xaxs="i",yaxs="i",lwd=2)
  #Sys.sleep(0.1)
}

count<-0
for(rr in 1:5000){
  target<-runif(2,-2,2)
  temp<-cbind(x,y)-matrix(rep(target,n),byrow=T,ncol=2)
  cover<-ifelse(min(apply(temp^2,1,sum)) < r^2,1,0)
  count<-count+cover
  color<-ifelse(cover < 0.5,"blue","red")
  par(new=T)
  plot(target[1],target[2],xlab="",ylab="",xlim=c(-2,2),ylim=c(-2,2),xaxs="i",yaxs="i",
       cex=1.5,pch=19,col=color)
}
count
#mtext(side=1,line=3,paste(paste("count =",count),"/5000"))
#savePlot("covering by circles_1",type="jpg")

##margin
mtext(side=1,at=20,line=0,"Bottom No. 0")
mtext(side=1,at=20,line=1,"Bottom No. 1")
mtext(side=1,at=20,line=2,"Bottom No. 2")
mtext(side=1,at=20,line=3,"Bottom No. 3")
mtext(side=2,at=20,line=0,"Left No. 0")
mtext(side=2,at=20,line=1,"Left No. 1")
mtext(side=2,at=20,line=2,"Left No. 2")
mtext(side=3,at=20,line=0,"Top No. 0")
mtext(side=3,at=20,line=1,"Top No. 1")
mtext(side=4,at=20,line=0,"Right No. 0")
```

### 산불
- Forest Fire, 21*21

```r
par(mar=rep(4,4))
V<-matrix(0,21,21)
V[11,11]<-1
image(x=1:21,y=1:21,z=V,axes=F,col=c("white","red","black"),
      breaks=c(-0.5,0.5,1.5,2.5),xlab="",ylab="",main="Fire Process")
abline(h=0.5+(0:21),v=0.5+(0:21))

sec<-0.5
V.0<-V
count<-1
time<-0
set.seed(124)

while(count>0){
  time<-time+1
  for(i in 1:21){
    for(j in 1:21){
      if(V.0[i,j]==1){
        if((runif(1)>0.5)&(i<=20)) if(V.0[i+1,j]==0) V[i+1,j]<-1
        if((runif(1)>0.5)&(i>=2)) if(V.0[i-1,j]==0) V[i-1,j]<-1
        if((runif(1)>0.5)&(i<=20)) if(V.0[i,j+1]==0) V[i,j+1]<-1
        if((runif(1)>0.5)&(i>=2)) if(V.0[i,j-1]==0) V[i,j-1]<-1
        V[i,j]<-2
      }
    }
  }
  par(new=T)
  image(x=1:21,y=1:21,z=V,axes=F,col=c("white","red","black"),
        breaks=c(-0.5,0.5,1.5,2.5),xlab="",ylab="",main="")
  abline(h=0.5+(0:21),v=0.5+(0:21))
  burnt<-sum(V==2)
  mtext(side=1,at=11,line=2,burnt)
  Sys.sleep(sec)
  V.0<-V
  count<-sum(V.0==1)
  mtext(side=1,at=11,line=2,burnt,col="white")
}
burnt<-sum(V==2)
mtext(side=1,at=20,line=2,paste("burnt = ",burnt))
mtext(side=1,at=2,line=2,paste("time = ",time))
```