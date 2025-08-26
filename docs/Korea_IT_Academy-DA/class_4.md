# Class 4 - R Statistics Distribution function

- 기초통계학 통계 분포를 이해하고, R 프로그래밍을 통해 분포 그래프 확인

```r

## before distribution option
# d : probability density (확률 밀도)
# p : cumulative probability (누적 확률)
# q : quantiles (분위수)
# r : random number (난수)

## List
if(0)"
  1.  norm    | normal distribution
  2.  exp     | exponential distribution
  3.  gamma   | gamma distribution
  4.  pois    | poison distribution
  5.  weibull | weibull distribution
  6.  cauchy  | cauchy distribution
  7.  beta    | beta distribution
  8.  t       | student's t distribution
  9.  f       | Ficher's F distribution
  10. chisq   | chisqure distribution
  11. binom   | binomial distribution
  12. geom    | geometric distribution
  13. hyper   | hypergeometric distribution
  14. logis   | logistic distribution
  15. lborm   | log normal distribution
  16. nbinom  | negative binomial distribution
  17. unif    | uniform distribution
  18. wilcox  | Wilcoxon rank sum
  19. sigrank | Wilcoxon signed rank
"

## example

## standard normal distribution
curve(dnorm(x), from = -3, to = 3, main = "Density of N(0,1)", ylab="")

## Chisqure distribution
d <- c(1,5,10)
dev.off() # delete recent plot
for(i in d) curve(dchisq(x,df=i),0,20,add=TRUE)
```