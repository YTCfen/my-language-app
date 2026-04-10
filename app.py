import streamlit as st
import google.generativeai as genai

st.set_page_config(page_title="🔎多語練習機 🔊", page_icon="🌍")
st.title("🔎多語練習機 🔊")

try:
    API_KEY = st.secrets["MY_API_KEY"]
    genai.configure(api_key=API_KEY.strip())
except:
    st.error("請在 Secrets 設定中配置 MY_API_KEY")

text = st.text_input("輸入中文句子：", "這多少錢？")

if st.button("開始多語轉換"):
    # 嘗試不同的模型名稱清單
    models_to_try = ['gemini-1.5-flash', 'gemini-1.5-pro', 'gemini-pro']
    response = None
    
    with st.spinner('正在尋找可用模型並翻譯中...'):
        for model_name in models_to_try:
            try:
                model = genai.GenerativeModel(model_name)
                prompt = f"""
                請將『{text}』翻譯成日文、韓文、泰文。
                請嚴格遵守以下格式輸出：
                
                ### [國旗] [語言名稱]
                <div style="background-color: #FFFF00; padding: 10px; border-radius: 5px; color: black; font-weight: bold; margin-bottom: 5px;">原文：[原文]</div>
                <div style="background-color: #E0E0E0; padding: 10px; border-radius: 5px; color: black; margin-bottom: 10px;">羅馬拼音：[拼音]</div>
                
                **💡 相關生詞：**
                * [單字1] ([拼音]) - [中文意思]
                
                **📝 其他例句：**
                1. [例句1] (拼音)
                
                ---
                """
                response = model.generate_content(prompt)
                if response:
                    st.success(f"成功連線 (模型: {model_name})")
                    st.markdown(response.text, unsafe_allow_html=True)
                    break
            except:
                continue
        
        if not response:
            st.error("所有模型連線均失敗。這通常代表您的 API Key 尚未開通 Gemini API 權限，請至 Google AI Studio 確認該 Key 是否已啟用。")

st.caption("✨ 每天練習一個句子，同時精通日韓泰！")
