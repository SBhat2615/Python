import tkinter as tk

HEIGHT = 700
WIDTH = 800

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

frame = tk.Frame(root, bg='#80c1ff')
frame.place(relx=0.1, rely=0.1, relwidth=0.8, relheight=0.5)

button = tk.Button(frame, text="Test button")
button.place(relx=0, rely=0, relwidth=0.25, relheight=0.25)

label = tk.Label(frame, text="This is a Label", bg='yellow', fg='red')
label.place(relx=0.3, rely=0, relwidth=0.45, relheight=0.25)

entry = tk.Entry(frame, bg='green')
entry.place(relx=0.8, rely=0, relwidth=0.2, relheight=0.1)

root.mainloop()