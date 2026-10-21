import streamlit as st

st.set_page_config(page_title="منصة توليد الفيديوهات AI", layout="wide")

st.title("🎥 منصة توليد الفيديوهات AI المخصصة")

with st.sidebar:
    st.header("إعدادات المشروع")
    project_type = st.selectbox("نوع المشروع:", ["إسكتش كوميدي (أم وابنها)", "أنيميشن قطط ثلاثي الأبعاد"])
    
    if project_type == "إسكتش كوميدي (أم وابنها)":
        character = st.selectbox("اختر الشخصية الرئيسية:", ["الأم (شخصية عراقية)", "الابن (شخصية عراقية)"])
    else:
        cat_mood = st.selectbox("حالة القط:", ["مرح", "مشاكس", "حزين"])

    st.header("إعدادات التوليد")
    model = st.selectbox("اختر النموذج:", ["Kling AI", "Luma Dream Machine"])
    aspect_ratio = st.selectbox("مقاس الفيديو:", ["9:16 (Reels/TikTok)", "16:9 (YouTube)"])

prompt = st.text_area("أدخل الوصف (Prompt) لتوليد المشهد:", placeholder="مثال: الشخصية تتحدث بحماس وتبتسم في مقهى عراقي...")

if st.button("توليد الفيديو"):
    if prompt:
        st.write(f"جاري توليد الفيديو لمشروع '{project_type}' باستخدام {model}...")
    else:
        st.warning("يرجى كتابة الوصف أولاً.")
