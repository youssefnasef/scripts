import os
import threading
import time
from tkinter import Tk, Label, Text, Scrollbar, RIGHT, Y, END, BOTH, Frame
from tkinter.ttk import Progressbar
from PIL import Image
from psd_tools import PSDImage
from concurrent.futures import ThreadPoolExecutor

Image.MAX_IMAGE_PIXELS = None
SUPPORTED_FORMATS = ['.psd', '.tiff', '.tif', '.png']

ROOT_FOLDER = r"\\20.0.0.172\\تنفيذ اوامر التشغيل طنطا\\2025\\شهر 5"

# الفولدر اللي هيتحفظ فيه الشغل (الصور المحوّلة)
OUTPUT_ROOT = r"\\20.0.0.172\\التنفيذ\\شهر 5"

class AutoImageConverter:
    def __init__(self, root):
        self.root = root
        self.root.title("تحويل الصور التلقائي")
        self.root.geometry("800x500")

        font = ("Segoe UI", 12)
        log_font = ("Segoe UI", 11)

        self.progress_label = Label(root, text="التقدم: 0/0", font=font)
        self.progress_label.pack(pady=5)
        self.progressbar = Progressbar(root, orient="horizontal", length=700, mode='determinate')
        self.progressbar.pack(pady=10)

        self.log_text = Text(root, wrap='word', font=log_font, height=20)
        self.scrollbar = Scrollbar(root, command=self.log_text.yview)
        self.log_text.configure(yscrollcommand=self.scrollbar.set)
        self.scrollbar.pack(side=RIGHT, fill=Y)
        self.log_text.pack(expand=True, fill=BOTH, padx=10, pady=10)

        self.is_converting = False

        # بدء التحويل تلقائياً
        thread = threading.Thread(target=self.loop_process_folder)
        thread.daemon = True
        thread.start()

    def loop_process_folder(self):
        while True:
            self.log("🔍 جاري فحص المجلدات...")
            self.progressbar['value'] = 0
            image_tasks = []

            for root_dir, _, files in os.walk(ROOT_FOLDER):
                for filename in files:
                    name, ext = os.path.splitext(filename)
                    ext = ext.lower()
                    if ext in SUPPORTED_FORMATS:
                        input_path = os.path.join(root_dir, filename)
                        relative_path = os.path.relpath(root_dir, ROOT_FOLDER)
                        output_dir = os.path.join(OUTPUT_ROOT, relative_path)
                        os.makedirs(output_dir, exist_ok=True)
                        output_path = os.path.join(output_dir, name + ".jpg")

                        if not os.path.exists(output_path) or os.path.getmtime(input_path) > os.path.getmtime(output_path):
                            image_tasks.append((input_path, output_path, ext))

            total_tasks = len(image_tasks)
            self.progressbar['maximum'] = total_tasks
            self.progress_label.config(text=f"تم العثور على {total_tasks} ملف للتحويل.")
            self.log(f"💡 تم العثور على {total_tasks} ملف للتحويل.")

            completed = 0
            if total_tasks > 0:
                with ThreadPoolExecutor(max_workers=3) as executor:
                    futures = [executor.submit(self.process_image, *task) for task in image_tasks]
                    for future in futures:
                        future.result()
                        completed += 1
                        self.progressbar['value'] = completed
                        self.progress_label.config(text=f"التقدم: {completed}/{total_tasks}")
            else:
                self.log("✅ لا توجد ملفات جديدة.")

            self.log("🕐 جاري الانتظار 60 ثانية لإعادة الفحص...")
            time.sleep(60)

    def process_image(self, input_path, output_path, ext):
        try:
            filename = os.path.basename(input_path)
            self.log(f"🚀 جاري معالجة: {filename}")
            if ext == '.psd':
                self.convert_psd(input_path, output_path)
            elif ext == '.png':
                self.convert_png(input_path, output_path)
            else:
                self.convert_image(input_path, output_path)
            self.log(f"✅ تم التحويل: {filename}")
        except Exception as e:
            self.log(f"❌ خطأ في الملف {input_path}: {e}")

    def convert_psd(self, input_path, output_path):
        psd = PSDImage.open(input_path)
        composite = psd.composite()
        if composite.mode not in ("RGB", "CMYK"):
            composite = composite.convert("RGB")
        dpi = composite.info.get("dpi", (300, 300))
        composite.save(output_path, "JPEG", dpi=dpi, quality=90)

    def convert_png(self, input_path, output_path):
        img = Image.open(input_path)
        if img.mode == 'RGBA':
            background = Image.new('RGB', img.size, (255, 255, 255))
            background.paste(img, mask=img.split()[3])
            img = background
        elif img.mode not in ("RGB", "CMYK"):
            img = img.convert("RGB")
        dpi = img.info.get("dpi", (300, 300))
        img.save(output_path, "JPEG", dpi=dpi, quality=90)

    def convert_image(self, input_path, output_path):
        img = Image.open(input_path)
        if img.mode not in ("RGB", "CMYK"):
            img = img.convert("RGB")
        dpi = img.info.get("dpi", (300, 300))
        img.save(output_path, "JPEG", dpi=dpi, quality=90)

    def log(self, msg):
        self.log_text.insert(END, msg + "\n")
        self.log_text.see(END)

if __name__ == "__main__":
    root = Tk()
    app = AutoImageConverter(root)
    root.mainloop()
