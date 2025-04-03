import tkinter

import requests
from tkinter import *
from PIL import Image, ImageTk
import io
from pathlib import Path

bg_color = 'white'

#functions
def get_fox_image():
    global fox_image
    global fox_url
    response = requests.get('https://randomfox.ca/floof/')

    if response.status_code == 200:#ok
        #gettig image url
        fox = response.json()
        fox_url = fox['image']
        #downloading image
        img_response = requests.get(fox_url)
        img_data = img_response.content #binary
        #converting image to PhotoImage object
        image = Image.open(io.BytesIO(img_data))
        #image = image.resize((500, 500))
        fox_image = ImageTk.PhotoImage(image)
        canvas.itemconfig(fox_canvas, image=fox_image)
    else:
        print("An error has occured while fetching photo.")


def save_image():
    try:
        save_img_data = requests.get(fox_url).content
    except NameError:
        print('Geneate image first!')
        return
    number = 1
    path_to_file = Path(f'saved_photos/fox{number}.jpg')
    while path_to_file.is_file():
        print(f"fox{number}.jpg exists")
        number += 1
        path_to_file = Path(f'saved_photos/fox{number}.jpg')

    with open(path_to_file, 'wb') as save:
        save.write(save_img_data)

def change_motive():
    global bg_color
    if bg_color == 'white':
        bg_color = 'black'
        btn_text.set('White mode')
    else:
        bg_color = 'white'
        btn_text.set('Dark mode')

    canvas.configure(bg=bg_color)
    window.configure(bg=bg_color)

#window and Canvas
window = Tk()
window.config(width=900, height=900)
canvas = Canvas(width=700, height=700, highlightthickness=0)
fox_canvas = canvas.create_image(350, 350, image=None)


#----------BUTTONS----------

new_fox = Button(text='Generate new Fox', command=get_fox_image)
save_fox = Button(text='Save Fox', command=save_image)
btn_text = tkinter.StringVar(window, 'Dark Mode')
change_motive = Button(textvariable=btn_text, command=change_motive)
btn_text.set('Dark mode')

#-------------UI------------

canvas.grid(row=0, column=0, columnspan=2)
new_fox.grid(row=1, column=0)
save_fox.grid(row=1, column=1)
change_motive.grid(row=2, column=0, columnspan=2)

window.mainloop()

