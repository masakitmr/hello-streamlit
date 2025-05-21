import streamlit as st
import numpy as np

st.title("がん予測アプリ（仮）")

st.write("以下の数値を入力してください：")

mean_radius = st.number_input("平均半径", min_value=0.0)
mean_texture = st.number_input("平均テクスチャ", min_value=0.0)
mean_perimeter = st.number_input("平均周囲長", min_value=0.0)
mean_area = st.number_input("平均面積", min_value=0.0)

if st.button("予測する"):
    # 入力値をまとめる
    data = np.array([[mean_radius, mean_texture, mean_perimeter, mean_area]])

    # 仮の予測ロジック
    if data[0][0] > 15 and data[0][2] > 100:
        st.error("予測結果：がんの可能性あり")
    else:
        st.success("予測結果：がんの可能性なし")
