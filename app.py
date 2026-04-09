python
import streamlit as st
import google.generativeai as genai

# 設定網頁標題
st.title("🌍 我的多語練習機")

# 這裡要貼上你剛才拿到的 API 鑰匙
# 暫時先直接貼在這裡，之後我教你更安全的做法
genai.configure(api_key="這裡換成你剛才複製的那串API_KEY")

# 輸入框
text = st.text_input("輸入中文句子：", "今天天氣很好")

if st.button("開始多語轉換"):
    model = genai.GenerativeModel('gemini-1.5-flash')
    prompt = f"請將『{text}』翻譯成日文、韓文、泰文。每一種語言請提供：1.原文 2.羅馬拼音 3.一句簡單的情境說明。請用美觀的格式排列。"
    
    response = model.generate_content(prompt)
    st.markdown(response.text)
