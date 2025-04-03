import requests
from tkinter import *
from PIL import Image, ImageTk
import io

from PIL.ImageOps import expand


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
        image = image.resize((500, 500))
        fox_image = ImageTk.PhotoImage(image)
        canvas.itemconfig(fox_canvas, image=fox_image)
    else:
        print("An error has occured while fetching photo.")


def save_image():
    save_img_data = requests.get(fox_url).content
    with open('saved_photos/fox.jpg', 'wb') as save:
        save.write(save_img_data)

#window
window = Tk()
window.config(width=900, height=900, padx=30, pady=30, bg='black')
canvas = Canvas(width=700, height=700, bg='black', highlightthickness=0)

fox_canvas = canvas.create_image(350, 350, image=None)
canvas.grid(row=0, column=0)

new_fox = Button(text='Generate new Fox', command=get_fox_image)
new_fox.grid(row=1, column=0)
save_fox = Button(text='Save Fox', command=save_image)
save_fox.grid(row=2, column=0)

window.mainloop()

