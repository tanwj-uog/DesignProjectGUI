from tkinter import *
from tkinter.ttk import Style
from PIL import ImageTk, Image
import tkinter.font as font

root = Tk(className='Home Page')
root.geometry("800x480")
print(font.families())
btn_style = Style()
btn_style.configure('btn_style', font = ('Arial', 18, 'bold'), background = 'blue' )
#frame = Frame(root)
#frame.pack()

#canvas = Canvas(root, bg="#FFFFFF", width=800, height=480)
#canvas.pack()

# Set window size to match BIGTREETECT PI TFT50 5 inch screen
#root.geometry("800x480")

# Set background color
root['background'] = '#FFFFFF'

# img = Image.open("hom2.png")
# img = img.resize((93, 163), Image.ANTIALIAS)
# resized_img = ImageTk.PhotoImage(img)
# panel = Label(canvas, image = resized_img)
# panel.pack()

#img = (Image.open("doctor.png"))
#resized_image= img.resize((93,163), Image.ANTIALIAS)
#doctor = ImageTk.PhotoImage(resized_image)

#doctor = PhotoImage(file = "hom2.png")
#canvas.create_image(0,0, anchor=NW, image=doctor)

circle_img = (Image.open("images/corner.PNG"))
resized_img = circle_img.resize((180, 165), Image.ANTIALIAS)
circle = ImageTk.PhotoImage(resized_img)
circle_img_label = Label(image=circle, bg="white")
circle_img_label.grid(sticky=N)
#circle_img_label.pack()

# spacer1 = Label(root, text="" , bg="white")
# spacer1.grid(row=0, column=1)

doctor_img = (Image.open("images/doctor.png"))
resized_img = doctor_img.resize((170, 288), Image.ANTIALIAS)
doctor = ImageTk.PhotoImage(resized_img)
doctor_img_label = Label(image=doctor, bg="white")
doctor_img_label.grid(row=0, column=1, sticky=N, padx=(0,175))
#doctor_img_label.pack()


ngtCleaner_label = Label(root, text = "   NGT Cleaner", bg="white", font=("Arial bold", 18))
ngtCleaner_label.grid(row=1, column=1, sticky=N, padx=(0,177))

# Add Image
start_btn_img1 = (Image.open("images/start_btn.PNG"))
#start_btn_img = PhotoImage(file="start_btn.PNG")
start_btn_img = ImageTk.PhotoImage(start_btn_img1)

# Create button and image
start_btn = Button(root, image=start_btn_img,
             borderwidth=0, bg="white")
start_btn.grid(row=2, column=1, padx=(0,0))

spacer1 = Label(root, text="asdasdas", bg="white")
spacer1.grid(row=2, column=2, padx=250)


root.mainloop()
