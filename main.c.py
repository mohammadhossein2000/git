from tkinter import Tk, filedialog
from PIL import Image
import os

def compress_images(image_paths, destination_path):
    for image_path in image_paths:
        # بارگیری تصویر
        image = Image.open(image_path)
        image_name = os.path.basename(image_path)
        
        # کاهش حجم تصویر
        image.save(destination_path + '/' + image_name, optimize=True)
        
        # محاسبه حجم تصویر قبل و بعد از کاهش
        original_size = os.path.getsize(image_path)
        compressed_size = os.path.getsize(destination_path + '/' + image_name)
        compression_ratio = (1 - compressed_size / original_size) * 100
        
        print(f'تصویر {image_name} کاهش حجم یافت. نسبت فشرده‌سازی: {compression_ratio:.2f}%')

def select_images():
    root = Tk()
    root.withdraw()
    
    # دریافت آدرس دلخواه از کاربر
    destination_path = filedialog.askdirectory(title='انتخاب مسیر ذخیره فایل ها')
    
    # دریافت فایل‌های تصویر
    image_paths = filedialog.askopenfilenames(title='انتخاب تصاویر', filetypes=[('تصاویر', '*.png;*.jpg;*.jpeg;*.gif')])
    
    # نمایش تصاویر و اجازه انتخاب از کاربر
    for image_path in image_paths:
        image = Image.open(image_path)
        image.show()
    
    # کاهش حجم تصاویر و ذخیره آن‌ها در مسیر دلخواه
    compress_images(image_paths, destination_path)

select_images()
