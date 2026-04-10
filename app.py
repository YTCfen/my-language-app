import streamlit as st
import google.generativeai as genai

st.title("🌍 最終測試版")

# 1. 請再次檢查這裡的 Key 是否正確
API_KEY = "這裡換成你的API_KEY"
genai.configure(api_key=API_KEY)

text = st.text_input("輸入內容：", "你好")

if st.button("點擊測試"):
    # 使用最基礎的模型名稱，不加 models/ 前綴試試
    model = genai.GenerativeModel('gemini-1.5-flash')
    
    st.write("⏳ 正在嘗試與 AI 對話...")
    
    try:
        # 加入 stream=False 確保一次性拿回所有結果，不分段
        response = model.generate_content(text, stream=False)
        
        # 檢查是否有內容回傳
        if response.text:
            st.success("✅ 收到回覆：")
            st.write(response.text)
        else:
            st.warning("⚠️ AI 有回應但內容是空的，可能是安全過濾器攔截了內容。")
            
    except Exception as e:
        st.error(f"❌ 發生錯誤：{e}")
        # 這行會把最底層的錯誤邏輯印出來，幫我們找原因
        st.exception(e)
