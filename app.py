import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="多語練習機", page_icon="🌍")
st.title("🌍 我的多語練習機")

# 這裡請貼上你的 API Key
API_KEY = "AIzaSyCbE5dZScjtY37wSCpP3C-pZGJ_inWhkXE"

# 設定 API
genai.configure(api_key=API_KEY)

text = st.text_input("輸入中文句子：", "這多少錢？")

if st.button("開始多語轉換"):
    # 建立一個進度提示
    with st.status("正在連線至 Google AI...", expanded=True) as status:
        try:
            # 使用最新且最快的 flash 模型
            st.write("正在組織翻譯內容...")
            model = genai.GenerativeModel('gemini-pro')
            
            prompt = f"將『{text}』翻譯成日文、韓文、泰文。每種語言請提供：1.原文 2.羅馬拼音 3.一句簡單的情境說明。"
            
            st.write("AI 正在翻譯中 (通常需 3-5 秒)...")
            response = model.generate_content(prompt)
            
            status.update(label="翻譯完成！", state="complete", expanded=False)
            st.markdown(response.text)
            
        except Exception as e:
            status.update(label="連線失敗", state="error")
            st.error(f"錯誤訊息：{e}")
