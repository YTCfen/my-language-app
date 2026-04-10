import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="多語練習機", page_icon="🌍")
st.title("🌍 我的多語練習機")

# 這裡貼上你的 API Key
API_KEY = "這裡換成你的API_KEY"

# 設定 API
genai.configure(api_key=API_KEY)

text = st.text_input("輸入中文句子：", "這多少錢？")

if st.button("開始多語轉換"):
    with st.status("正在連線...", expanded=True) as status:
        try:
            # 修正點：使用目前 Google 推薦的完整模型路徑
            # 如果這個還不行，請試著改回 'gemini-1.5-flash'
            model = genai.GenerativeModel('models/gemini-1.5-flash')
            
            prompt = f"將『{text}』翻譯成日文、韓文、泰文。每種語言請提供：1.原文 2.羅馬拼音 3.一句簡單的情境說明。"
            
            st.write("AI 翻譯中...")
            response = model.generate_content(prompt)
            
            status.update(label="翻譯完成！", state="complete", expanded=False)
            st.markdown(response.text)
            
        except Exception as e:
            status.update(label="連線失敗", state="error")
            st.error(f"錯誤訊息：{e}")
            st.info("提示：如果持續 404，代表您的帳號權限僅支援特定模型，請告知我。")
