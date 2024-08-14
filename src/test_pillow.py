from html2image import Html2Image
from PIL import Image

# Initialize Html2Image
hti = Html2Image()

# Path to the HTML file
html_file = 'output.html'

# Generate the image from the HTML file
hti.screenshot(html_file=html_file, save_as='output.png')

# Open the image with Pillow
img = Image.open('output.png')

# Optionally, you can process or display the image
img.show()

print("Image generated and saved as 'output.png'")
