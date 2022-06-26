import tkinter as tk
import tkinter.filedialog
import math

# tkinterfiledialogだけを利用する例

# rootウィンドウはwithdrow()メソッドを読んで隠す

root = tk.Tk()
root.withdraw()

filename = tkinter.filedialog.asksaveasfilename()
# fsa
# ファイル名がもらえなければ終了
# fsa

if filename:
    pass
else:
    print("No file specified")
    exit()

#
# 正弦波の重ね合わせで鋸波を近似する。
#
# w=sin(t)+ sin(2t)/2+sin(3t)/3+sin(4t)/4
#
# 2周期分、全体は1000ステップで、高調波は5番目まで

cycles = 2
steps = 1000
harmonics = 5
# ファイルがひらけないときのエラー対応
try:
    with open(filename, 'w') as file:
        for i in range(steps):

            angle_in_degree = 360*cycles*i/steps

            angle = math.radians(angle_in_degree)
            s = str(angle_in_degree)
            w = 0.0
            for i in range(1, harmonics+1):
                w += math.sin(angle*(i))/i
                s = s+"," + str(w)  # csvファイル形式にするために必要

            # print(s)

            file.write(s+"\n")

        print("writing to file "+filename+" is finished")

except IOError:
    print("unable to open file")
