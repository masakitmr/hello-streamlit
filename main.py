import streamlit as st

st.title("簡単な診断アプリ")
name = st.text_input("お名前を入力してください：")
age = st.number_input("年齢を入力してください：", min_value=0)

if st.button("診断する"):
    if age >= 20:
        st.success(f"{name}さんは成人です。")
    else:
        st.info(f"{name}さんは未成年です。")
