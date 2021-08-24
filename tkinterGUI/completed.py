from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Completed')
root.geometry('{}x{}'.format(800, 480))
root['background'] = '#FFFFFF'

"""
Creating and laying out all of the main containers
"""
# create all of the main containers
top_frame = Frame(root, bg='white', width=800, height=250)
bottom_frame = Frame(root, bg='white', width=800, height=130)

# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
top_frame.grid(row=0, sticky="ew")
bottom_frame.grid(row=1, sticky="ew")

"""
Creation of widgets that will be inflated onto the top frame
"""
# Circle decorations at the top left corner
circle_img = (Image.open("images/corner.PNG"))
resized_img = circle_img.resize((130, 120), Image.ANTIALIAS)
circle = ImageTk.PhotoImage(resized_img)
circle_img_label = Label(image=circle, bg="white")

# Green tick to signify completion
tick_img = (Image.open("images/green_tick.png"))
resized_img = tick_img.resize((180, 180), Image.ANTIALIAS)
tick = ImageTk.PhotoImage(resized_img)
tick_img_label = Label(image=tick, bg="white")

# Inflating the widgets in the top frame
circle_img_label.grid(row=0, column=0, sticky=NW)
tick_img_label.grid(row=0, column=0)


"""
Creation of widgets that will be inflated onto the bottom frame
"""
# Label for the word "Completed!"
ngtCleaner_label = Label(root, text="Completed!", bg="white", font=("Arial bold", 24))

# Start Cleaning Button
start_btn_img = PhotoImage(file="images/startnewset_btn.PNG")
start_btn = Button(root, image=start_btn_img,
             borderwidth=0, bg="white", highlightthickness = 0, bd = 0)

# Inflating the widgets in the bottom frame
ngtCleaner_label.grid(row=1, column=0, sticky=N)
start_btn.grid(row=1, column=0)

root.mainloop()
