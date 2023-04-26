from tkinter import Button, Tk
from tkinter import messagebox
from collections import deque
import settings
import time

class Cell:
    all = []
    queue = deque()
    visited = []
    path = []

    num_of_start_point = 0
    num_of_end_point = 0
    target_cell = None
    begin_search = True
    
    def __init__(self, x, y):
        self.is_start_point = False
        self.is_empty = True
        self.is_end_point = False
        self.is_barreer = False
        self.is_visited = False
        self.parent = None
        self.cell_btn_object = None
        self.x = x
        self.y = y
        self.distance = float('inf')

        # Append the object to the Cell.all List
        Cell.all.append(self)
    
    def create_btn_object(self, location):
        btn = Button(
            location,
            width=4,
            height=2,
        )
        btn.bind('<Button-1>', self.left_click_actions) # Left Click
        btn.bind('<Button-3>', self.right_click_actions) # Right Click
        self.cell_btn_object = btn

    def left_click_actions(self, event):
        if not self.is_barreer and self.is_empty and Cell.num_of_start_point < 1:
            self.show_start_point()
            self.is_start_point = True
            self.is_visited = True
            self.is_empty = False
            Cell.num_of_start_point = 1
        elif self.is_start_point:
            self.show_empty()
            self.is_start_point = False
            self.is_visited = False
            self.is_empty = True
            Cell.num_of_start_point = 0
        elif not self.is_barreer and self.is_empty and Cell.num_of_start_point == 1 and Cell.num_of_end_point < 1:
            self.show_end_point()
            self.is_end_point = True
            self.is_visited = False
            self.is_empty = False
            Cell.num_of_end_point = 1
            Cell.target_cell = self
        elif self.is_end_point:
            self.show_empty()
            self.is_end_point = False
            self.is_visited = False
            self.is_empty = True
            Cell.num_of_end_point = 0
        print(f"Cell neighbours:  {self.surrounded_cells}")
        print(f"Cell: {self} \nIs barreer: {self.is_barreer} \nIs startPoint: {self.is_start_point} \nIs endPoint: {self.is_end_point} \nIs empty: {self.is_empty} \nIs visited: {self.is_visited}")

    def right_click_actions(self, event):
        if not self.is_start_point and not self.is_end_point and self.is_empty:
            self.show_barreer()
            self.is_empty = False
            self.is_barreer = True
        elif self.is_barreer:
            self.show_empty()
            self.is_barreer = False
            self.is_empty = True
        print(f"Cell: {self} \nIs barreer: {self.is_barreer} \nIs startPoint: {self.is_start_point} \nIs endPoint: {self.is_end_point} \nIs empty: {self.is_empty} \nIs visited: {self.is_visited}")
    
    def get_cell_by_axis(self, x, y):
        # return a cell object based on the value of x and y
        for cell in Cell.all:
            if cell.x == x and cell.y == y:
                return cell

    @property # We can now use this as an attribute
    def surrounded_cells(self):
        cells = [
            self.get_cell_by_axis(self.x - 1, self.y), 
            self.get_cell_by_axis(self.x, self.y - 1), 
            self.get_cell_by_axis(self.x + 1, self.y), 
            self.get_cell_by_axis(self.x, self.y + 1) 
        ]
        cells = [cell for cell in cells if cell is not None]
        return cells

    
    def show_cell(self):
        self.cell_btn_object.configure(text=self.surrounded_cells_mines_length)
    
    def show_start_point(self):
        self.cell_btn_object.configure(bg=settings.LIGHT_GREEN)
    
    def show_empty(self):
        self.cell_btn_object.configure(bg='SystemButtonFace')

    def show_end_point(self):
        self.cell_btn_object.configure(bg=settings.LIGHT_RED)
    
    def show_barreer(self):
        self.cell_btn_object.configure(bg=settings.GREY)
    
    def show_queued(self):
        self.cell_btn_object.configure(bg=settings.DARK_BLUE)

    def show_visited(self):
        self.cell_btn_object.configure(bg=settings.LIGHT_BLUE)
    
    def show_path(self):
        if self in Cell.path:
            self.cell_btn_object.configure(bg=settings.LIGHT_PURPLE)

    @staticmethod
    def quit_cell_events():
        for cell in Cell.all:
            cell.cell_btn_object.unbind('<Button-1>')
            cell.cell_btn_object.unbind('<Button-3>')
    
    def __repr__(self):
        return f"Cell({self.x}, {self.y})"
    
    @staticmethod
    def reset_all_cells():
        # Delete all Cell instances
        Cell.all.clear()
        Cell.queue.clear()

        # Reset all class variables
        Cell.visited = []
        Cell.path = []
        Cell.num_of_start_point = 0
        Cell.num_of_end_point = 0
    
    @staticmethod
    def start_dijkstra_search():
        start_cell = None
        target_cell = None

        if Cell.num_of_start_point == 1 and Cell.num_of_end_point == 1:
            # Search for the start and target cell, set the distance of the start to 0
            for cell in Cell.all:
                if cell.is_start_point:
                    start_cell = cell
                    cell.distance = 0
                if cell.is_end_point:
                    target_cell = cell
            
             # Dijkstra's algorithm
            queue = deque([start_cell])
            while queue:
                curr_cell = queue.popleft()
                curr_cell.is_visited = True
                curr_cell.show_visited()
                Cell.visited.append(curr_cell)  # add visited cell to the list
                if curr_cell == target_cell:
                    # messagebox.showinfo("Path Found", f"Path from {start_cell} to {target_cell}.")
                    break
                for adj_cell in curr_cell.surrounded_cells:
                    if not adj_cell.is_barreer:
                        new_distance = curr_cell.distance + 1 # All edges have a weight of 1
                        if new_distance < adj_cell.distance:
                            adj_cell.distance = new_distance
                            adj_cell.parent = curr_cell
                            queue.append(adj_cell)
                            adj_cell.show_queued()

            # Check if there's a path
            if target_cell.distance == float('inf'):
                messagebox.showinfo("No Path Found", "There is no path to the target cell.")
                Cell.quit_cell_events()
                return

            # Traverse the cells from the target cell to the start cell
            curr_cell = target_cell
            while curr_cell != start_cell:
                Cell.path.insert(0, curr_cell)
                curr_cell = curr_cell.parent
            
            # Finally adding the start cell to the Path
            Cell.path.insert(0, start_cell)

            # Show the path
            for cell in Cell.path:
                cell.show_path()
            
            Cell.quit_cell_events()
    



