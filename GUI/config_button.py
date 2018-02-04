from tkinter import *
widget = Button(text= 'Vasuki',padx=10,pady=10)
widget.pack(padx=10,pady=10)
widget.config(cursor='gumby')
widget.config(bd=5,relief=RAISED)
widget.config(bg='blue',fg='black')
widget.config(font=('helvetica',20))
mainloop()
