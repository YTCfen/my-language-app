import streamlit as st
import google.generativeai as genai

# 設定網頁標題與外觀
st.set_page_config(page_title="🔎多語練習機 🔊", page_icon="🌍")
st.title("🔎多語練習機 🔊")

# 1. 讀取 Secrets 中的 API Key
try:
    API_KEY = st.secrets["MY_API_KEY"]
    genai.configure(api_key=API_KEY.strip())
except Exception:
    st.error("❌ 請在 Streamlit Secrets 設定中配置 MY_API_KEY")
    st.stop()

# 2. 使用者輸入
text = st.text_input("請輸入想練習的中文句子：", "這多少錢？")

if st.button("開始多語轉換"):
    # 建立多個備選模型名稱，應對不同帳號權限
    # 注意：'gemini-1.5-flash' 是目前最推薦的
    model_list = ['gemini-1.5-flash', 'gemini-1.5-flash-latest', 'gemini-pro']
    success = False

    with st.spinner('AI 正在拆解語言並造句中...'):
        for model_name in model_list:
            try:
                model = genai.GenerativeModel(model_name)
                
                # 核心指令 (Prompt)
                prompt = f"""
                你是一個語言學習專家。請將『{text}』翻譯成日文、韓文、泰文。
                請嚴格依照以下格式輸出，不要有前言：

                ### [國旗] [語言名稱]
                <div style="background-color: #FFFF00; padding: 10px; border-radius: 5px; color: black; font-weight: bold; margin-bottom: 5px;">原文：[原文]</div>
                <div style="background-color: #E0E0E0; padding: 10px; border-radius: 5px; color: black; margin-bottom: 10px;">羅馬拼音：[拼音]</div>
                
                **💡 相關生詞：**
                * [單字1] ([拼音]) - [中文意思]
                * [單字2] ([拼音]) - [中文意思]
                
                **📝 其他例句：**
                1. [例句1]
                   - 拼音：[例句1拼音]
                2. [例句2]
                   - 拼音：[例句2拼音]
                
                ---
                """
                
                response = model.generate_content(prompt)
                
                if response.text:
                    st.success(f"✅ 翻譯成功！(使用模型: {model_name})")
                    st.markdown(response.text, unsafe_allow_html=True)
                    success = True
                    break # 成功後跳出迴圈
            except Exception:
                continue # 失敗則嘗試下一個模型

        if not success:
            st.error("❌ 目前無法連線至 Google AI。")
            st.info("💡 建議檢查：\n1. 確保已在 Google AI Studio 啟用 Gemini API。\n2. 檢查 API Key 是否正確貼在 Secrets 中。\n3. 若剛申請 Key，請等 5 分鐘後再試。")

st.caption("✨ 每天一小步，讓學習更有趣！")
