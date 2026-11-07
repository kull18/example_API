from fastapi import UploadFile
from io import BytesIO
from PIL import Image, ImageOps

def strip_metadata(image_bytes: bytes, format: str = "JPEG") -> bytes:
    with Image.open(BytesIO(image_bytes)) as img:
        img = ImageOps.exif_transpose(img)

        if format.upper() in ["JPEG", "JPG"] and img.mode in ("RGBA", "P"):
            img = img.convert("RGB")

        clean_img = Image.new(img.mode, img.size)
        clean_img.putdata(list(img.getdata()))

        output = BytesIO()
        clean_img.save(output, format=format)
        return output.getvalue()