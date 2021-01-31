# 
import sys
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
import tkinter.font as tkFont
from PIL import Image, ImageTk
import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt
mpl.use("TkAgg")
import genClass

class GridApp:
    """The main class representing a grid of coloured cells."""

    def __init__(self, master, n, width=600, height=600, pad=5):
        """Initialize a grid and the Tk Frame on which it is rendered."""
        menu = Menu(master)
        master.config(menu=menu)
        fileMenu = Menu(menu)
        fileMenu.add_command(label="Generate Classic", command=self.newClass)
        fileMenu.add_command(label="Generate DWave")
        fileMenu.add_command(label="Solve Classic")
        fileMenu.add_command(label="Solve DWave")
        fileMenu.add_command(label="Exit", command=self.exitProgram)
        menu.add_cascade(label="Options", menu=fileMenu)
        editMenu = Menu(menu)
        editMenu.add_command(label="Clear", command=self.clearAll)
        editMenu.add_command(label="Done!", command=self.gameOVER)
        menu.add_cascade(label="Edit", menu=editMenu)

        # Number of cells in each dimension.
        # Some dimensions for the App in pixels.
        self.width, self.height = width, height
        palette_height = 40
        # Padding stuff: xsize, ysize is the cell size in pixels (without pad).
        npad = N + 1
        self.pad = pad
        xsize = (width - npad*pad) / N
        ysize = (height - npad*pad) / N
        # Canvas dimensions for the cell grid and the palette.
        c_width, c_height = width, height
        p_pad = 5
        p_width = p_height = palette_height - 2*p_pad

        # The main frame onto which we draw the App's elements.
        frame = Frame(master)
        frame.pack()

        # The canvas onto which the grid is drawn.
        self.w = Canvas(master, width=c_width, height=c_height)
        self.w.pack()

        load = Image.open("puzzle.png")
        render = ImageTk.PhotoImage(load)
        self.puzzle = Label(self.w, image=render)
        self.puzzle.image = render
        self.puzzle.place(x=0, y=0)

        load = Image.open("duck1.png")
        pil_image1 = ImageTk.PhotoImage(load)
        load = Image.open("duck2.png")
        pil_image2 = ImageTk.PhotoImage(load)

        button_width=10

        # Add labels
        self.text_lab = []
        dx = 600/N
        for iy in range(0,N):
            for ix in range(0,N):
                if guess[iy][ix] == 0:
                    text = Label(self.w, text=symbols[0], font=("Arial", fontsize))
                elif guess[iy][ix] == 1:
                    text = Label(self.w, text=symbols[1], font=("Arial", fontsize))
                elif guess[iy][ix] == 2:
                    text = Label(self.w, text=symbols[2], font=("Arial", fontsize))
                text.place(x=ix*dx+dx/2,y=iy*dx+dx/2)
                self.text_lab.append(text)


        def w_click_callback(event):
            """Function called when someone clicks on the grid canvas."""
            x, y = event.x, event.y

            # Did the user click a cell in the grid?
            # Indexes into the grid of cells (including padding)
            ix = int(x // (xsize + pad))
            iy = int(y // (ysize + pad))
            xc = x - ix*(xsize + pad) - pad
            yc = y - iy*(ysize + pad) - pad
            if ix < N and iy < N and 0 < xc < xsize and 0 < yc < ysize:
                i = iy*N+ix
                if guess[iy][ix]==0:
                    guess[iy][ix]=1
                    self.text_lab[i].config(text=symbols[1], font=("Arial", fontsize) )
                elif guess[iy][ix]==1:
                    guess[iy][ix]=2
                    self.text_lab[i].config(text=symbols[2], font=("Arial", fontsize) )
                elif guess[iy][ix]==2:
                    guess[iy][ix]=0
                    self.text_lab[i].config(text=symbols[0], font=("Arial", fontsize) )

        # Bind the grid click callback function to the left mouse button
        # press event on the grid canvas.
        self.puzzle.bind('<ButtonPress-1>', w_click_callback)

    def _get_cell_coords(self, i):
        """Get the <letter><number> coordinates of the cell indexed at i."""
        # The horizontal axis is labelled A, B, C, ... left-to-right;
        # the vertical axis is labelled 1, 2, 3, ... bottom-to-top.
        iy, ix = divmod(i, self.n)
        return '{}{}'.format(chr(ix+65), self.n-iy)

    def clearAll(self):
        for iy in range(0,N):
            for ix in range(0,N):
                i = iy*n+ix
                guess[iy][ix] = 0
                self.text_lab[i].config(text='', font=("Arial", fontsize))

    def gameOVER(self):
        if np.array_equal(stars, guess):
            print("You won")
        else:
            print("You lost")

    def newClass(self):
        grid,stars = genClass.generate_classic(N,S)
        load = Image.open("puzzle.png")
        render = ImageTk.PhotoImage(load)
        self.puzzle.image = render
        self.puzzle.place(x=0, y=0)

    # leave patoLogic
    def exitProgram(self):
        exit()

if __name__ == "__main__":

    # Maximum and default grid size
    MAX_N=26; N=5; S=1
    grid,stars = genClass.generate_classic(N,S)

    symbols = ['','*','o']
    fontsize = 25

    guess = np.zeros((N,N))#np.copy(stars)

    # Set the whole thing running
    root = Tk()
    root.title("patoLogic") # Add a title
    grid = GridApp(root, N, 600, 600, 5)
    # Don't allow resizing in the x or y direction
    root.resizable(0,0)
    p1 = PhotoImage(file = 'duck2.png')
    # Icon set for program window
    root.iconphoto(False, p1)
    root.mainloop()
