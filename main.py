'''
Main Visual running program
'''

from tkinter import *
import tkinter.ttk as ttk
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

state_colors = {
    "Start": f"{settings.LIGHT_GREEN}",
    "Target": f"{settings.LIGHT_RED}",
    "Wall": f"{settings.GREY}",
    "Visited": f"{settings.LIGHT_BLUE}",
    "Queued": f"{settings.DARK_BLUE}",
    "Shortest-Path": f"{settings.LIGHT_PURPLE}"
}
#######################################################

# Create Window
root.configure(bg='black')
root.title(f"{settings.WIDTH}x{settings.HEIGHT}")
root.geometry('1440x720')
root.resizable(False, False)

# Top frame and elements 
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
    font=('Helvetica', 48),
    borderwidth=0,
    highlightthickness=0,
    padx=10,
    pady=10,
    justify=CENTER
)
program_title.place(
    x=utilities.width_percentage(10), y=utilities.width_percentage(2)
)

# Create a canvas to indicate the colors
canvas = Canvas(top_frame, width=utilities.width_percentage(30), height=utilities.height_percentage(20), background='Black', highlightthickness=0)
canvas.place(x=utilities.height_percentage(140), y=utilities.height_percentage(0))

y = 20
for state, color in state_colors.items():
    canvas.create_rectangle(20, y, 30, y+10, fill=color)
    canvas.create_text(40, y+5, text=state, anchor=W, fill='white')
    y +=20

# Left frame and elements
left_frame = Frame(
    root,
    bg='black',
    width=utilities.width_percentage(25),
    height=utilities.height_percentage(75)
)
left_frame.place(x=0, y=utilities.height_percentage(25))

# Search button
btn_search = Button(
    left_frame,
    width=15,
    height=4,
    text=f"Start Dijkstra \nSearch",
    font=("Helvetica", 12, "bold"),
    relief="sunken",
    bg=settings.BLACK,
    activebackground = 'black',
    activeforeground = settings.WHITE,
    fg=settings.WHITE,
    borderwidth=4,
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
    height=4,
    text=f"Restart",
    font=("Helvetica", 12, "bold"),
    relief="sunken",
    bg=settings.BLACK,
    activebackground = 'black',
    activeforeground = settings.WHITE,
    fg=settings.WHITE,
    borderwidth=4,
    command=restart_grid
)
btn_restart.place(
    x=utilities.width_percentage(8.5), 
    y=utilities.height_percentage(40)
)

# Center frame and elements
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