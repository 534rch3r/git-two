import tkinter as tk

window = tk.Tk()
#root = Tk()

label1 = tk.Label(text="label1").grid(row=0, column=0)
label2 = tk.Label(text="label2").grid(row=1, column=5)
label3 = tk.Label(text="label3").grid(row=2, column=3)
#label = Label(root, text="Hello world")


#label1.grid(row=0, column=0)
#label2.grid(row=1, column=5)
#label3.grid(row=2, column=3)


#label1.pack()
#label2.pack()
#label.pack()



'''
window.mainloop() tells Python to run the Tkinter event loop.
This method listens for events, such as button clicks or keypresses,
and blocks any code that comes after it from running until the window it’s
called on is closed. Go ahead and close the window you’ve created,
and you’ll see a new prompt displayed in the shell.
'''
window.mainloop()
#root.mainloop()
