library(readxl)
sxfj <- read_excel("~/Documents/经济预测与决策/山西汾酒数据.xlsx", range = "B1:G234")
sxfj1 <- data.frame(scale(sxfj,center=T,scale=T))
fit <- lm(收盘价 ~ 开盘价 + 最高价 + 最低价 + 成交量 + 成交额, data = sxfj1)

library(stargazer)
sxfj2 <- data.frame(sxfj)
stargazer(sxfj2, out = '~/Desktop/s.html')
stargazer(cor(sxfj1), type = 'html', out = '~/Documents/经济预测与决策/图片/cor.html')
plot(sxfj1)
stargazer(fit, type = 'html', out = '~/Documents/经济预测与决策/图片/lm.html')
dwtest(fit)
stargazer(anova(fit), type = 'html', out = '~/Documents/经济预测与决策/图片/anova.html')

par(family='STKaiti')
par(mfrow=c(2,2))
plot(fit)
library(lmtest)
bp <- bptest(fit)
stargazer(bp, type = 'html', out = '~/Documents/经济预测与决策/图片/bp.html')

library(car)
v <- vif(fit)
stargazer(vif(fit), type = 'html', out = '~/Documents/经济预测与决策/图片/vif.html')
stargazer(vif(fit),sqrt(vif(fit)) > 2, type = 'html', out = '~/Documents/经济预测与决策/图片/vif.html')

library(psych)
KMO(cor(sxfj1))
bartlett.test(sxfj1)
par(mfrow=c(1,1))
sxfj_cor <- cor(sxfj1[,-6])
fa.parallel(sxfj_cor, n.obs = 233, fa='both', n.iter=100)
fa <- fa(sxfj_cor, nfactors = 2, rotate='varimax', fm='pa')
fa
factor.plot(fa, lables=rownames(fa$loadings))
fa.diagram(fa, simple = F)
fa$weights

f1 <- sxfj1$开盘价*fa$weights[1]+sxfj1$最高价*fa$weights[2]+sxfj1$最低价*fa$weights[3]+sxfj1$成交量*fa$weights[4]+sxfj1$成交额*fa$weights[5]
f2 <- sxfj1$开盘价*fa$weights[6]+sxfj1$最高价*fa$weights[7]+sxfj1$最低价*fa$weights[8]+sxfj1$成交量*fa$weights[9]+sxfj1$成交额*fa$weights[10]
sxfj2 <- data.frame(sxfj1,f1,f2)
fit2 <- lm(收盘价 ~ f1 + f2, data = sxfj2)
summary(fit2)
cor(f1,f2)
vif(fit2)
stargazer(fit2, out = '~/Desktop/fit2.html')
par(mfrow=c(2,2))
plot(fit2)

