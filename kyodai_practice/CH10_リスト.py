# e = list()
n = list(range(4))
print(n)

newList = list()
t = "a textbook of Python"
tlist = t.split()
for str in tlist:
    print(str)
    newList.append(str)  # add ではなく　appendが正。これは難しい。


print(newList[-2])
print(tlist)


# 歩の添え字
a = [1, 2, 3, 54, 5]
print(a[-1])

# スライス
b = a[1:3]  # 3については戦闘からのインデックスでないことに注意。　長さでもなくて、後ろからのインデックスになる。

print(b)

# 二つのリストを統合するにはextendを用いる。
a = [5, 1, 3, 2]
b = [343, 21, 43]
a.extend(b)
print(a)


# リストのリスト

a = [[1, 2, 3], [4, 5, 6], [4, 6, 9]]
sum = 0
for row in a:
    for element in row:
        sum += element

print(a)
print(sum)


# 内包表記というもの、Pythonのアルゴリズムでこのようなものが有ったように思えるが･･･。
a = [i*i for i in range(5)]
print(a)
