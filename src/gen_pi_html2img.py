from html2image import Html2Image
from PIL import Image
import os
import time

dbg = 0

def gen_code_image(max_count_caracters:int, lines:int, html_file):
    print(f"max:{max_count_caracters},lines:{lines}")
    hti = Html2Image()
    # html_file = 'output.html'
    # img_file = 'output.png'
    img_file = f"{html_file[:-5]}.png"
    new_folder, img_file = os.path.split(img_file)
    print(new_folder, img_file )
    # time.sleep(10)
    hti.output_path = new_folder
    hti.screenshot(html_file=html_file, save_as=img_file, size=(max_count_caracters*8,lines*18))
    # hti.screenshot(html_file=html_file, save_as='output.png', size=(600,400))

    # Open the image with Pillow
    img = Image.open(f"{new_folder}\\{img_file}")

    # Optionally, you can process or display the image
    if dbg>=9:  img.show()

    print(f"Image generated and saved as '{new_folder}\\{img_file}'")
    return f"{new_folder}\\{img_file}"


if __name__ == "__main__":
    gen_code_image(120, 40, 'output.html')