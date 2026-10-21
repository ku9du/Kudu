import streamlit as st
import os
import requests

st.set_page_config(page_title="AI منصة توليد الفيديوهات", layout="wide")
st.title("📹 المخصصة AI منصة توليد الفيديوهات")

kling_api_key = st.secrets.get("KLING_API_KEY")

with st.sidebar:
    st.header("إعدادات المشروع")
    project_type = st.selectbox("نوع المشروع", ["إسكتش كوميدي (أم وابنها)"])

    if project_type == "إسكتش كوميدي (أم وابنها)":
        character = st.selectbox("اختر الشخصية الرئيسية", ["الأم (شخصية عراقية)", "الابن (شخصية عراقية)"])
    if project_type == "إسكتش كوميدي (أم وابنها)":
        cat_mood = None
    else:
        cat_mood = st.selectbox("حالة القط", ["حزين", "مشاكس", "مرح"])

st.header("إعدادات التوليد")
model = st.selectbox("اختر النموذج", ["Kling AI", "Luma Dream Machine"])
aspect_ratio = st.selectbox("مقاس الفيديو", ["9:16 (Reels/TikTok)", "16:9 (YouTube)"])

prompt = st.text_area("لتوليد المشهد (Prompt) أدخل الوصف", placeholder="أم عراقية طيبة في الخمسينات من عمرها، ترتدي عباية تقليدية، تجلس في مقهي شعبي عراقي، تبتسم بحماس وتتحدث مع ابنها بخفة دم.")

if st.button("توليد الفيديو"):
    if prompt:
        if not kling_api_key:
            st.error("مفتاح الـ API الخاص بـ Kling AI غير موجود في إعدادات التطبيق (Secrets).")
        else:
            st.write(f"جاري توليد الفيديو لمشروع {project_type} باستخدام {model}...")
            # هنا ستضع الكود الخاص بالاتصال بـ API Kling
    else:
        st.warning("يرجى كتابة الوصف أولاً.")

