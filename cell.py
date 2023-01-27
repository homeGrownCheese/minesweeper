from tkinter import Button


def left_click_actions(event):
    print(event)
    print("I am left clicked")


def right_click_actions(event):
    print(event)
    print("I am right clicked")


class Cell:
    def __init__(self, is_mine=False):
        self.is_mine = is_mine
        self.cell_btn_object = None

    def create_btn_object(self, location):
        btn = Button(
            location,
            text='Text',
        )
        btn.bind('<Button-1>', left_click_actions)  # Left click
        btn.bind('<Button-3>', right_click_actions)  # Right click
        self.cell_btn_object = btn
