# このファイルは、本文中に載っている命令文を太メイしているサンプル文
# for分をもう一度やってみる
initial = 20
rx = 1
r1 = 0
r2 = 0
for i in range(15):
    r1 = rx
    r2 = initial/r1
    r_new = (r1+r2)/2
print(r1, r2, r_new)

# forbun
for i in range(15):
    if i == 0:
        continue
    if i == 9:
        break
    print(i)

#fsa
x = 0
for i in range(19):
    y = i
    print(i)
#

#プリント文を最後に入れることでfor文中のprintを表示させる事のテスト。正直無駄。
x=0
for i in range(5,20,3):
    print(i)
print("end")

P58
for i in ["三条", "四条", "五条"]:
    for j in ["河原町", "烏丸", "堀川"]:
        cross = i+j
        print(cross)
print("end")
