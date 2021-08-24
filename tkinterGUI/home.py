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
top_frame = Frame(root, bg='white', width=800, height=250)
#middle_frame = Frame(root, bg='gray', width=800, height=50)
bottom_frame = Frame(root, bg='white', width=800, height=130)

# layout all of the main containers
root.grid_rowconfigure(1, weight=1)
root.grid_columnconfigure(0, weight=1)
top_frame.grid(row=0, sticky="ew")
#middle_frame.grid(row=1, sticky="ew")
bottom_frame.grid(row=1, sticky="ew")

"""
Creation of widgets that will be inflated onto the top frame
"""
# Circle decorations at the top left corner
circle_img = (Image.open("images/corner.PNG"))
resized_img = circle_img.resize((130, 120), Image.ANTIALIAS)
circle = ImageTk.PhotoImage(resized_img)
circle_img_label = Label(image=circle, bg="white")

# Doctor holding syringe illustration
doctor_img = (Image.open("images/doctor.png"))
resized_img = doctor_img.resize((133, 216), Image.ANTIALIAS)
doctor = ImageTk.PhotoImage(resized_img)
doctor_img_label = Label(image=doctor, bg="white")

# Inflating the widgets in the top frame
circle_img_label.grid(row=0, column=0, sticky=NW)
doctor_img_label.grid(row=0, column=0)


"""
Creation of widgets that will be inflated onto the bottom frame
"""
# Label for the word "NGT Cleaner"
ngtCleaner_label = Label(root, text="NGT Cleaner", bg="white", font=("Arial bold", 18))

# Start Cleaning Button
start_btn_img = PhotoImage(file="images/start_btn.PNG")
start_btn = Button(root, image=start_btn_img,
             borderwidth=0, bg="white", highlightthickness = 0, bd = 0)

# Inflating the widgets in the bottom frame
ngtCleaner_label.grid(row=1, column=0, sticky=N)
start_btn.grid(row=1, column=0)

root.mainloop()
