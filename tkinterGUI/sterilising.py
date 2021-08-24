from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Sterilising')
root.geometry('{}x{}'.format(800, 480))
root['background'] = '#FFFFFF'

"""
Creating and laying out all of the main containers
"""
# create all of the main containers
top_frame = Frame(root, bg='white', width=800, height=300)
bottom_frame = Frame(root, bg='white', width=800, height=180)

# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
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
sterilizer_img = (Image.open("images/sterilizer.png"))
resized_img = sterilizer_img.resize((280, 280), Image.ANTIALIAS)
sterilizer = ImageTk.PhotoImage(resized_img)
sterilizer_img_label = Label(image=sterilizer, bg="white")

# "Sterilising NGT" label widget
sterilisingNGT_label = Label(root, text="Sterilising NGT", bg="white", font=("Arial bold", 24))

# Timer widget
timer_label = Label(root, text="00:05:00", bg="white", font=("Arial bold", 24))

# Stop and Pause button widget
stop_img = (Image.open("images/stop.PNG"))
stop = ImageTk.PhotoImage(stop_img)
stop_btn = Button(root, image=stop,
                       borderwidth=0, bg="white", highlightthickness = 0, bd = 0)

pause_img = (Image.open("images/pause.PNG"))
pause = ImageTk.PhotoImage(pause_img)
pause_btn = Button(root, image=pause,
                       borderwidth=0, bg="white", highlightthickness = 0, bd = 0 )
# Temp & Humidity
dht_label = Label(root, text="28°C\n30%", bg="white", font=("Arial bold", 24))

# Inflating the widgets in the top frame
circle_img_label.grid(row=0, column=0, sticky=NW)
sterilizer_img_label.grid(row=0, column=0, sticky=NS)
dht_label.grid(row=0, column=0, sticky=NE)

# Inflating the widgets in the bottom frame
sterilisingNGT_label.grid(row=1, column=0, sticky=N)
timer_label.grid(row=1, column=0, pady=(35,0))
stop_btn.grid(row=1, column=0, sticky=SW)
pause_btn.grid(row=1, column=0, sticky=SE)

root.mainloop()