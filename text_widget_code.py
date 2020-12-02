from tkinter import *

root = Tk()
text_widget = Entry(root, textvariable=StringVar(),font = ("Arial",12))

name = text_widget.get()


def greet():
  name =  text_widget.get()
  label = Label(root, text=name)
  label.pack()

btn = Button(root, text="SUBMIT",bg = "orange",fg = "yellow",command=greet)
text_widget.pack()
btn.pack()

root.mainloop()
