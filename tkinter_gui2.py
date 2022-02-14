import tkinter as tk
from matplotlib import image

from matplotlib.pyplot import fill, text

window = tk.Tk()
window.geometry("500x950")

# image file for background
bg = tk.PhotoImage(file = "gradient2.png")

# create canvas
canvas1 = tk.Canvas(window, width=500, height=950)
canvas1.pack(fill="both", expand=True)

# display image
canvas1.create_image(0, 0, image = bg, anchor = "nw")

# Add text
canvas1.create_text(250, 237.5, fill="white", font= "Roboto 32",text = "Welcome")

# create a text box
text_entry1 = tk.Entry(canvas1)
text_entry2 = tk.Entry(canvas1)
text_entry3 = tk.Entry(canvas1)

canvas1.create_window(200, 412.5, window=text_entry1, height=40, width=200)
canvas1.create_window(200, 452.5, window=text_entry2, height=40, width=200)
canvas1.create_window(200, 492.5, window=text_entry3, height=40, width=200)

# Create buttons
button1 = tk.Button(window, text = "Exit")
button3 = tk.Button(window, text = "Start")
button2 = tk.Button(window, text = "Reset")

# display buttons
button1_canvas = canvas1.create_window(350, 412.5, window = button1)
button2_canvas = canvas1.create_window(350, 452.5, window = button2)
button3_canvas = canvas1.create_window(350, 492.5, window = button3)



if __name__ == '__main__':
    window.mainloop()