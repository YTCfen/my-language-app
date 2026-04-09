import streamlit as st
import google.generativeai as genai

# 1. 網頁標題
st.title("🌍 我的多語練習機")

# 2. 設定你的鑰匙 (請確保引號內是你的 API Key)
genai.configure(api_key="這裡換成你的API_KEY")

# 3. 輸入框
text = st.text_input("輸入中文句子：", "今天天氣很好")

# 4. 按鈕觸發
if st.button("開始多語轉換"):
    # 這裡我們換成最穩定的 gemini-pro 模型
    model = genai.GenerativeModel('gemini-pro')
    
    # 使用 try...except 確保安全
    try:
        prompt = f"將『{text}』翻譯成日文、韓文、泰文。每種語言請提供：1.原文 2.羅馬拼音 3.一句簡單的情境說明。"
        response = model.generate_content(prompt)
        
        # 顯示結果
        st.success("完成！")
        st.markdown(response.text)
        
    except Exception as e:
        st.error(f"抱歉，連線出了點問題：{e}")
