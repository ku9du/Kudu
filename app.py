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
prompt = st.text_area("أدخل الوصف (Prompt) لتوليد المشهد", placeholder="مثال: أم عراقية طيبة في الخمسينات من عمرها، ترتدي عباية تقليدية، تجلس في مقهي شعبي عراقي، تبتسم بحماس وتتحدث مع ابنها بخفة دم")

if st.button("توليد الفيديو"):
    if prompt:
        if not kling_api_key:
            st.error("غير موجود في إعدادات التطبيق (Secrets) API مفتاح الـ Kling AI")
        else:
            st.write(f"جاري توليد الفيديو لمشروع {project_type} باستخدام {model}...")
            st.write("ملاحظة: هنا سنضع الكود الخاص بالاتصال بـ API Kling")
    else:
        st.warning("يرجى كتابة الوصف أولاً.")
