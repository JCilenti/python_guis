# this is a tkinter gui file

import tkinter as tk

window = tk.Tk() # create a tkinter object/window


greeting = tk.Label(
    text="Hello, CY383 Class", 
    fg="white", 
    bg="black",
    width="50",
    height="50")
greeting.pack()

button = tk.Button(
    text = "CLICK ME!!!",
    width=25,
    height=5,
    bg="blue",
    fg="yellow")
button.pack()

user_data = tk.Entry(fg="yellow", bg="blue", width=50)
user_data.pack()
data = user_data.get()

text_box = tk.Text()
text_box.pack()


#window.geometry("400x400")

if __name__ == '__main__':

    window.mainloop()
