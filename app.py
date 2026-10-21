import streamlit as st
import os
import requests

st.set_page_config(page_title="AI توليد الفيديوهات", layout="wide")
st.title("🎬 منصة توليد الفيديوهات AI المخصصة")

kling_api_key = st.secrets.get("KLING_API_KEY")

with st.sidebar:
    st.header("إعدادات المشروع")
    project_type = st.selectbox("اختر نوع المشروع", ["مشهد كوميدي (أم وابنها)", "مشهد درامي"])

if project_type == "مشهد كوميدي (أم وابنها)":
    character = st.selectbox("اختر الشخصية الرئيسية", ["الأم (شخصية عراقية)", "الابن (شخصية عراقية)"])
    cat_mood = None
else:
    character = None
    cat_mood = st.selectbox("حالة القط", ["مرح", "مشاكس", "حزين"])

st.header("إعدادات التوليد")
model = st.selectbox("اختر النموذج", ["Kling AI", "Luma Dream Machine"])
aspect_ratio = st.selectbox("مقاس الفيديو", ["9:16 (Reels/TikTok)", "16:9 (YouTube)"])
prompt = st.text_area("أدخل الوصف (Prompt) لتوليد المشهد", placeholder="مثال...")

if st.button("توليد الفيديو"):
    if prompt:
        if not kling_api_key:
            st.error("مفتاح الـ Kling AI غير موجود في إعدادات التطبيق.")
        else:
            st.write(f"جاري توليد الفيديو لمشروع {project_type}...")
            
            url = "https://api.klingai.com/v1/videos/text2video"
            headers = {
                "Authorization": f"Bearer {kling_api_key}",
                "Content-Type": "application/json"
            }
            data = {
                "prompt": prompt,
                "aspect_ratio": "9:16" if aspect_ratio.startswith("9:16") else "16:9",
                "model": "kling-v1",
                "mode": "professional"
            }
            
            try:
                response = requests.post(url, headers=headers, json=data)
                if response.status_code == 200:
                    st.success("تم إرسال طلب توليد الفيديو بنجاح!")
                    st.json(response.json())
                else:
                    st.error(f"خطأ في الاتصال: {response.status_code}")
                    st.text(response.text)
            except Exception as e:
                st.error(f"حدث خطأ: {e}")
    else:
        st.warning("يرجى كتابة الوصف أولاً.")
