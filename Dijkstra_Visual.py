'''
Main Visual running program
'''

from tkinter import *
import settings
import utilities
from cell import Cell


root = Tk()

################# FUNCTIONS ###########################
def restart_grid():
    delete_grid()
    Cell.reset_all_cells()
    create_grid()

def delete_grid():
    # Get all the widgets in center_frame
    widgets = center_frame.grid_slaves()
    # Remove all the widgets from center_frame
    for widget in widgets:
        widget.destroy()

def create_grid():
    for x in range(settings.GRID_SIZE):
        for y in range(settings.GRID_SIZE):
            c = Cell(x, y)
            c.create_btn_object(center_frame)
            c.cell_btn_object.grid( # Will take the center frame as the parent
            column=x,row=y
            )
#######################################################

# Create Window
root.configure(bg='black')
root.title(f"{settings.WIDTH}x{settings.HEIGHT}")
root.geometry('1440x720')
root.resizable(False, False)

# Creation of Frames
top_frame = Frame(
    root,
    bg='black',
    width=settings.WIDTH,
    height=utilities.height_percentage(25)
)
top_frame.place(x=0,y=0)

program_title = Label(
    top_frame,
    bg='black',
    fg='white',
    text="DIJKSTRA'S ALGORITHM",
    font=('', 48)
)
program_title.place(
    x=utilities.width_percentage(25), y=0
)

left_frame = Frame(
    root,
    bg='blue',
    width=utilities.width_percentage(25),
    height=utilities.height_percentage(75)
)
left_frame.place(x=0, y=utilities.height_percentage(25))

# Search button
btn_search = Button(
    left_frame,
    width=15,
    height=5,
    text=f"Start Dijkstra Search",
    command=Cell.start_dijkstra_search
)
btn_search.place(
    x=utilities.width_percentage(8.5), 
    y=utilities.height_percentage(0.5)
)

# Restart button
btn_restart = Button(
    left_frame,
    width=15,
    height=5,
    text=f"Restart",
    command=restart_grid
)
btn_restart.place(
    x=utilities.width_percentage(8.5), 
    y=utilities.height_percentage(60)
)

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

# Create Grid
create_grid()

# Run window
root.mainloop()