from PIL import Image, ImageDraw, ImageFont

def gen_code_image_windows():

    # Define the size of the window
    # width, height = 600, 400
    width, height = 1000, 800

    # Create a new image with a white background
    # image = Image.new("RGB", (width, height), "white")
    image = Image.new("RGB", (width, height), color= (31, 31, 31))
    draw = ImageDraw.Draw(image)

    # Draw the macOS style window
    # Draw the title bar
    title_bar_height = 40
    # draw.rectangle([0, 0, width, title_bar_height], fill="#e8e8e8")
    draw.rectangle([0, 0, width, title_bar_height], fill="#313131")

    # Draw the three circles (close, minimize, maximize)
    circle_radius = 8
    circle_y = title_bar_height // 2
    padding = 10

    # Close button (red)
    draw.ellipse([padding, circle_y - circle_radius, padding + 2 * circle_radius, circle_y + circle_radius], fill="#ff5f57")

    # Minimize button (yellow)
    draw.ellipse([padding + 3 * circle_radius, circle_y - circle_radius, padding + 5 * circle_radius, circle_y + circle_radius], fill="#ffbd2e")

    # Maximize button (green)
    draw.ellipse([padding + 6 * circle_radius, circle_y - circle_radius, padding + 8 * circle_radius, circle_y + circle_radius], fill="#28c940")

    # Add some text to the title bar (optional)
    title = "My macOS Style Window"
    font = ImageFont.load_default()
    # text_width, text_height = draw.textlength(title, font=font)
    text_width  = draw.textlength(title, font=font)
    text_x = (width - text_width) // 2
    # text_y = (title_bar_height - text_height) // 2
    text_y = (title_bar_height - 1 ) // 2
    # draw.text((text_x, text_y), title, fill="black", font=font)

    # Add content to the window (optional)
    content = "Hello, World!"
    content_x = padding
    content_y = title_bar_height + padding
    draw.text((content_x, content_y), content, fill="black", font=font)

    # Save the image
    image.save("mac_window_style.png")

    im1 = Image.open('mac_window_style.png')
    im2 = Image.open('output.png')
    im1.paste(im2)
    im1.save('pillow_paste.png', quality=95)

    im1.show()

    # Optionally, display the image
    # image.show()

    print("macOS style window image generated and saved as 'mac_window_style.png'")