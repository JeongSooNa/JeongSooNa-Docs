# Class 4 - R Statistics Distribution function

- 기초통계학 통계 분포를 이해하고, R 프로그래밍을 통해 분포 그래프 확인

### Before Distribution Options
  - d : probability density (확률 밀도)
  - p : cumulative probability (누적 확률)
  - q : quantiles (분위수)
  - r : random number (난수)

### 분포 함수

1. 정규분포 (normal distribution)
  - norm

![jpg](../img/normal_distribution.png)

  - 평균과 표준편차로 정의되는 분포로, 자연 현상이나 측정값에서 흔히 볼 수 있다.
  - 통계학 분포에서 가장 기초가 되는 연속확률분포로, 분석 결과 해석, 일반화 등에 가장 많이 사용된다.
  - 표준정규분포 [ N(0,1) ] : 평균이 0, 분산이 1인 정규분포
  - 중심극한정리 : 표본의 갯수 n이 커질 수록 어떠한 분포든 표뵨 평균의 분포는 정규분포에 가까워진다.
  ```r
  #중심극한정리
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

2. 지수분포 (exponential distribution)
  - exp

3. (gamma distribution)
  - gamma

4. (poison distribution)
  - pois

5. (weibull distribution)
  - weibull

6. (cauchy distribution)
  - cauchy

7. (beta distribution)
  - beta

8. (student's t distribution)
  - t

9. (Ficher's F distribution)
  - f

10. (chisqure distribution)
  - chisq

11. (binomial distribution)
  - binom

12. (geometric distribution)
  - geom

13. (hypergeometric distribution)
  - hyper

14. (logistic distribution)
  - logis

15. (log normal distribution)
  - lborm

16. (negative binomial distribution)
  - nbinom

17. (uniform distribution)
  - unif

18. (Wilcoxon rank sum)
  - wilcox

19. (Wilcoxon signed rank)
  - sigrank


