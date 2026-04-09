import streamlit as st
import google.generativeai as genai

st.title("🌍 我的多語練習機")

# 這裡請務必確保引號存在
my_key = "AIzaSyCGx2MX5Q1FT5fDluU_wevaT75-d6_xBpI"

try:
    genai.configure(api_key=my_key)
    model = genai.GenerativeModel('gemini-pro')
except Exception as e:
    st.error(f"連線設定失敗：{e}")

text = st.text_input("輸入中文句子：", "今天天氣很好")

if st.button("開始多語轉換"):
    with st.spinner('AI 正在思考中...'):
        try:
            prompt = f"請將『{text}』翻譯成日文、韓文、泰文。每一種語言請提供：1.原文 2.羅馬拼音 3.一句簡單的情境說明。請用 Markdown 格式清楚排列。"
            response = model.generate_content(prompt)
            st.success("轉換完成！")
            st.markdown(response.text)
