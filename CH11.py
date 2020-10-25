import os

print(os.getcwd())

f=open('日本語ファイル.txt','w')    #w はたぶんwriteモードのことを意味する。
f.write('日本語\n nihong \n nihongo \n')
f.close()

# 日本語ファイル。txtを読み込みようにopenにして、その内容を表示させる
f=open('日本語ファイル.txt','r') # rなのでリードを意味するだろう。
s=f.read()
f.close()
print(s)


with open('日本語ファイル.txt','r') as ff:
    line=ff.read()

print(line) #範囲が外れているのに問題なく読めるのか。スコープ。