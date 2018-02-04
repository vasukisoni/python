from tkinter import *
from tkinter.messagebox import *

def callback():
    if askyesno('Verify','Do you really want to quit ?'):
        showwarning('Yes', 'Quit no yet implemented')

    else:
        showinfo('No', 'Quit has been cancelled ! ')

errmsg = 'sorry no spam allowed'

Button(text='quit',command = callback).pack(fill=X)
Button(text = 'spam', command=(lambda: showerror('spam',errmsg))).pack(fill=X)
mainloop()
    
    
