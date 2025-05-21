import streamlit as st

st.title("Streamlit UI 部品サンプル")

name = st.text_input("お名前は？")
age = st.number_input("年齢は？", min_value=0, max_value=120)
like_python = st.checkbox("Pythonは好きですか？")
color = st.radio("好きな色は？", ["赤", "青", "緑"])
hobby = st.selectbox("趣味を選んでください", ["読書", "運動", "ゲーム", "音楽", "その他"])

if st.button("送信"):
    st.write(f"こんにちは {name} さん！")
    st.write(f"{age}歳ですね。")
    st.write("Pythonが好きです！" if like_python else "Pythonは好きじゃないのですね。")
    st.write(f"好きな色は {color} ですね。")
    st.write(f"趣味は {hobby} ですね。")
