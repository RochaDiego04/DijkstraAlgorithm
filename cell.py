from tkinter import Button

class Cell:
    all = []
    num_of_start_point = 0
    num_of_end_point = 0
    
    def __init__(self, x, y):
        self.is_start_point = False
        self.is_empty = True
        self.is_end_point = False
        self.is_barreer = False
        self.cell_btn_object = None
        self.x = x
        self.y = y

        # Append the object to the Cell.all List
        Cell.all.append(self)

    def create_btn_object(self, location):
        btn = Button(
            location,
            width=12,
            height=4,
            text=f"{self.x},{self.y}"
        )
        btn.bind('<Button-1>', self.left_click_actions) # Left Click
        btn.bind('<Button-3>', self.right_click_actions) # Right Click
        self.cell_btn_object = btn

    def left_click_actions(self, event):
        if not self.is_barreer and self.is_empty and Cell.num_of_start_point < 1:
            self.show_start_point()
            self.is_start_point = True
            self.is_empty = False
            Cell.num_of_start_point = 1
        elif self.is_start_point:
            self.show_empty()
            self.is_start_point = False
            self.is_empty = True
            Cell.num_of_start_point = 0
        elif not self.is_barreer and self.is_empty and Cell.num_of_start_point == 1 and Cell.num_of_end_point < 1:
            self.show_end_point()
            self.is_end_point = True
            self.is_empty = False
            Cell.num_of_end_point = 1
        elif self.is_end_point:
            self.show_empty()
            self.is_end_point = False
            self.is_empty = True
            Cell.num_of_end_point = 0


    def right_click_actions(self, event):
        print(event)
        print("I am right clicked!")
    
    @property # We can now use this as an attribute
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y - 1),
            self.get_cell_by_axis(self.x - 1, self.y),
            self.get_cell_by_axis(self.x - 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y - 1),
            self.get_cell_by_axis(self.x + 1, self.y),
            self.get_cell_by_axis(self.x + 1, self.y + 1),
            self.get_cell_by_axis(self.x, self.y + 1)
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells
    
    def show_cell(self):
        self.cell_btn_object.configure(text=self.surrounded_cells_mines_length)
    
    def show_start_point(self):
        self.cell_btn_object.configure(bg='green')
    
    def show_empty(self):
        self.cell_btn_object.configure(bg='SystemButtonFace')

    def show_end_point(self):
        self.cell_btn_object.configure(bg='red')
    
    def __repr__(self):
        return f"Cell({self.x}, {self.y})"