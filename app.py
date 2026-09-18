import streamlit as st

from modules.copywriter import CopyRequest, generate_copy
from modules.prompt_generator import build_prompt
from modules.image_tools import process_image

st.set_page_config(page_title="AI Marketing Toolkit", page_icon="✦", layout="wide")

st.title("AI Marketing Toolkit")
st.caption("Open-source starter toolkit for marketing copy, AI image prompts, and image preparation.")

tab1, tab2, tab3 = st.tabs(["文案助手", "Prompt 生成器", "图片尺寸处理"])

with tab1:
    st.subheader("营销文案助手")
    product = st.text_input("产品 / 品牌", "你的产品")
    scene = st.text_input("使用场景", "小红书封面")
    audience = st.text_input("目标人群", "目标用户")
    goal = st.text_input("目标", "种草")
    tone = st.selectbox("语气", ["清晰、有吸引力", "专业可信", "年轻活泼", "简洁高级"])

    if st.button("生成文案", type="primary"):
        result = generate_copy(CopyRequest(product, scene, audience, goal, tone))
        st.markdown(f"### {result['title']}")
        st.write(result["subtitle"])
        st.text(result["body"])

with tab2:
    st.subheader("AI 图片 Prompt")
    subject = st.text_input("画面主题", "夏日女性生活方式")
    size = st.selectbox("尺寸", ["1080x1920", "1242x1660", "1080x1080", "1920x1080"])
    style = st.text_input("视觉风格", "流行杂志封面")
    palette = st.text_input("色彩", "天空蓝、花朵粉、牛仔蓝、温暖金色阳光")
    composition = st.text_input("构图", "人物自然、主体突出、留出标题空间")
    extra = st.text_area("其他要求", "画面干净，细节清晰，避免杂乱元素")

    if st.button("生成 Prompt", type="primary"):
        st.code(build_prompt(subject, size, style, palette, composition, extra), language="text")

with tab3:
    st.subheader("图片尺寸处理")
    uploaded = st.file_uploader("上传图片", type=["png", "jpg", "jpeg", "webp"])
    col1, col2 = st.columns(2)
    with col1:
        width = st.number_input("目标宽度", min_value=100, max_value=5000, value=1080, step=10)
    with col2:
        height = st.number_input("目标高度", min_value=100, max_value=5000, value=1920, step=10)

    if uploaded and st.button("处理并下载", type="primary"):
        result = process_image(uploaded, int(width), int(height))
        st.image(result, caption=f"{width} × {height}", use_container_width=True)
        st.download_button(
            "下载 JPG",
            data=result,
            file_name=f"marketing_{width}x{height}.jpg",
            mime="image/jpeg",
        )
