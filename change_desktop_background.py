import ctypes
import os
from tkinter import Tk, Entry, Button, Label
from PIL import Image, ImageDraw, ImageFont

def create_image_with_text(text, output_path):
    width, height = 1920, 1080
    background_color = (48, 84, 10)

    image = Image.new('RGB', (width, height), color=background_color)
    draw = ImageDraw.Draw(image)

    font_size = 100
    try:
        font = ImageFont.truetype("arial.ttf", font_size)
    except IOError:
        font = ImageFont.load_default()

    text_bbox = draw.textbbox((0, 0), text, font=font)
    text_width = text_bbox[2] - text_bbox[0]
    text_height = text_bbox[3] - text_bbox[1]
    text_x = (width - text_width) // 2
    text_y = (height - text_height) // 2

    draw.text((text_x, text_y), text, font=font, fill=(255, 255, 255))

    image.save(output_path)

def change_desktop_background(image_path):
    abs_image_path = os.path.abspath(image_path)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, abs_image_path, 3)

def generate_and_set_background():
    text = entry.get()
    output_image_path = r'C:\\Users\\thebl\\Desktop\\desktop_python_stuff\\output_image.jpg'
    create_image_with_text(text, output_image_path)
    change_desktop_background(output_image_path)
    label_result.config(text="Background updated successfully!")

app = Tk()
app.title("Background Text Generator")

label = Label(app, text="Enter your text:")
label.pack()

entry = Entry(app, width=50)
entry.pack()

button = Button(app, text="Set as Background", command=generate_and_set_background)
button.pack()

label_result = Label(app, text="")
label_result.pack()

app.mainloop()
