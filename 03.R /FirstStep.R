#----------------------------------------------第一章 R语言介绍--------------------------------------------------------
help.start()
install.packages('vcd')                #下载包
help(package='vcd')                    #包说明
search()                               #查看那些包已经加载
library()                              #显示库中有哪些包
library(grid)                          #加载包
library(vcd)                           #加载包
help("Arthritis") 
Arthritis
example(Arthritis)
q()
lmfit <- lm(mpg~wt,data=mtcars)
lmfit
summary(lmfit)                         #统计概要
help(lm)                               #查看lm对应部分
plot(lmfit) 
predict(lmfit,mynewdata)

#---------------------------------------------第二章 数据结构----------------------------------------------------------
a <- c(1,2,5,3,6,-2,4)                  #数值型向量
b <- c('one','two','three')             #字符型向量
c <- c(TRUE,TRUE,TRUE,FALSE,TRUE,FALSE) #逻辑性向量
a <- c('k','j','h','a','c','m')
a[3] 
a[c(1,3,5)]
i <- c(1,3,5)
a[i]
a[c(2:6)]
a[2:6]

#-------------------------------------------矩阵--------------------------------------
y <- matrix(1:20,nrow = 5,ncol = 4)
y
x <- matrix(c(1,3,4,6,5,7,6,3),nrow = 2,ncol = 4)                 #默认排列
x
rnames <- c("First",'Second')
cnames <- c('one','two','three','four')
x <- matrix(x,nrow=2,ncol=4,dimnames=list(rnames,cnames),byrow=T) #按行排列
x
x <- matrix(1:10,nrow = 2,byrow = T)
x[c(1:4)]
x[2,]
x[,2]
x[1,4]
x[1,c(3,4)]
x[,c(1,2,3)]
a <- c(1,5,4,6)
b <- c(6,3,47,6)
c <- c(4,6,1,3)
d <- c(5,2,2,23)
#----------------------------------------数据框-------------------------
ID <- c(1,2,3,4)
age <- c(25,34,28,52)
diabetes <- c('Type1','Type2','Type3','Type4')
status <- c('Poor','Improved','Excellent','Poor')
patientdata <- data.frame(ID,age,diabetes,status,row.names = ID)
patientdata
plot(patientdata$ID,patientdata$age)
patientdata[1:2]                                 #默认取列
patientdata[c('ID','status')]
a <- patientdata$age                             #向量形式
a <- patientdata[c('age')]                       #数据框形式
table(patientdata$diabetes,patientdata$status)   #列联表

#1 $
summary(mtcars$mpg)
plot(mtcars$mpg,mtcars$disp)
plot(mtcars$mpg,mtcars$wt)
#2 attach() 注意原有重名变量会被优先选择
attach(mtcars)
  summary(mpg)
  plot(mpg,disp)
  plot(mpg,wt)
detach(mtcars)
# with()
with(mtcars,{
  stats <<- summary(mpg)                        #<<为替代标准赋值符，应用到with以外
  stats
})
stats

#----------------------------------------因子-------------------------------------
ID <- c(1,2,3,4)
age <- c(25,34,28,52)
diabetes <- c('Type1','Type2','Type3','Type4')
status <- c('Poor','Improved','Excellent','Poor')
diabetes <- factor(diabetes) #名义变量 
status <- factor(status,order=T,levels=c('Poor','Improved','Excellent')) #有序变量  labels为值标签
patientdata <- data.frame(ID,age,diabetes,status,row.names = ID)
patientdata
str(patientdata) #显示对象的结构类型
summary(patientdata) #显示对象的统计概要

#---------------------------------------实用函数---------------------------------------
patientdata
rbind(patientdata,c(5,31,'Type4','Poor'))    #按行合并
a <- c(2,3,4,5)
cbind(patientdata,a)                         #按列合并
length(patientdata)                          #ob数量
dim(patientdata)                             #维度
str(patientdata)                             #显示结构
class(patientdata)                           #显示类型
name(patientdata)                            #显示各成分名称
ls()                                         #显示当前对象
rm()                                         #删除对象
rm(list=ls())                                #删除所有对象
fix()                                        #直接编辑对象

#-----------------------------------------------第三章 图形初阶----------------------------------------------------------
dose <- c(20,30,40,45,60)
drugA <- c(16,20,27,40,60)
drugB <- c(15,18,25,31,40)
plot(dose,drugA,type='b') #Type=b表示同时绘制点和线

par()                #表示列出当前绘图所有参数
par(no.readonly = T) #表示列出当前绘图非可读参数（可修改）
opar <- par(no.readonly = T) #将默认参数赋值，方便最后恢复
plot(dose,drugA,type='b')
par(opar)

plot(dose,drugA,main='dose',type='b',pch=25,cex=2,lty=5,lwd=2,bg='blue',col.axis='green',col.lab='yellow',col.main='red',fg='red')
#tpye=b同时绘制点线、pch点符号（21-25指定col和bg填充颜色）、cex点大小、lty线类型、lwd线宽度
#cex.axis/lab/main/sun 调整大小
#font.axis/lab/main/sub 调整字体 1：常规，2：粗体，3：斜体，4：粗斜体，5：符号字体
n <- 7
pie(rep(1,n),rainbow(10))

#-----------------------------------------------------字体----------------------
windowsFonts(A=windowsFont('华文行楷'))
plot(dose,drugA,main='药品',type='b',family='A') #使用windows的字体库，mac使用quartzFonts()

#------------------------------------------------------图形大小--------------------
opar <- par(no.readonly = T) 
par(pin=c(2,3)) #宽高 par(mai=c(1,0.5,1,0.2),mar=c(5,4,4,2)+0.1)  mai英寸 mar英分
par(lwd=2,cex=1.5)
par(cex.axis=.75,font.axis=3)
plot(dose,drugA,type='b',pch=19,lty=2,col='red')
plot(dose,drugB,type='b',pch=23,lty=6,col='blue',bg='green')
par(opar)

plot(dose,drugA,type='b',
     col='red',lty=2,pch=2,lwd=2,
     main='Clinical Trials for Drug A',
     sub='This is hypothetical data',
     xlab='Dosage',ylab='Drug Response',
     xlim=c(0,60),ylim=c(0,70)) #xlim限制x轴范围

abline(lm(drugA~dose))
abline(h=c(1,5,7),v=seq(1,10,2),lty=2,col='blue') #辅助线，h为y轴，v为x轴
dev.new()
title(main='a',col.main='red',sub='b',col.sub='blue')

#-----------------------------------------------图例-------------------------------
install.packages('Hmisc')
dose <- c(20,30,40,45,60)
drugA <- c(16,20,27,40,60)
drugB <- c(15,18,25,31,40)
opar <- par(no.readonly = T) 
plot(dose,drugA,type='b',
     pch=15,lty=1,col='red',ylim=c(0,60),
     main='Drug Dosage',ylab='Drug Response'
     )
lines(dose,drugB,type='b',
      pch=17,lty=2,col='blue')
abline(h=c(30),lwd=1.5,lty=2,col='gray')
library(Hmisc)
minor.tick(nx=3,ny=3,tick.ratio=0.5)
legend('topleft',inset=.05,title='Drug Type',c('a','b'),
       lty=c(1,2),pch=c(15,17),col=c('red','blue'))
par(opar)

#--------------------------------------------文本标注-----------------------------
attach(mtcars)
plot(wt,mpg,
     main='Mileage vs. Car Weight',
     xlab='Weight',ylab='Mileage',
     pch=18,col='blue') #pos1234上下左右
text(wt,mpg,row.names(mtcars),
     cex=0.6,pos=4,col='red')
detach(mtcars)

opar<-par(no.readonly = T)
par(cex=1.5)
plot(1:7,1:7,type='n')
text(3,3,'Example f default text')
text(4,4,family='mono','Example of mono-spaced text')
text(5,5,family='serif','Example of serif text')
par(opar)

help(plotmath)
demo(plotmath) #数学标注

#----------------------------------------------------图形组合-------------------------------
attach(mtcars)
opar <- par(no.readonly = T)
par(mfrow=c(2,2))
plot(wt,mpg)
plot(wt,disp)
hist(wt)
boxplot(wt)
par(opar)
detach(mtcars)

attach(mtcars)
layout(matrix(c(1,1,2,3),2,2,byrow=T)) #22表示两行两列
hist(wt)
hist(mpg)
hist(disp)
detach(mtcars)

attach(mtcars)
layout(matrix(c(1,1,2,3),2,2,byrow=T),widths=c(3,1),heights=c(1,2)) #widths/heights各列或各行宽度组成的一个响亮
hist(wt)
hist(mpg)
hist(disp)
detach(mtcars)

#---------------------------------------------精细控制图----------------------------------------
opar <- par(no.readonly = T)
par(fig=c(0,0.8,0,0.8))
plot(mtcars$wt,mtcars$mpg,
     xlab='Miles Per Gallon',
     ylab='Car Weight')
par(fig=c(0,0.8,0.55,1),new=T)
boxplot(mtcars$wt,horizeontal=T,axe=T)#在上方添加箱线图 new表示添加到现有图形 横向0~0.8，纵向0.55~1
par(fig=c(0.65,1,0,0.8),new=T)
boxplot(mtcars$mpg,axe=F)#在右侧添加箱线图 横向0.65~1 纵向0~0.8
mtext('Enhanced Scatterplot',side=3,outer=T,line=-3)
par(opar)

#-----------------------------------------------第四章 基本数据管理----------------------------------------------------------
manager <- c(1,2,3,4,5)
date <- c('10/24/08','10/28/08','10/1/08','10/12/08','5/1/09')
country <- c('US','US','UK','UK','UK')
gender <- c('M','F','F','M','F')
age <- c(32,45,25,39,99)
q1 <- c(5,3,3,3,2)
q2 <- c(4,5,5,3,2)
q3 <- c(5,2,5,4,1)
q4 <- c(5,5,5,NA,2)
q5 <- c(5,5,2,NA,1)
leadership <- data.frame(manager,date,country,gender,age,
                         q1,q2,q3,q4,q5,stringsAsFactors = F)

#-------------------------创建新变量-------------------------
mydata <- data.frame(x1=c(2,2,6,4),
                     x2=c(3,4,2,8))
mydata <- transform(mydata,
                    sumx=x1+x2,
                    meanx=(x1+x2)/2)

leadership <- within(leadership,{                #重新编码
  agecat <- NA
  agecat[age>75] <- 'Elder'
  agecat[age>=55&age<=75] <- 'Middle Aged'
  agecat[age<55] <- 'Young'})
fix(leadership)                                   #手动修改变量

names(leadership)
names(leadership)[2]<-'testdate'
names(leadership)[6:10]<-c('item1','item2','item3','item4','item5')

#---------------------缺失值------------------------------
y <- c(1,2,3,NA)
is.na(y)
is.na(leadership[,6:10])
x <- c(1,2,3,5/0)
is.infinite(x)
is.nan(x)

x <- c(1,2,NA,3)
y <- x[1]+x[2]+x[3]+x[4]
z <- sum(x,na.rm = T)
na.omit(leadership) #移除含有缺失值的行
leadership

#-----------------------日期值------------------
?as.Date
mydates <- as.Date(c('2007-06-22','2004-02-13'))     #默认日期格式
mydates
strDate <- c('01/05/1965','08/16/1975')
dates <- as.Date(strDate,'%m/%d/%Y')
strDate
dates
myformat <- '%m/%d/%y'
leadership$date <- as.Date(leadership$date,myformat)
leadership

date()   #返回现在时间
Sys.Date()   #返回今天日期
today <- Sys.Date()
format(today, format='%B %b %Y')
format(today,format='%A')

startdate <- as.Date('2004-02-13')
enddate <- as.Date('2011-01-22')
days <- enddate-startdate
days
dob <- as.Date('1956-10-12')
difftime(today,dob,units = 'weeks')

set.seed(1234)

ind <- sample(2, nrow(iris), replace = TRUE, prob = c(0.7,0.3))

trainData <- iris[ind==1,]

testData <- iris[ind==2,]



