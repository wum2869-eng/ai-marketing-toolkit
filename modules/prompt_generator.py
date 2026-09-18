def build_prompt(
    subject: str,
    size: str,
    style: str,
    palette: str,
    composition: str,
    extra: str = "",
) -> str:
    subject = subject.strip() or "营销主题"
    size = size.strip() or "1080x1920"
    style = style.strip() or "现代商业视觉"
    palette = palette.strip() or "清爽、高对比"
    composition = composition.strip() or "主体突出、层次清晰"
    extra = extra.strip()

    prompt = (
        f"Create a polished marketing visual for {subject}. "
        f"Canvas size: {size}. "
        f"Visual style: {style}. "
        f"Color palette: {palette}. "
        f"Composition: {composition}. "
        "Clean hierarchy, strong focal point, natural proportions, "
        "sharp details, professional commercial design, no unnecessary text."
    )
    if extra:
        prompt += f" Additional requirements: {extra}"
    return prompt
