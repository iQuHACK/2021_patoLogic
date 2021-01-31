# 
import sys
from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from PIL import Image, ImageTk
import numpy as np
import matplotlib.pyplot as plt

# Maximum and default grid size
MAX_N, DEFAULT_N = 26, 10
# The "default" colour for an unfilled grid cell
UNFILLED = '#fff'

guess_stars = np.array([[0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 0, 1],
       [0, 0, 0, 1, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 1, 0, 0, 0, 0],
       [0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
       [0, 0, 1, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 1, 0, 0, 0],
       [1, 0, 0, 0, 0, 0, 0, 0, 0, 0],
       [0, 0, 0, 0, 0, 0, 0, 0, 1, 0]])

class GridApp:
    """The main class representing a grid of coloured cells."""

    # The colour palette
    colours = (UNFILLED, 'red', 'green')
    ncolours = len(colours)

    def __init__(self, master, n, width=600, height=600, pad=5):
        """Initialize a grid and the Tk Frame on which it is rendered."""

        # Number of cells in each dimension.
        self.n = n
        # Some dimensions for the App in pixels.
        self.width, self.height = width, height
        palette_height = 40
        # Padding stuff: xsize, ysize is the cell size in pixels (without pad).
        npad = n + 1
        self.pad = pad
        xsize = (width - npad*pad) / n
        ysize = (height - npad*pad) / n
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
        img = Label(self.w, image=render)
        img.image = render
        img.place(x=0, y=0)


        # Add labels
        self.text_lab = []
        dx = 600/n
        print(dx)
        for iy in range(0,n):
            for ix in range(0,n):
                if guess_stars[iy][ix] == 1:
                    text = Label(self.w, text="*")
                else:
                    text = Label(self.w, text=".")
                text.place(x=ix*dx+dx/2,y=iy*dx+dx/2)

                """
                duck = Image.open('duck_icon.png')
                duck = duck.resize((int(0.5*600/10), int(0.5*600/10)), Image.ANTIALIAS)
                my_img = ImageTk.PhotoImage(duck)
                text = Label(self.w, image = my_img)
                text.place(x=ix*dx+dx//4,y=iy*dx+dx//4)
                #text.pack()
                """

                #duck=PhotoImage(file='duck_icon.png')
                #text = Label(self.w,image=duck,bg='grey').pack()
                
                #img = Image.open('duck_icon.png')
                #self.tkimage = ImageTk.PhotoImage(img)
                #text = Label(self,image = self.tkimage).place(x=0, y=0, relwidth=1, relheight=1)

                #text = self.w.create_text((ix*dx, iy*dx), text="*")
                #rect = self.palette_canvas.create_rectangle(x, y, x+p_width, y+p_height, fill=self.colours[i])
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
            if ix < n and iy < n and 0 < xc < xsize and 0 < yc < ysize:
                i = iy*n+ix
                print(i)
                self.text_lab[i].config(text='')
        # Bind the grid click callback function to the left mouse button
        # press event on the grid canvas.
        img.bind('<ButtonPress-1>', w_click_callback)

    def _get_cell_coords(self, i):
        """Get the <letter><number> coordinates of the cell indexed at i."""
        # The horizontal axis is labelled A, B, C, ... left-to-right;
        # the vertical axis is labelled 1, 2, 3, ... bottom-to-top.
        iy, ix = divmod(i, self.n)
        return '{}{}'.format(chr(ix+65), self.n-iy)

# Get the grid size from the command line, if provided
try:
    n = int(sys.argv[1])
except IndexError:
    n = DEFAULT_N
except ValueError:
    print('Usage: {} <n>\nwhere n is the grid size.'.format(sys.argv[0]))
    sys.exit(1)
if n < 1 or n > MAX_N:
    print('Minimum n is 1, Maximum n is {}'.format(MAX_N))
    sys.exit(1)

# Set the whole thing running
root = Tk()
root.title("patoLogic")     # Add a title
grid = GridApp(root, n, 600, 600, 5)
# Don't allow resizing in the x or y direction
#root.resizable(0, 0)

root.mainloop()
