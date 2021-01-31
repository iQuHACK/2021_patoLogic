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
from tkinter import simpledialog

class GridApp:
    """The main class representing a grid of coloured cells."""

    def __init__(self, master, width=600, height=600, pad=5):
        """Initialize a grid and the Tk Frame on which it is rendered."""
        menu = Menu(master)
        master.config(menu=menu)
        fileMenu = Menu(menu)
        fileMenu.add_command(label="Generate Classic", command=self.newClassic)
        fileMenu.add_command(label="Generate Quantum-Inspired", command=self.newInsp)
        fileMenu.add_command(label="Generate Quantum", command=self.newQuantum)
        fileMenu.add_command(label="Solve Classic", command=self.solveClassic)
        fileMenu.add_command(label="Solve Quantum-Inspired", command=self.solveInsp)
        fileMenu.add_command(label="Solve DWave", command=self.solveQuantum)
        fileMenu.add_command(label="Exit", command=self.exitProgram)
        menu.add_cascade(label="Options", menu=fileMenu)
        editMenu = Menu(menu)
        editMenu.add_command(label="Clear", command=self.clearAll)
        editMenu.add_command(label="Done!", command=self.gameOVER)
        menu.add_cascade(label="Edit", menu=editMenu)

        self.N = 5
        self.S = 1

        # Number of cells in each dimension.
        # Some dimensions for the App in pixels.
        self.width, self.height = width, height
        palette_height = 40
        # Canvas dimensions for the cell grid and the palette.
        c_width, c_height = width, height
        p_pad = 5
        p_width = p_height = palette_height - 2*p_pad

        # Padding stuff: xsize, ysize is the cell size in pixels (without pad).
        npad = self.N + 1
        self.pad = pad
        self.xsize = (width - npad*self.pad) / self.N
        self.ysize = (height - npad*self.pad) / self.N

        # The main frame onto which we draw the App's elements.
        frame = Frame(master)
        frame.pack()

        # The canvas onto which the grid is drawn.
        self.w = Canvas(master, width=c_width, height=c_height)
        self.w.pack()

        load = Image.open("start.png")
        render = ImageTk.PhotoImage(load)
        self.start = Label(self.w, image=render)
        self.start.image = render
        self.start.place(x=0, y=0)

        load = Image.open("duck1.png")
        self.pil_image1 = ImageTk.PhotoImage(load)
        load = Image.open("duck2.png")
        self.pil_image2 = ImageTk.PhotoImage(load)

    def _get_cell_coords(self, i):
        """Get the <letter><number> coordinates of the cell indexed at i."""
        # The horizontal axis is labelled A, B, C, ... left-to-right;
        # the vertical axis is labelled 1, 2, 3, ... bottom-to-top.
        iy, ix = divmod(i, self.n)
        return '{}{}'.format(chr(ix+65), self.n-iy)

    def clearAll(self):
        for iy in range(0,self.N):
            for ix in range(0,self.N):
                i = iy*self.N+ix
                self.guess[iy][ix] = 0
                self.text_lab[i].config(text='', font=("Arial", fontsize))

    def gameOVER(self):
        if np.array_equal(self.stars, self.guess):
            print("Correct solution")
        else:
            print("Incorrect solution")

    def w_click_callback(self,event):
        """Function called when someone clicks on the grid canvas."""
        x, y = event.x, event.y

        # Did the user click a cell in the grid?
        # Indexes into the grid of cells (including padding)
        ix = int(x // (self.xsize + self.pad))
        iy = int(y // (self.ysize + self.pad))
        xc = x - ix*(self.xsize + self.pad) - self.pad
        yc = y - iy*(self.ysize + self.pad) - self.pad
        if ix < self.N and iy < self.N and 0 < xc < self.xsize and 0 < yc < self.ysize:
            i = iy*self.N+ix
            if self.guess[iy][ix]==0:
                self.guess[iy][ix]=1
                self.text_lab[i].config(text=symbols[1], font=("Arial", fontsize) )
            elif self.guess[iy][ix]==1:
                self.guess[iy][ix]=2
                self.text_lab[i].config(text=symbols[2], font=("Arial", fontsize) )
            elif self.guess[iy][ix]==2:
                self.guess[iy][ix]=0
                self.text_lab[i].config(text=symbols[0], font=("Arial", fontsize) )
        #draw_board(self.guess)
        #load = Image.open(".board.png")
        #render = ImageTk.PhotoImage(load)
        #self.puzzle.image = render

    def newClassic(self):
        N = simpledialog.askstring(title="Input", prompt="Puzzle dimension")
        self.N = int(N)
        S = simpledialog.askstring(title="Input", prompt="Stars per region")
        self.S = int(S)

        self.grid,self.stars = genClass.generate_classic(self.N,self.S)
        self.guess = np.zeros((self.N,self.N))#np.copy(stars)
        load = Image.open("puzzle.png")
        render = ImageTk.PhotoImage(load)
        self.puzzle = Label(self.w, image=render)
        self.puzzle.image = render
        self.puzzle.place(x=0, y=0)
        self.puzzle.bind('<ButtonPress-1>', self.w_click_callback)
        p1 = PhotoImage(file = 'duck2.png')
        # Icon set for program window
        root.iconphoto(False, p1)

        # Add labels
        self.text_lab = []
        dx = 600/self.N
        for iy in range(0,self.N):
            for ix in range(0,self.N):
                if self.guess[iy][ix] == 0:
                    text = Label(self.w, text=symbols[0], font=("Arial", fontsize))
                elif self.guess[iy][ix] == 1:
                    text = Label(self.w, text=symbols[1], font=("Arial", fontsize))
                elif self.guess[iy][ix] == 2:
                    text = Label(self.w, text=symbols[2], font=("Arial", fontsize))
                text.place(x=ix*dx+dx/2,y=iy*dx+dx/2)
                self.text_lab.append(text)
        mainloop()

    def newInsp(self):

        N = simpledialog.askstring(title="Input", prompt="Puzzle dimension")
        self.N = int(N)
        S = simpledialog.askstring(title="Input", prompt="Stars per region")
        self.S = int(S)

        solution_grid = solve_puzzle(N, nstars, region_grid, annealer="neal", num_reads=200)
        self.grid,self.stars = genClass.generate_classic(self.N,self.S)
        self.guess = np.zeros((self.N,self.N))#np.copy(stars)
        load = Image.open("puzzle.png")
        render = ImageTk.PhotoImage(load)
        self.puzzle = Label(self.w, image=render)
        self.puzzle.image = render
        self.puzzle.place(x=0, y=0)
        self.puzzle.bind('<ButtonPress-1>', self.w_click_callback)
        p1 = PhotoImage(file = 'duck2.png')
        # Icon set for program window
        root.iconphoto(False, p1)

        # Add labels
        self.text_lab = []
        dx = 600/self.N
        for iy in range(0,self.N):
            for ix in range(0,self.N):
                if self.guess[iy][ix] == 0:
                    text = Label(self.w, text=symbols[0], font=("Arial", fontsize))
                elif self.guess[iy][ix] == 1:
                    text = Label(self.w, text=symbols[1], font=("Arial", fontsize))
                elif self.guess[iy][ix] == 2:
                    text = Label(self.w, text=symbols[2], font=("Arial", fontsize))
                text.place(x=ix*dx+dx/2,y=iy*dx+dx/2)
                self.text_lab.append(text)
        mainloop()
    def newQuantum(self):
        print('not implemented')
    def solveClassic(self):
        print('not implemented')
    def solveInsp(self):
        print('not implemented')
    def solveQuantum(self):
        print('not implemented')


#region_grid, star_grid = generate_puzzle(N, S, annealer="leap", num_reads=100)
#solution_grid = solve_puzzle(N, nstars, region_grid, annealer="neal", num_reads=200)

    # leave patoLogic
    def exitProgram(self):
        exit()

if __name__ == "__main__":

    # Maximum and default grid size
    MAX_N=26;
    #grid,stars = genClass.generate_classic(N,S)

    symbols = ['','*','o']
    fontsize = 25

    # Set the whole thing running
    root = Tk()
    root.title("patoLogic") # Add a title
    grid = GridApp(root, 600, 600, 5)
    # Don't allow resizing in the x or y direction
    p1 = PhotoImage(file = 'duck2.png')
    # Icon set for program window
    root.iconphoto(False, p1)
    root.resizable(0,0)
    root.mainloop()
