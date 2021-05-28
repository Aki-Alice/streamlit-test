# 各ライブラリのインポート
import streamlit as st   
import numpy as np
import pandas as pd
from PIL import Image
import time

# タイトルの表示
st.title("Streamlit 超入門")

# テキストの追加
st.write("プログレスバーの表示")
"Start!!"

# プログレスバー（ロードバー）の表示
latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f"Iteration {i+1}")
    bar.progress(i + 1)
    time.sleep(0.1)

"Done!!!"


# 2カラムレイアウトにする
left_column, right_column = st.beta_columns(2)
# 左側にボタンを設置し、押されたら右側にテキストを表示する
button = left_column.button("右カラムに文字を表示")
if button:
    right_column.write("ここは右カラム")

# expanderの追加
expander1 = st.beta_expander("問い合わせ1")   
expander1.write("問い合わせ1の回答")
expander2 = st.beta_expander("問い合わせ2")   
expander2.write("問い合わせ2の回答")
expander3 = st.beta_expander("問い合わせ3")   
expander3.write("問い合わせ3の回答")


# テキスト入力エリアとスライダーセレクトをサイドバーに追加
#text = st.sidebar.text_input("あなたの趣味を教えてください。")
#condition = st.sidebar.slider("あなたの今の調子は？", 0, 100, 50)
# 入力結果表示
#"あなたの趣味：", text
#"コンディション", condition

#　セレクトボックスの設置
#option = st.selectbox(
#    "あなたが好きな数字を教えてください。",
#    list(range(1,11))
#)
# セレクトボックスで選択された値を表示
#"あなたの好きな数字は、", option, "です。"

# 画像の表示/非表示のチェックボックスを追加する
# if st.checkbox("Show Image"):
#    # 表示する画像のソース
#    img = Image.open("wonderwatch.jpg")
#    # 画像表示
#    st.image(img, caption="懐中時計", use_column_width=True)


# DataFrameの作成
#df = pd.DataFrame(
#    np.random.rand(100, 2)/[50, 50] + [35.69, 139.70],
#    columns=["lat", "lon"],
#)
# DataFrameの表示
# st.dataframe(df.style.highlight_max(axis=0)) #<= 動的なDataFrameの表示に使う
# st.table(df.style.highlight_max(axis=0)) #<= 静的なDataFrameの表示に使う

# mapの表示
# st.map(df)

# DataFrameを各種グラフでプロットする
# st.line_chart(df) #<= 一般的な折れ線グラフ
# st.area_chart(df) #<= 中身が塗られた折れ線グラフ
# st.bar_chart(df)  #<= 棒グラフ


# マジックコマンド
#"""
# 章
## 節
### 項

#```python
#import streamlit as st   
#import numpy as np
#import pandas as pd
#```
#"""