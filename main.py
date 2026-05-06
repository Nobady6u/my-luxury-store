import streamlit as st
import random
import time

# 1. إعدادات المتجر الأساسية
st.set_page_config(page_title="LUXURY TRENDS | علي إكسبريس", layout="wide", page_icon="🔥")

# 2. تصميم الواجهة (CSS الفاخر)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Cairo:wght@400;700&display=swap');
    html, body, [class*="css"] { font-family: 'Cairo', sans-serif; text-align: right; }
    .stApp { background-color: #0b0d11; color: white; }
    .gold-text { color: #D4AF37; font-weight: bold; }
    .header-box { text-align: center; padding: 30px; background: linear-gradient(180deg, #161b22 0%, #0b0d11 100%); border-bottom: 1px solid #D4AF37; margin-bottom: 25px; }
    .product-card { background-color: #161b22; border-radius: 20px; padding: 20px; border: 1px solid #30363d; transition: 0.4s; text-align: center; }
    .product-card:hover { border-color: #D4AF37; transform: translateY(-10px); box-shadow: 0 10px 20px rgba(212, 175, 55, 0.1); }
    .price-tag { font-size: 24px; color: #D4AF37; font-weight: bold; margin: 10px 0; }
    .old-price { color: #8b949e; text-decoration: line-through; font-size: 16px; margin-left: 10px; }
    .stButton>button { background: linear-gradient(90deg, #D4AF37, #f1d279); color: black; border-radius: 12px; font-weight: bold; width: 100%; border: none; height: 45px; }
    </style>
    """, unsafe_allow_html=True)

# 3. محاكي جلب المنتجات من علي إكسبريس (تلقائي)
def get_trending_products():
    # هنا نضع روابط صور حقيقية ومستقرة لمنتجات ترند
    items = [
        {"name": "ساعة Ultra الذكية - إصدار 2026", "img": "https://images.unsplash.com/photo-1544006659-f0b21f04cb1d?w=500", "price": 300, "old": 500},
        {"name": "سماعات Pro عازلة للضوضاء", "img": "https://images.unsplash.com/photo-1505740420928-5e560c06d30e?w=500", "price": 150, "old": 350},
        {"name": "ماكينة قهوة احترافية - ترند", "img": "https://images.unsplash.com/photo-1517668808822-9ebb02f2a0e6?w=500", "price": 450, "old": 700},
        {"name": "نظارات ذكية بلس - إصدار محدود", "img": "https://images.unsplash.com/photo-1572635196237-14b3f281503f?w=500", "price": 200, "old": 400}
    ]
    random.shuffle(items) # لضمان التجديد البصري في كل تحديث
    return items

# هيدر الموقع
st.markdown('<div class="header-box"><h1 style="color:#D4AF37;">👑 LUXURY ALI TRENDS</h1><p>منتجات علي إكسبريس الأكثر مبيعاً - تُحدث تلقائياً</p></div>', unsafe_allow_html=True)

# عرض المنتجات
products = get_trending_products()
cols = st.columns(2)

for idx, item in enumerate(products):
    with cols[idx % 2]:
        st.markdown(f"""
            <div class="product-card">
                <img src="{item['img']}" style="width:100%; border-radius:15px; height:200px; object-fit:cover;">
                <h3 style="margin-top:15px; font-size:18px;">{item['name']}</h3>
                <p class="price-tag">€{item['price']} <span class="old-price">€{item['old']}</span></p>
                <p style="color:#3fb950; font-size:14px;">🔥 خصم لفترة محدودة</p>
            </div>
        """, unsafe_allow_html=True)
        if st.button(f"أضف للسلة - شراء", key=f"buy_{idx}"):
            st.success("تمت الإضافة! سنحولك للدفع...")

# 4. الشات بوت المطور (Ali AI)
st.sidebar.markdown('<h2 style="color:#D4AF37; text-align:center;">💬 Ali AI Assistant</h2>', unsafe_allow_html=True)
st.sidebar.info("مرحباً رامي! أنا مساعدك الذكي، اسألني عن الشحن أو الأسعار.")

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# عرض المحادثة
for msg in st.session_state.chat_history:
    with st.sidebar.chat_message(msg["role"]):
        st.markdown(msg["content"])

# استقبال الرسائل
if user_input := st.sidebar.chat_input("بشو بقدر أساعدك؟"):
    st.session_state.chat_history.append({"role": "user", "content": user_input})
    with st.sidebar.chat_message("user"):
        st.markdown(user_input)

    with st.sidebar.chat_message("assistant"):
        # ذكاء اصطناعي بسيط بناءً على الكلمات
        input_lower = user_input.lower()
        if any(word in input_lower for word in ["سعر", "بكم", "رخيص"]):
            reply = "أسعارنا منافسة جداً لأننا نجلبها من المصنع مباشرة، تبدأ من 150 يورو."
        elif any(word in input_lower for word in ["شحن", "توصيل", "وقت"]):
            reply = "الشحن حالياً مجاني لكل أوروبا! التوصيل بياخد من 3 لـ 5 أيام عمل."
        elif any(word in input_lower for word in ["جودة", "أصلي"]):
            reply = "جميع منتجاتنا المختارة هي 'Top Rated' من علي إكسبريس ومضمونة 100%."
        else:
            reply = f"سؤال جميل بخصوص '{user_input}'! كخبير في الترندات، بنصحك تستغل الخصم الحالي قبل انتهاء الـ 10 دقائق."
        
        st.markdown(reply)
        st.session_state.chat_history.append({"role": "assistant", "content": reply})

# التحديث التلقائي كل 10 دقائق (600 ثانية)
time.sleep(1) # تأخير بسيط لراحة المتصفح
st.caption("🔄
