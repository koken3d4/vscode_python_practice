import pandas as pd

csv_input = pd.read_csv(
    filepath_or_buffer=".\practice\秋田県人口データ.csv", encoding="ms932", sep=",")
# インプットの項目数（行数 * カラム数）を返却します。
print(csv_input.size)
# 指定したカラムだけ抽出したDataFrameオブジェクトを返却します。

# カラムの抽出
print(csv_input[["年", "女"]])
# print(csv_input[["年"],["女"]]) 　# 複数のカラムを抜き出すときは個々を[]でかこうのではなく全体を囲う

# データの抽出その2
# print(csv_input[["女"]>100000])
print(csv_input[csv_input["女"] > 160000])
print(csv_input[(csv_input["女"] > 160000) & (csv_input["男"] > 150000)])# 条件をつけるときは&か|　でその条件を()で囲ってそのなかにcsv_inputを記述する
