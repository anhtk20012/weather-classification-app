import streamlit as st

st.set_page_config(page_title="Weather Classification", page_icon="⛅", layout="centered")

# ======= 1 MÀU DUY NHẤT DÙNG CHO SÁNG + TỐI =======
ACCENT = "#4EA8DE"         # màu xanh dịu, both mode đều đẹp
BG_BOX = "#E5F3FB20"        # nền mờ trong hộp (20 = độ trong suốt 12%)
TEXT_COLOR = "inherit"       # dùng màu chữ tự nhiên của Streamlit

# ======= CSS TỐI ƯU – KHÔNG PHỤ THUỘC THEME =======
st.markdown(f"""
<style>

.big-title {{
    text-align:center;
    font-size: 42px;
    font-weight: 700;
    padding: 10px 0 20px 0;
    color: {ACCENT};
}}

.card {{
    padding: 24px;
    background: {BG_BOX};
    border-radius: 16px;
    border-left: 6px solid {ACCENT};
    box-shadow: 0 4px 10px rgba(0,0,0,0.08);
    margin-left:auto;
    margin-right:auto;
    margin-top:25px;
    max-width: 750px;
    font-size: 18px;
    color: {TEXT_COLOR};
    line-height: 1.6;
}}

.card ul {{
    margin-top:10px;
    padding-left: 20px;
}}

.card li {{
    margin-bottom: 6px;
}}

</style>
""", unsafe_allow_html=True)

# ======= UI HIỂN THỊ =======
st.markdown("<div class='big-title'>⛅ Weather Classification App</div>", unsafe_allow_html=True)

st.markdown(f"""
<div class='card'>
Ứng dụng sử dụng mô hình CNN để phân loại <b>ảnh thời tiết</b> thành 4 nhóm chính:

- ☁️ <b>Cloudy</b>
- 🌧️ <b>Rain</b>
- ☀️ <b>Shine</b>
- 🌅 <b>Sunrise</b>

Bạn có thể sử dụng thanh menu bên trái để truy cập các tính năng:
<ul>
<li>🔮 Predict — Dự đoán ảnh thời tiết</li>
<li>🖼️ Dataset — Xem ảnh mẫu trong dataset</li>
<li>📊 Dashboard — Thống kê mô hình</li>
<li>🎯 Training — Huấn luyện mô hình</li>
</ul>

</div>
""", unsafe_allow_html=True)
st.write("")
st.info("👉 Hãy mở menu bên trái để bắt đầu!")
