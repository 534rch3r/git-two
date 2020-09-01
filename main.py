import tkinter as tk

window = tk.Tk()
#tutorial: root = Tk()

def button1_click():
    label_button1 = tk.Label(text="label_button1")
    label_button1.pack()


#label1 = tk.Label(text="label1").grid(row=0, column=0)
#label2 = tk.Label(text="label2").grid(row=1, column=5)
#label3 = tk.Label(text="label3").grid(row=2, column=3)
#tutorial: label = Label(root, text="Hello world")
#label1.grid(row=0, column=0)
#label2.grid(row=1, column=5)
#label3.grid(row=2, column=3)

label1 = tk.Label(text="label1")
label2 = tk.Label(text="label2")
label3 = tk.Label(text="label3")

button1 = tk.Button(text="button1", 
#state=tk.DISABLED,
command=button1_click,padx=50, pady=50, fg="blue", bg="red")
#command=button1_click,padx=50, pady=50).grid(row=3, column=4)
#tutorial: button1 = Button(root,text="button1", state=DISABLED)

button1.pack()
label1.pack()
label2.pack()
label3.pack()

'''
window.mainloop() tells Python to run the Tkinter event loop.
This method listens for events, such as button clicks or keypresses,
and blocks any code that comes after it from running until the window it’s
called on is closed. Go ahead and close the window you’ve created,
and you’ll see a new prompt displayed in the shell.
'''
window.mainloop()
#tutorial: root.mainloop()
