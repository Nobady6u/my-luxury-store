import streamlit as st

# 1. إعدادات الصفحة والشكل العام
st.set_page_config(page_title="HOME LUXURY | ALI TRENDS", layout="wide", page_icon="👑")

st.markdown("""
    <style>
    .stApp { background-color: #050505; color: white; font-family: 'Arial'; }
    .gold-header { 
        background: linear-gradient(90deg, #D4AF37, #F9E076);
        -webkit-background-clip: text;
        -webkit-text-fill-color: transparent;
        text-align: center; font-size: 45px; font-weight: bold; padding: 20px;
    }
    .product-card {
        background-color: #111; border: 1px solid #333;
        border-radius: 20px; padding: 25px; text-align: center;
        transition: 0.3s;
    }
    .product-card:hover { border-color: #D4AF37; transform: translateY(-5px); }
    .old-price { color: #888; text-decoration: line-through; font-size: 18px; }
    .new-price { color: #D4AF37; font-size: 30px; font-weight: bold; display: block; margin-top: 5px; }
    .stButton>button {
        background-color: #D4AF37; color: black; border-radius: 10px;
        width: 100%; font-weight: bold; border: none; height: 50px;
    }
    </style>
    """, unsafe_allow_html=True)

st.markdown('<p class="gold-header">👑 HOME LUXURY VIP</p>', unsafe_allow_html=True)

# 2. المنتجات (بصور احترافية)
products = [
    {
        "name": "Smart Watch Ultra Premium",
        "img": "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=500",
        "sale": 300.0, "old": 500.0
    },
    {
        "name": "Luxury Audio Soundbar",
        "img": "https://images.unsplash.com/photo-1545454675-3531b543be5d?w=500",
        "sale": 150.0, "old": 350.0
    }
]

cols = st.columns(2)
for i, p in enumerate(products):
    with cols[i]:
        st.markdown(f'''
            <div class="product-card">
                <img src="{p['img']}" width="100%" style="border-radius:15px; margin-bottom:15px;">
                <h3 style="margin-bottom:10px;">{p['name']}</h3>
                <span class="old-price">€{p['old']}</span>
                <span class="new-price">€{p['sale']}</span>
            </div>
        ''', unsafe_allow_html=True)
        st.button(f"أضف للسلة - Buy Now", key=f"btn_{i}")

# 3. عودة الشات بوت في الجانب (Sidebar)
st.sidebar.title("💬 المساعد الذكي (Ali AI)")
if "messages" not in st.session_state:
    st.session_state.messages = []

for message in st.session_state.messages:
    with st.sidebar.chat_message(message["role"]):
        st.markdown(message["content"])

if prompt := st.sidebar.chat_input("كيف يمكنني مساعدتك؟"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.sidebar.chat_message("user"):
        st.markdown(prompt)
    with st.sidebar.chat_message("assistant"):
        response = f"أهلاً بك! نحن نوفر شحن مجاني اليوم على كافة المنتجات."
        st.markdown(response)
        st.session_state.messages.append({"role": "assistant", "content": response})
        
