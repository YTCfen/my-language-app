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
            chat_completion = client.chat.completions.create(
                messages=[
                    {
                        "role": "system",
                        "content": "你是一個專業的語言學習專家，負責將中文句子翻譯為日、韓、泰文。你必須全程使用「繁體中文(Taiwan)」進行說明與翻譯，絕對禁止使用簡體中文。"
                    },
                    {
                        "role": "user",
                        "content": f"請將『{text}』翻譯成日文、韓文、泰文。依照指定的 HTML 格式與繁體中文輸出相關生詞與例句。"
                    }
                ],
                model="llama-3.3-70b-versatile",
                temperature=0.3,
            )
            
            st.success("✅ 翻譯成功（已強制繁體化）！")
            # 關鍵修正點：choices[0]
            st.markdown(chat_completion.choices[0].message.content, unsafe_allow_html=True)
            
        except Exception as e:
            st.error(f"連線失敗：{e}")
