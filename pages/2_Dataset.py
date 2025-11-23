import streamlit as st
from pathlib import Path

st.set_page_config(page_title="Dataset", page_icon="🖼️", layout="centered")

ACCENT = "#4EA8DE"
TEXT_COLOR = "inherit"

st.markdown(f"""
<style>

.section-title {{
    font-size: 42px;
    font-weight: 700;
    text-align: center;
    padding: 12px 0 20px 0;
    color: {ACCENT};
}}

.class-title {{
    font-size: 26px;
    font-weight: 700;
    margin-top: 25px;
    color: {TEXT_COLOR};
}}

</style>
""", unsafe_allow_html=True)

st.markdown("<div class='section-title'>🖼️ Dataset Viewer</div>", unsafe_allow_html=True)

BASE_DIR = Path(__file__).parent.parent / "assets" / "Multi-class Weather Dataset"

CLASSES = ["Cloudy", "Rain", "Shine", "Sunrise"]
ICONS = {
    "Cloudy": "☁️",
    "Rain": "🌧️",
    "Shine": "☀️",
    "Sunrise": "🌅"
}

for cls in CLASSES:
    st.markdown(
        f"<div class='class-title'>{ICONS[cls]} {cls}</div>",
        unsafe_allow_html=True
    )

    folder_path = BASE_DIR / cls
    imgs = list(folder_path.glob("*.jpg"))[:8]

    cols = st.columns(4)

    for idx, img_path in enumerate(imgs):
        with cols[idx % 4]:
            st.image(img_path, width='stretch')