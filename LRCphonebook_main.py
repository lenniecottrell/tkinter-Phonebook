from tkinter import *
import tkinter as tk
from tkinter import messagebox

#import other modules to make sure we have them
import LRCphonebook_gui
import LRCphonebook_func

class ParentWindow(Frame):
    def __init__ (self, master, *args, **kwargs):
        Frame.__init__(self, master, *args, **kwargs)

        # define our master frame config
        self.master = master
        self.master.minsize(500,300) #(height, Width)
        self.master.maxsize(500,300)
        
        # This center_window method will center our app on the user's screen
        LRCphonebook_func.center_window(self,500,300)
        self.master.title("The Tkinter Phonebook")
        self.master.configure(bg='#F0F0F0')
        
        # This protocol method is a tkinter built-in method to catch if
        # the user clicks the upper corner, 'X' on Windows OS
        self.master.protocol('WM_DELETE_WINDOW', lambda: LRCphonebook_func.ask_quit(self))
        arg = self.master

        # load in the GUI widgets from a separate module
        # keeping your code compartmentalized and clutter free
        LRCphonebook_gui.load_gui(self)



if __name__ == "__main__":
    root = tk.Tk() #this is the syntax to call a tkinter window, put in the variable root
    App = ParentWindow(root) #instantiating a class of ParentWindow called "App"
    root.mainloop() #this keeps the window up until the user closes it




        
