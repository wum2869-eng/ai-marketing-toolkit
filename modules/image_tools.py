from io import BytesIO
from PIL import Image, ImageOps

def process_image(uploaded_file, width: int, height: int) -> BytesIO:
    """Fit an uploaded image into a target canvas while preserving proportions."""
    image = Image.open(uploaded_file).convert("RGB")
    fitted = ImageOps.contain(image, (width, height))
    canvas = Image.new("RGB", (width, height), "white")
    x = (width - fitted.width) // 2
    y = (height - fitted.height) // 2
    canvas.paste(fitted, (x, y))

    output = BytesIO()
    canvas.save(output, format="JPEG", quality=95)
    output.seek(0)
    return output
