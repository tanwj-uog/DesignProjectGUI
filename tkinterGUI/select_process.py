from tkinter import *
from PIL import ImageTk, Image


root = Tk()
root.title('Home')
root.geometry('{}x{}'.format(800, 480))
root['background'] = '#FFFFFF'

"""
Creating and laying out all of the main containers
"""
# create all of the main containers
first_frame = Frame(root, bg='white', width=800, height=120)
second_frame = Frame(root, bg='white', width=800, height=120)
third_frame = Frame(root, bg='white', width=800, height=120)
fourth_frame = Frame(root, bg='white', width=800, height=120)

# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
first_frame.grid(row=0, sticky="ew")
second_frame.grid(row=1, sticky="ew")
third_frame.grid(row=2, sticky="ew")
fourth_frame.grid(row=3, sticky="ew")


"""
Creation of widgets that will be inflated onto the frames
"""
# Circle decorations at the top left corner
circle_img = (Image.open("images/corner.PNG"))
resized_img = circle_img.resize((130, 120), Image.ANTIALIAS)
circle = ImageTk.PhotoImage(resized_img)
circle_img_label = Label(image=circle, bg="white")

# Full Process Button
fullprocess_btn_img = PhotoImage(file="images/fullprocess_btn.PNG")
fullprocess_btn = Button(root, image=fullprocess_btn_img,
             borderwidth=0, bg="white")

# Clean Only Button
cleanonly_btn_img = PhotoImage(file="images/cleanonly_btn.PNG")
cleanonly_btn = Button(root, image=cleanonly_btn_img,
                       borderwidth=0, bg="white")

# Sterilise Only Button
steriliseonly_btn_img = PhotoImage(file="images/steriliseonly_btn.PNG")
steriliseonly_btn = Button(root, image=steriliseonly_btn_img,
                       borderwidth=0, bg="white")

# Dry Only Button
dryonly_btn_img = PhotoImage(file="images/dryonly_btn.PNG")
dryonly_btn = Button(root, image=dryonly_btn_img,
                       borderwidth=0, bg="white")

# Inflating the widgets in the first frame
circle_img_label.grid(row=0, column=0, sticky=NW)
fullprocess_btn.grid(row=0, column=0, sticky=NS)

# Inflating the widgets in the second frame
cleanonly_btn.grid(row=1, column=0, sticky=NS)

# Inflating the widgets in the third frame
steriliseonly_btn.grid(row=2, column=0, sticky=NS)

# Inflating the widgets in the fourth frame
dryonly_btn.grid(row=3, column=0, sticky=NS)

root.mainloop()
