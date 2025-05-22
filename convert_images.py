import os
import time
from PIL import Image
from psd_tools import PSDImage

ROOT_FOLDER = r"\\20.0.0.172\\تنفيذ اوامر التشغيل طنطا\\2025\\شهر 5"

# الفولدر اللي هيتحفظ فيه الشغل (الصور المحوّلة)
OUTPUT_ROOT = r"\\sv-t.taildd4b8f.ts.net\\التنفيذ\\شهر 5"

SUPPORTED_FORMATS = ['.psd', '.tiff', '.tif']

def convert_psd(input_path, output_path):
    psd = PSDImage.open(input_path)
    composite = psd.composite()
    
    # PIL Image من psd-tools بيرجعها دايمًا RGB، فمع الأسف لازم نحفظها كده
    dpi = composite.info.get("dpi", (300, 300))
    composite.save(output_path, "JPEG", dpi=dpi)


def convert_image(input_path, output_path):
    img = Image.open(input_path)

    # نخلي الصورة زي ما هي (RGB أو CMYK)
    color_mode = img.mode
    dpi = img.info.get("dpi", (300, 300))

    if color_mode in ["RGB", "CMYK"]:
        img.save(output_path, "JPEG", dpi=dpi)
    else:
        # لو الصورة بنظام ألوان مش مدعوم في JPEG، نحولها لـ RGB
        img.convert("RGB").save(output_path, "JPEG", dpi=dpi)


def process_folder():
    for root, dirs, files in os.walk(ROOT_FOLDER):
        for filename in files:
            name, ext = os.path.splitext(filename)
            ext = ext.lower()
            if ext in SUPPORTED_FORMATS:
                input_path = os.path.join(root, filename)
                relative_path = os.path.relpath(root, ROOT_FOLDER)
                output_dir = os.path.join(OUTPUT_ROOT, relative_path)
                os.makedirs(output_dir, exist_ok=True)
                output_path = os.path.join(output_dir, name + ".jpg")

                if not os.path.exists(output_path):
                    try:
                        if ext == '.psd':
                            convert_psd(input_path, output_path)
                        else:
                            convert_image(input_path, output_path)
                        print(f"✅ تم التحويل: {input_path} → {output_path}")
                    except Exception as e:
                        print(f"❌ فشل في تحويل {input_path}: {e}")
                        with open("errors.log", "a", encoding="utf-8") as log:
                            log.write(f"❌ {input_path} - {str(e)}\n")


if __name__ == "__main__":
    while True:
        process_folder()
        time.sleep(60)
