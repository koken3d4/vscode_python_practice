# 演習26
# for文を使うと、ターミナルを選択範囲で実行ではどうにも上手く描写されない。
# for文を使わないでベタにコードを記述すると、正常に描写される。
# for文を使って描写させようとすると、ターミナルでPythonファイルを実行を選択する必要が有る。ただその場合は、exit()を用いてPythonのシェル?から抜ける必要が有る。

from turtle import*
n=5
for i in range(n):
    forward(100)
    angle=360/n
    left(angle)
    # done()

# forward(100)
# left(72)
# forward(100)
# left(72)
# forward(100)
# left(72)
# forward(100)
# left(72)
# forward(100)
# left(72)



done()
print("end")