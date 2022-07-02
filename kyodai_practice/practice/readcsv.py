import csv
import glob
import os
import pandas

# from email.quoprimime import quote

# vscode的には/でOK\\ではどうNANDだろう?->　\\ や　\　でもいけた。VSCodeだから?
filepath = ".\kyodai_practice\practice\秋田県人口データ.csv"
# filepath = "./practice/秋田県人口データ.csv"  # vscode敵には/でOK\\ではどうNANDだろう?
csv_file = open(filepath, "r", encoding="ms932", errors="", newline="")
f = csv.reader(csv_file, delimiter=",", doublequote=True,
               lineterminator="\r\n", quotechar='"', skipinitialspace=True)
for row in f:
    print(row)

# # for file in files:
# #     print(file)
# str =os.path.abspath(".")
# print(str)

# files =os.listdir(".")  ## ディレクトリないのファイル、ディレクトリを取得するメソッド
# for file in files:
#     print(file)
