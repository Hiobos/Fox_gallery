import requests
from pathlib import Path
from PIL import Image, ImageTk
import io


class Utils:
    def __init__(self):
        self.bg_color = ['white', 'black']
        self.clr = self.bg_color[0]
        self.fox_image = None

    def change_motive(self, btn_text, canvas, window):
        if self.clr == self.bg_color[0]:
            self.clr = self.bg_color[1]
            btn_text.set('White mode')
        else:
            self.clr  = self.bg_color[0]
            btn_text.set('Dark mode')

        canvas.configure(bg=self.clr)
        window.configure(bg=self.clr)

    def get_fox_image(self, canvas, fox_canvas):
        global fox_url
        response = requests.get('https://randomfox.ca/floof/')

        if response.status_code == 200:  # ok
            # gettig image url
            fox = response.json()
            fox_url = fox['image']
            # downloading image
            img_response = requests.get(fox_url)
            img_data = img_response.content  # binary
            # converting image to PhotoImage object
            image = Image.open(io.BytesIO(img_data))

            max_size = (800, 700)
            image.thumbnail(max_size)

            self.fox_image = ImageTk.PhotoImage(image)
            canvas.itemconfig(fox_canvas, image=self.fox_image)
        else:
            print("An error has occured while fetching photo.")

    def save_image(self):
        try:
            save_img_data = requests.get(fox_url).content
        except NameError:
            print('Generate image first!')
            return
        number = 1
        path_to_file = Path(f'saved_photos/fox{number}.jpg')
        while path_to_file.is_file():
            number += 1
            path_to_file = Path(f'saved_photos/fox{number}.jpg')

        with open(path_to_file, 'wb') as save:
            save.write(save_img_data)