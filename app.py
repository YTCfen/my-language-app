import streamlit as st
import google.generativeai as genai

# 二、修改網頁標題與名稱
st.set_page_config(page_title="🔎多語練習機 🔊", page_icon="🌍")
st.title("🔎多語練習機 🔊")

# 讀取秘密鑰匙
try:
    API_KEY = st.secrets["MY_API_KEY"]
    genai.configure(api_key=API_KEY.strip())
except:
    st.error("請在 Secrets 設定中配置 MY_API_KEY")

text = st.text_input("輸入中文句子：", "這多少錢？")

if st.button("開始多語轉換"):
    # 這裡改回最穩定的模型名稱
    model = genai.GenerativeModel('gemini-pro')
    
    # 三、要求的 HTML 格式、生詞與例句
    prompt = f"""
    請將『{text}』翻譯成日文、韓文、泰文。
    請嚴格遵守以下格式輸出，不要有任何額外的前言或結語：
    
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
    
    with st.spinner('正在分析生詞與造句...'):
        try:
            response = model.generate_content(prompt)
            # 一、使用 HTML 渲染功能來顯示底色
            st.markdown(response.text, unsafe_allow_html=True)
        except Exception as e:
            # 這裡如果還是 404，程式會自動顯示錯誤細節
            st.error(f"連線失敗：{e}")

st.caption("✨ 每天練習一個句子，同時精通日韓泰！")
