import streamlit as st
import google.generativeai as genai

st.title("⚡️ 最簡測試")

# 請確保這串 Key 是正確的
genai.configure(api_key="這裡換成你的API_KEY")

if st.button("連線測試"):
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    # 改用 try 之外最直接的方式
    st.write("連線中...")
    response = model.generate_content("Hi") 
    st.write("AI 說了：" + response.text)
