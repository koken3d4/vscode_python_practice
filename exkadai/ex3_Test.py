# xの平方根を求める
inputNumber = input("rangeの数：")
try:
    inputnumber = int(inputNumber)
except ValueError:
    print(inputnumber, "は数値に変換できません")
    exit()
except:
    print("予期しないエラーです")
    exit()

inputNumber = int(inputNumber)  #
for i in range(inputNumber):
    if(i == 3):
        print(i)
    elif(i == 5):
        print(i)
    else:
        print("つらいさんなのだ")
print("end")


a = 1
b = 0
if(a == 1):
    if(b == 0):
        print("YES")
else:
    print("NO")


c = 2.9979238593e8
na = 6.02214076323

form = 'kousokuha{0:12.8g}m/s,abogadorosuuha{1:12.8}.molとなります。'
print(form.format(c, na))
