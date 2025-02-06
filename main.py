from tkinter import *
from time import strftime
from PIL import Image, ImageTk

def update():
    """Update the time, day, and date dynamically."""
    time_string = strftime("%I:%M:%S %p")
    day_string = strftime("%A")
    date_string = strftime("%B %d, %Y")

    # Update text items on canvas
    canvas.itemconfig(time_text, text=time_string)
    canvas.itemconfig(day_text, text=day_string)
    canvas.itemconfig(date_text, text=date_string)

    window.after(1000, update)  # Schedule next update

window = Tk()
window.title("Ghibli Clock")
icon = PhotoImage(file="icon.png") # creates a photo image object
window.iconphoto(True, icon) # sets the icon of the window

width = window.winfo_screenwidth()
height = window.winfo_screenheight()

# Create a canvas that fills the window
canvas = Canvas(window, width=width, height=height, highlightthickness=0)
canvas.pack(fill="both", expand=True)

# Load and set background image
bg_photo = Image.open("background.png")
bg_photo = bg_photo.resize((width, height))
bg_photo = ImageTk.PhotoImage(bg_photo)
canvas.create_image(0, 0, image=bg_photo, anchor=NW)

# Add static text elements on canvas

canvas.create_text(width / 2, height / 2 + 100, 
                   text="Dream Big, Keep Exploring! 🚀", 
                   font=("Courier", 12, "bold"), fill="#b35b45")

# Add dynamic text placeholders
time_text = canvas.create_text(width / 2, height / 2 - 100, 
                               text="", font=("Helvetica", 48, "bold"), fill="#d68263")

day_text = canvas.create_text(width / 2, height / 2-10, 
                              text="", font=("Ink Free", 22, "bold"), fill="#d68263")

date_text = canvas.create_text(width / 2, height / 2 + 20, 
                               text="", font=("Ink Free", 22, "bold"), fill="#d68263")

# Start updating time
update()

window.mainloop()
