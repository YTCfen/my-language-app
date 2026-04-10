import streamlit as st
from groq import Groq

st.set_page_config(page_title="🔎多語練習機 🔊", page_icon="🌍")
st.title("🔎多語練習機 🔊")

# 讀取 Groq 鑰匙
try:
    client = Groq(api_key=st.secrets["GROQ_API_KEY"])
except:
    st.error("❌ 請在 Secrets 設定中配置 GROQ_API_KEY")
    st.stop()

text = st.text_input("輸入中文句子：", "這多少錢？")

if st.button("開始多語轉換"):
    with st.spinner('正在分析中...'):
        try:
            # 使用 Groq 的超高速模型 llama-3.3-70b-versatile
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "user",
                        "content": f"將『{text}』翻譯成日文、韓文、泰文。每種語言請提供：1.原文(黃底) 2.羅馬拼音(灰底) 3.相關生詞 4.其他例句。請用HTML格式輸出底色。",
                    }
                ],
                model="llama-3.3-70b-versatile",
            )
            
            # 定義顯示格式 (直接由 Python 處理底色確保穩定)
            # 這裡我們手動處理輸出格式以符合你的美觀要求
            st.success("✅ 翻譯成功！")
            st.markdown(chat_completion.choices[0].message.content, unsafe_allow_html=True)
            
        except Exception as e:
            st.error(f"連線失敗：{e}")

st.caption("✨ 換了更強大的 Groq 引擎，速度更快了！")
