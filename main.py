import streamlit as st

# 1. إعدادات المتجر الفاخر
st.set_page_config(page_title="HOME LUXURY | ALI TRENDS", layout="wide")

st.markdown("""
    <style>
    .stApp { background-color: #0E1117; color: white; }
    .gold-header { color: #D4AF37; text-align: center; font-size: 35px; font-weight: bold; }
    .product-card {
        background-color: #1A1C23; border: 1px solid #D4AF37;
        border-radius: 15px; padding: 20px; text-align: center;
    }
    .old-price { color: #ff4b4b; text-decoration: line-through; font-size: 18px; margin-right: 10px; }
    .new-price { color: #D4AF37; font-size: 28px; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="gold-header">👑 HOME LUXURY - ALI TRENDS</p>', unsafe_allow_html=True)

# 2. المنتجات (السعر الفعلي 300 يورو والمشطوب 500 يورو)
products = [
    {
        "name": "Luxury Smart Watch - AliExpress Trend",
        "img": "https://ae01.alicdn.com/kf/S8f98c8c6d36e4f9b8c8c6d36e4f9b8c8W.jpg",
        "sale": 300.0,
        "old": 500.0
    },
    {
        "name": "Premium Audio System - AliExpress Trend",
        "img": "https://ae01.alicdn.com/kf/H21e330f8d9b54c86b86e74f762310116O.jpg",
        "sale": 150.0,
        "old": 350.0
    }
]

cols = st.columns(2)
for i, p in enumerate(products):
    with cols[i]:
        st.markdown(f'''
            <div class="product-card">
                <img src="{p['img']}" width="100%" style="border-radius:10px;">
                <h3 style="color:white; font-size:20px; margin-top:15px;">{p['name']}</h3>
                <p>
                    <span class="old-price">€{p['old']}</span>
                    <span class="new-price">€{p['sale']}</span>
                </p>
                <div style="background:#D4AF37; color:black; font-weight:bold; padding:8px; border-radius:5px; font-size:14px;">AI PICKED: TRENDING 🔥</div>
            </div>
        ''', unsafe_allow_html=True)
        if st.button(f"أضف للسلة", key=f"btn_{i}"):
            st.toast("تمت الإضافة بنجاح!")

st.write("---")
st.info("🤖 يتم الآن تحديث المنتجات ترند من علي إكسبريس تلقائياً...")
