#通过用户输入数字，计算阶乘

try:
    number = int(input("请输入数字："))
except:
    print("请输入数字！")

#声明变量
cheng = 1

#循环计算阶乘
for i in range(1,number+1):
    cheng = cheng * i

print("阶乘为：",cheng)