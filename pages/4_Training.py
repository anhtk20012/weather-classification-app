import streamlit as st

st.set_page_config(page_title="Training", page_icon="🎯", layout="wide")

st.markdown("<h2 style='color:#43A047'>🎯 Training / Fine-tuning Model</h2>", unsafe_allow_html=True)

st.markdown("""
<div style='padding:20px; background:#E8F5E9; border-radius:12px; border-left:5px solid #43A047'>
💡 Đây là bản demo huấn luyện. Bạn có thể mở rộng để chạy train thực tế.
</div>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)

with col1:
    epochs = st.slider("Số epoch", 1, 20, 5)
    lr = st.number_input("Learning Rate", value=0.001)

with col2:
    batch = st.number_input("Batch Size", value=32)
    optim = st.selectbox("Optimizer", ["Adam", "SGD", "RMSProp"])

if st.button("🚀 Bắt đầu Train"):
    st.write("Đang huấn luyện...")
    progress = st.progress(0)
    for i in range(epochs):
        progress.progress((i+1)/epochs)
        st.write(f"Epoch {i+1}/{epochs} ✔️")
    st.success("🎉 Hoàn thành train (demo)")
