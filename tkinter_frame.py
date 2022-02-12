import tkinter as tk


window  = tk.Tk()

frame_a = tk.Frame()
frame_b = tk.Frame()

label_a = tk.Label(master=frame_a, text = "I'm in frame A")
label_b = tk.Label(master=frame_b, text = "I'm in frame B")

label_a.pack()
label_b.pack()

# the order you pack a frame is the order it is displayed
frame_a.pack()
frame_b.pack()

window.mainloop()

