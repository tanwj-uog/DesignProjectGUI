import os
from tkinter import *
from PIL import ImageTk, Image
import time
import datetime
from tkinter import messagebox


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

# Declaration of variables for timer
hour = "0"
minute = "0"
second = "5"

def completedCallback():
    root.destroy()
    os.system('python3 completed.py')

# timer 
def timer(hour,minute,second):    


    current_time = int(hour)*3600 + int(minute)*60 + int(second)
    while current_time >0:
         
        # divmod(firstvalue = temp//60, secondvalue = temp%60)
        mins,secs = divmod(current_time,60)
  
        # Converting the input entered in mins or secs to hours,
        # mins ,secs(input = 110 min --> 120*60 = 6600 => 1hr :
        # 50min: 0sec)
        hours=0
        if mins >60:
             
            # divmod(firstvalue = temp//60, secondvalue
            # = temp%60)
            hours, mins = divmod(mins, 60)
         
        # using format () method to store the value up to
        # two decimal places

        current_time -= 1
        conversion = datetime.timedelta(seconds=current_time)
        converted_time = str(conversion)
        timer_label.config(text=converted_time)

  
        # updating the GUI window after decrementing the
        # temp value every time

        root.update()
        time.sleep(1)

        if (current_time == 0):
             #messagebox.showinfo("Time Countdown", "Time's up ")
             completedCallback()
        



# Timer widget
timer_label = Label(root, text="", bg="white", font=("Arial bold", 24))

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

timer(hour,minute,second)
root.mainloop()