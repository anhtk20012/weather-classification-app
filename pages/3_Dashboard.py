import streamlit as st
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from pathlib import Path
import plotly.express as px

st.set_page_config(page_title="Dashboard", page_icon="📊", layout="centered")

# ===== STYLE =====
ACCENT = "#4EA8DE"
BG_BOX = "#E5F3FB20"
TEXT_COLOR = "inherit"

st.markdown(f"""
<style>
.section-title {{
    font-size: 42px;
    font-weight: 700;
    text-align: center;
    padding: 20px 0;
    color: {ACCENT};
}}

.card {{
    background: {BG_BOX};
    padding: 18px;
    border-left: 6px solid {ACCENT};
    border-radius: 12px;
    box-shadow: 0px 4px 12px rgba(0,0,0,0.08);
    text-align: center;
    font-size:18px;
    color: {TEXT_COLOR};
}}
</style>
""", unsafe_allow_html=True)

# ===== TITLE =====
st.markdown("<div class='section-title'>📊 Weather Model Dashboard</div>", unsafe_allow_html=True)

# ===== READ DATA FROM REAL FOLDER =====
BASE_DIR = Path(__file__).parent.parent / "assets" / "Multi-class Weather Dataset"

# Lấy tất cả subfolder làm label
CLASSES = sorted([f.name for f in BASE_DIR.iterdir() if f.is_dir()])

# Đếm số ảnh trong từng class
class_counts = []
for cls in CLASSES:
    image_files = list((BASE_DIR / cls).glob("*.jpg"))
    class_counts.append(len(image_files))

# Tạo dataframe thật
df = pd.DataFrame({
    "label": CLASSES,
    "count": class_counts
})

# ===== SUMMARY CARDS =====
cols = st.columns(len(df))

for col, row in zip(cols, df.itertuples()):
    with col:
        st.markdown(
            f"""
            <div class='card'>
                <h3>{row.label}</h3>
                <p style='font-size: 26px; font-weight: 600;'>{row.count} ảnh</p>
            </div>
            """,
            unsafe_allow_html=True
        )

st.write("---")

# ===== DATASET SUMMARY =====
st.write("### 📦 Dataset Summary")

total_images = df["count"].sum()
max_class = df.loc[df["count"].idxmax()]
min_class = df.loc[df["count"].idxmin()]
balance_score = round(df["count"].std(), 2)

colA, colB, colC, colD = st.columns(4)

colA.metric("Tổng số ảnh", total_images)
colB.metric("Số class", len(df))
colC.metric("Class lớn nhất", f"{max_class.label}")
colD.metric("Class nhỏ nhất", f"{min_class.label}")
st.write(f"**Chỉ số cân bằng dataset (độ lệch chuẩn số ảnh giữa các class):** {balance_score}")
st.write("---")

# ===== CHARTS =====
st.subheader("📊 Phân bố số lượng ảnh trong Dataset")

# ----- PIE / DONUT -----
fig_pie = px.pie(
    df,
    names="label",
    values="count",
    title="Class Distribution (Pie Chart)",
    color="label",
    hole=0.45,  # tạo donut chart
    color_discrete_sequence=px.colors.qualitative.Set2
)
fig_pie.update_traces(
    textposition="inside", 
    textinfo="percent+label",
    hovertemplate="%{label}: %{value} ảnh (%{percent})<extra></extra>"  
)

st.plotly_chart(fig_pie, config={"responsive": True})

# ----- BAR CHART -----
fig_bar = px.bar(
    df,
    x="label",
    y="count",
    text="count",
    title="Number of Images per Class",
    color="label",
    color_discrete_sequence=px.colors.qualitative.Set2
)
fig_bar.update_traces(
    textposition="outside",
    hovertemplate="%{x}: %{y} ảnh<extra></extra>"
)
fig_bar.update_layout(yaxis_title="Images Count")
st.plotly_chart(fig_bar, config={"responsive": True})

