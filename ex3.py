# xの平方根を求める
count = 0
x = 2
#
rnew = x
#
diff = rnew - x/rnew
if(diff < 0):
    diff = -diff
while(diff > 1.0E-6):
    r1 = rnew
    r2 = x/r1
    rnew = (r1+r2)/2
    print(r1, rnew, r2)
    diff = r1-r2
    if(diff < 0):
        diff = -diff
    count += 1
# print("countの回数は："+count)  # 課題、カウントはintのため文字列として結合出来ないというわけか。
print("end")
