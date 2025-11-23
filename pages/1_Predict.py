import streamlit as st
from PIL import Image
from utils import load_model, predict

st.set_page_config(page_title="Predict Weather", page_icon="🔮", layout="centered")

ACCENT = "#4EA8DE"
BG_BOX = "#E5F3FB20"
TEXT_COLOR = "inherit"

st.markdown(f"""
<style>

.section-title {{
    font-size: 42px;
    font-weight: 700;
    text-align: center;
    padding: 12px 0;
    color: {ACCENT};
}}

.result-box {{
    padding: 20px;
    background: {BG_BOX};
    border-left: 6px solid {ACCENT};
    border-radius: 12px;
    margin-top: 20px;
    color: {TEXT_COLOR};
    box-shadow: 0 4px 6px rgba(0,0,0,0.08);
}}

.center {{
    text-align: center;
}}

</style>
""", unsafe_allow_html=True)

st.markdown("<div class='section-title'>🔮 Dự đoán thời tiết từ hình ảnh</div>", unsafe_allow_html=True)

model = load_model()

uploaded = st.file_uploader("📤 Tải ảnh thời tiết lên", type=["jpg", "jpeg", "png"])

if uploaded:
    img = Image.open(uploaded)

    st.image(img, caption="Ảnh đã tải", width='stretch')

    st.write("---")
    st.markdown("<h4 class='center'>🔍 Kết quả dự đoán</h4>", unsafe_allow_html=True)

    label, confidence, probs = predict(model, img)

    st.markdown(
        f"""
        <div class='result-box'>
            <h3 style='margin:0;'>🌈 {label}</h3>
            <p><strong>Độ tin cậy:</strong> {confidence*100:.2f}%</p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.write("### 📊 Xác suất từng loại:")
    for name, p in zip(["Cloudy", "Rain", "Shine", "Sunrise"], probs):
        st.write(f"- **{name}**: {p*100:.2f}%")

else:
    st.info("⬆️ Hãy tải ảnh lên để mô hình dự đoán.")
