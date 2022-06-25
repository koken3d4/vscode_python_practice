# 平方根を求める
import math
x = 123  # 静的型付けなので方を明記する必要がない。
rootx = math.sqrt(x)
print(rootx)


#　制御構造の復習
for i in range(50, 100, 3):
    print(i)


# while
print("while文の動作確認")
input("入力して下さい")
counter = 0
while (counter < 100):
    counter += 1
    print(counter)
