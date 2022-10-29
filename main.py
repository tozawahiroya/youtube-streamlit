import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image
import time


st.title('Streamlit 入門')

st.write(' プログレスバーの表示')
"Start!!"

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i+1)
    time.sleep(0.1)



left_column, right_column = st.columns(2)
button = left_column.button('右カラムに列を表示')
if button:
    right_column.write("テスト文です")

expander = st.expander('問い合わせ')
expander.write("aaaa")


# text = st.text_input('あなたの趣味を教えてください')
# '好きな数字は、', text,'です'

# condition = st.slider("あなたの今の調子は？" ,0,100,50)
# '好きな数字は、', condition,'です'



# st.write('check and selectbox')

# # if st.checkbox('showimage'):
# #     img = Image.open('/Users/tozawahiroya/Desktop/VS code/[pyscript]tech0-3 Tozawa Hiroya/images/Topic1.png')
# #     st.image(img, caption="Tozawa", use_column_width=True)

# option = st.selectbox(
#     '好きな番号',
#     list(range(1,11))
# )


# '好きな数字は、', option,'です'

# st.table(df.style.highlight_max(axis=0))

# df = pd.DataFrame(
#     np.random.rand(100,2)/[50,50] + [35.69, 139.70],
#     columns=['lat','lon']
# )

# st.map(df)









