class Dentak():
    def __init__(self):  # defの後に半角スペースが必要。そうしないと認識してくれない__は一体なんだろう?
        self.first_term = 0
        self.second_term = 0
        self.result = 0
        self.operation = "+"

    def do_operation(self):
        if self.operation == "+":
            self.result = self.first_term+self.second_term
        elif self.operation == "-":
            self.result = self.first_term-self.second_term


# メインプログラム
dentaku = Dentak()
while True:
    f = int(input("First term "))
    dentaku.first_term = f
    o = input("Operation (+ or -)")
    dentaku.operation = o
    s = int(input("Second term "))
    dentaku.second_term = s
    dentaku.do_operation()
    r = dentaku.result
    print("Result ", r)

##クラス変数という概念がPython独自かもしれない。そのような変数は他の言語では確認出来ていないので、さてどうしたものか?
