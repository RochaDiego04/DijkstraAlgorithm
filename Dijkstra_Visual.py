from tkinter import *
import settings
import utilities


root = Tk()

# Create Window
root.configure(bg='black')
root.title(f"{settings.WIDTH}x{settings.HEIGHT}")
root.geometry('1440x720')
root.resizable(False, False)

top_frame = Frame(
    root,
    bg='red',
    width=settings.WIDTH,
    height=utilities.height_percentage(25)
)
top_frame.place(x=0,y=0)

left_frame = Frame(
    root,
    bg='blue',
    width=utilities.width_percentage(25),
    height=utilities.height_percentage(75)
)
left_frame.place(x=0, y=utilities.height_percentage(25))

center_frame = Frame(
    root,
    bg='black',
    width=utilities.width_percentage(75),
    height=utilities.height_percentage(75)
)
center_frame.place(x=utilities.width_percentage(25), y=utilities.height_percentage(25))

# Run window
root.mainloop()