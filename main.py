import tkinter
from tkinter import *

from utils import Utils

utils = Utils()

#window and Canvas
window = Tk()
window.config(width=900, height=900)
canvas = Canvas(width=700, height=700, highlightthickness=0)
fox_canvas = canvas.create_image(350, 350, image=None)


#----------BUTTONS----------

new_fox = Button(text='Generate new Fox', command=lambda: utils.get_fox_image(canvas, fox_canvas))
save_fox = Button(text='Save Fox', command=lambda: utils.save_image())
btn_text = tkinter.StringVar(window, 'Dark Mode')
change_motive = Button(textvariable=btn_text, command=lambda: utils.change_motive(btn_text, canvas, window))
btn_text.set('Dark mode')

#-------------UI------------

canvas.grid(row=0, column=0, columnspan=2)
new_fox.grid(row=1, column=0, padx=10, pady=10, sticky='NSEW')
save_fox.grid(row=1, column=1, padx=10, pady=10, sticky='NSEW')
change_motive.grid(row=2, column=0, columnspan=2, padx=10, pady=10, sticky='NSEW')

window.mainloop()

