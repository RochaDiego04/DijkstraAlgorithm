'''
Main Visual running program
'''

from tkinter import *
import settings
import utilities
from cell import Cell


root = Tk()

# Create Window
root.configure(bg='black')
root.title(f"{settings.WIDTH}x{settings.HEIGHT}")
root.geometry('1440x720')
root.resizable(False, False)

# Creation of Frames
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
center_frame.place(
    x=utilities.width_percentage(25), 
    y=utilities.height_percentage(25)
)


btn_search = Button(
    left_frame,
    width=15,
    height=5,
    text=f"Start Dijkstra",
    command=Cell.start_dijkstra_search
)
btn_search.place(
    x=utilities.width_percentage(8.5), 
    y=utilities.height_percentage(12.5)
)

# Create Grid
for x in range(settings.GRID_SIZE):
    for y in range(settings.GRID_SIZE):
        c = Cell(x,y)
        c.create_btn_object(center_frame)
        c.cell_btn_object.grid( # Will take the center frame as the parent
            column=x,row=y
        )

# Run window
root.mainloop()