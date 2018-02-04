#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      kanha
#
# Created:     17/02/2014
# Copyright:   (c) kanha 2014
# Licence:     <your licence>
#-------------------------------------------------------------------------------
from tkinter.filedialog   import askopenfilename        # get standard dialogs
from tkinter.colorchooser import askcolor               # they live in Lib\tkinter
from tkinter.messagebox   import askquestion, showerror
from tkinter.simpledialog import askfloat
demos = {
    'Open':  askopenfilename,
    'Color': askcolor,
    'Query': lambda: askquestion('Warning', 'You typed "rm *"\nConfirm?'),
    'Error': lambda: showerror('Error!', "He's dead, Jim"),
    'Input': lambda: askfloat('Entry', 'Enter credit card number')
}