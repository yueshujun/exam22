

#用循环来遍历101-200之间的数字

#声明变量记录素数总数

sum = 0

for i in range(101,201):
    #声明变量标记
    flag = 0
    for j in range(2,i):
        if i % j == 0:
            flag = 1
            break
    if flag == 0:
        print("素数：",i)
        sum += 1
print("101-200之间共有素数：%d个"%sum)