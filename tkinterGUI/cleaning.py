from tkinter import *
from PIL import ImageTk, Image

cleaning = Tk()
cleaning.title('Cleaning')
cleaning.geometry('{}x{}'.format(800, 480))
cleaning['background'] = '#FFFFFF'

"""
Creating and laying out all of the main containers
"""
# create all of the main containers
top_frame = Frame(cleaning, bg='white', width=800, height=300)
bottom_frame = Frame(cleaning, bg='white', width=800, height=180)

# layout all of the main containers
cleaning.grid_rowconfigure(1, weight=1)
cleaning.grid_columnconfigure(0, weight=1)
top_frame.grid(row=0, sticky="ew")
bottom_frame.grid(row=1, sticky="ew")


"""
Creation of widgets that will be inflated onto the frames
"""
# Circle decorations at the top left corner
circle_img = (Image.open("images/corner.PNG"))
resized_img = circle_img.resize((130, 120), Image.ANTIALIAS)
circle = ImageTk.PhotoImage(resized_img)
circle_img_label = Label(image=circle, bg="white")

# Bubbles illustration to signifiy cleaning
bubble_img = (Image.open("images/bubbles.png"))
resized_img = bubble_img.resize((280, 280), Image.ANTIALIAS)
bubble = ImageTk.PhotoImage(resized_img)
bubble_img_label = Label(image=bubble, bg="white")

# "Cleaning NGT" label widget
cleaningNGT_label = Label(cleaning, text="Cleaning NGT", bg="white", font=("Arial bold", 24))

# Timer widget
timer_label = Label(cleaning, text="00:01:00", bg="white", font=("Arial bold", 24))

# Stop and Pause button widget
stop_img = (Image.open("images/stop.PNG"))
stop = ImageTk.PhotoImage(stop_img)
stop_btn = Button(cleaning, image=stop,
                  borderwidth=0, bg="white", highlightthickness = 0, bd = 0)

pause_img = (Image.open("images/pause.PNG"))
pause = ImageTk.PhotoImage(pause_img)
pause_btn = Button(cleaning, image=pause,
                   borderwidth=0, bg="white", highlightthickness = 0, bd = 0)
# Temp & Humidity
dht_label = Label(cleaning, text="28°C\n30%", bg="white", font=("Arial bold", 24))

# Inflating the widgets in the top frame
circle_img_label.grid(row=0, column=0, sticky=NW)
bubble_img_label.grid(row=0, column=0, sticky=NS)
dht_label.grid(row=0, column=0, sticky=NE)

# Inflating the widgets in the bottom frame
cleaningNGT_label.grid(row=1, column=0, sticky=N)
timer_label.grid(row=1, column=0, pady=(35,0))
stop_btn.grid(row=1, column=0, sticky=SW)
pause_btn.grid(row=1, column=0, sticky=SE)

cleaning.mainloop()