library(readxl)
data <- read_excel("D:/桌面/var数据.xlsx")
windowsFonts(A=windowsFont('黑体'))

attach(data)
opar <- par(no.readonly = T)
par(mfrow=c(1,2))
plot(M2, main='货币供应量M2（亿元）走势图', ylab='货币供应量M2', type='l', lwd=2, family ='A')
plot(I, main='一天同业拆借利率走势图（%）', ylab='利率', type='l', lwd=2, family ='A')
par(opar)
detach(data)

attach(data)
plot(SH, main='上证指数走势图', ylab='上证指数', type='l', lwd=2, family ='A')
lines(SZ, main='深证指数走势图', ylab='深证指数', type='l', lwd=2, family ='A')
detach(data)

