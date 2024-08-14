from html2image import Html2Image
from PIL import Image



hti = Html2Image()
html_file = 'output.html'
hti.screenshot(html_file=html_file, save_as='output.png', size=(600,400))

# Open the image with Pillow
img = Image.open('output.png')

# Optionally, you can process or display the image
img.show()

print("Image generated and saved as 'output.png'")
