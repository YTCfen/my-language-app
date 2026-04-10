import streamlit as st
import google.generativeai as genai

st.title("🌍 多語練習機 - 自動偵錯版")

# 1. 填入你的 Key
API_KEY = st.secrets["MY_API_KEY"]
genai.configure(api_key=API_KEY.strip())

# 2. 自動偵測可用的模型（這步最關鍵）
available_models = []
try:
    for m in genai.list_models():
        if 'generateContent' in m.supported_generation_methods:
            available_models.append(m.name)
except Exception as e:
    st.error(f"獲取模型清單失敗：{e}")

# 3. 介面設計
text = st.text_input("輸入中文：", "這多少錢？")

if st.button("開始翻譯"):
    if not available_models:
        st.error("此 API Key 似乎沒有可用的模型權限。")
    else:
        # 自動選擇清單中的第一個可用模型
        target_model = available_models[0]
        st.info(f"正在使用模型：{target_model}")
        
        try:
            model = genai.GenerativeModel(target_model)
            prompt = f"將『{text}』翻譯成日文、韓文、泰文。每種語言請提供：1.原文 2.羅馬拼音 3.一句簡單的情境說明。"
            response = model.generate_content(prompt)
            st.success("翻譯成功！")
            st.markdown(response.text)
        except Exception as e:
            st.error(f"翻譯執行失敗：{e}")
