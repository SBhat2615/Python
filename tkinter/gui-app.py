import tkinter as tk

HEIGHT = 427
WIDTH = 640

def get_weather(entry):
  label['text'] = entry

root = tk.Tk()

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='desert.png')
background_label = tk.Label(root, image=background_image)
background_label.place(x=0, y=0, relwidth=1, relheight=1)

# Frame 1
frame1 = tk.Frame(root, bg='#80c1ff', bd=5)
frame1.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame1, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame1, text="Get Weather", font=40, command=lambda: get_weather(entry.get()))
button.place(relx=0.7, relwidth=0.3, relheight=1)

# Frame 2
frame2 = tk.Frame(root, bg='#80c1ff', bd=10)
frame2.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(frame2, font=('Courier', 18))
label.place(relwidth=1, relheight=1)

# entry = tk.Entry(frame, bg='green')
# entry.place(relx=0.8, rely=0, relwidth=0.2, relheight=0.1)

root.mainloop()