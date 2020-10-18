#
def square_root(x):
    rnew = x
    #
    diff = rnew-x/rnew
    diff = abs(diff)
    # if(diff<0):
    #     diff=abss
    while(diff > 1.0e-6):
        r1 = rnew
        r2 = x/r1
        rnew = (r1+r2)/2
        print(r1, rnew, r2)
        diff = abs(r1-r2)
    return rnew


#
# ここからメインプログラム
v = 2
r = square_root(2)
print("結果は", r)
