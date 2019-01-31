startdate <- as.Date('1996-01-01')
enddate <- as.Date('2009-01-01')
num <- c(132616, 132410, 124250, 109126, 106988, 120900, 138369, 160300, 187341, 206068, 221056, 235445, 260552, 274618)
Energy <- ts(num,start=c(1996),end=c(2009))
plot(Energy,type='b',
     lty=2,pch=2,lwd=2,
     main='我国1996-2009年能源生产总量趋势图',
     xlab='年份',ylab='生产量',family='STKaiti')
library(TTR)
SMA1 <- SMA(Energy, n=3)
SMA2 <- SMA(SMA(Energy, n=3),n=3)
EMA1 <- EMA(Energy,ratio=0.6)
EMA2 <- EMA(EMA(Energy,ratio=0.6),ratio=0.6)
all <- data.frame(Energy, SMA1, SMA2, EMA1, EMA2)
S1 <- sum((abs(all$SMA1-all$Energy))/all$Energy,na.rm = T)/(14-sum(is.na(all$SMA1)))
S2 <- sum((abs(all$SMA2-all$Energy))/all$Energy,na.rm = T)/(14-sum(is.na(all$SMA2)))
E1 <- sum((abs(all$EMA1-all$Energy))/all$Energy,na.rm = T)/(14-sum(is.na(all$EMA1)))
E2 <- sum((abs(all$EMA2-all$Energy))/all$Energy,na.rm = T)/(14-sum(is.na(all$EMA2)))
a <- data.frame(c(NA, S1, S2, E1, E2))
all <- data.frame(all,a)

par(mfrow=c(2,2))
plot(SMA(Energy, n=3),xlab='一次移动平均法 n=3',family='STKaiti',type='b')
plot(SMA(SMA(Energy, n=3),n=3),xlab='二次移动平均法 n=3',family='STKaiti',type='b')
plot(EMA(Energy,ratio=0.6),xlab='一次指数平滑法 a=0.6',family='STKaiti',type='b')
plot(EMA(EMA(Energy,ratio=0.6),ratio=0.6),xlab='二次指数平滑法 a=0.6',family='STKaiti',type='b')


