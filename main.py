import tkinter as tk
from PIL import ImageTk,Image   
#import pathlib

window = tk.Tk()
#tutorial: root = Tk()
calc_variable1,calc_variable2 = 0,0
math_action = ""
img_number_imgViewerApp = 1

def images():
    #global window

    #https://www.freeimages.com/photographer/watford-39012
    img = Image.open(r"C:\Users\hencis\Desktop\stuff\software_data_projects_and_other_all\Images\freeimages\FreeImages_comContentLicense\new-zealand-ferns-1178495.jpg")
    img = img.resize((400, 400))
    window.img = ImageTk.PhotoImage(img)
    #img  = ImageTk.PhotoImage(Image.open(r"C:\Users\hencis\Desktop\stuff\software_data_projects_and_other_all\Images\freeimages\FreeImages_comContentLicense\new-zealand-ferns-1178495.jpg"))
    label4 = tk.Label(image=window.img)
    #label4.place(x=0, y=0, relwidth=1, relheight=1)

    button_quit = tk.Button(text="Exit program",command=window.quit,padx=20, pady=20, fg="black", bg="white", borderwidth=3)
 
    label4.pack()
    button_quit.pack()   

def imageViewer():
    global button_back
    global button_exit
    global button_forward
    global label4    
    global img_list
    global img_number_imgViewerApp
    global statusBar

    #img1 = Image.open(r"C:\Users\hencis\Desktop\stuff\software_data_projects_and_other_all\Images\freeimages\FreeImages_comContentLicense\new-zealand-ferns-1178495.jpg").resize(400, 400)
    #img2 = Image.open(r"C:\Users\hencis\Desktop\stuff\software_data_projects_and_other_all\Images\freeimages\FreeImages_comContentLicense\ferns-3-1405636.jpg")
    #img3 = Image.open(r"C:\Users\hencis\Desktop\stuff\software_data_projects_and_other_all\Images\freeimages\FreeImages_comContentLicense\ir-fern-frond-1372220.jpg")
    #img4 = Image.open(r"C:\Users\hencis\Desktop\stuff\software_data_projects_and_other_all\Images\freeimages\FreeImages_comContentLicense\on-the-fern-1409420.jpg")
   
    window.img1 = ImageTk.PhotoImage(Image.open(r"C:\Users\hencis\Desktop\stuff\software_data_projects_and_other_all\Images\freeimages\FreeImages_comContentLicense\new-zealand-ferns-1178495.jpg").resize((500, 500)))
    window.img2 = ImageTk.PhotoImage(Image.open(r"C:\Users\hencis\Desktop\stuff\software_data_projects_and_other_all\Images\freeimages\FreeImages_comContentLicense\ferns-3-1405636.jpg").resize((400, 400)))
    window.img3 = ImageTk.PhotoImage(Image.open(r"C:\Users\hencis\Desktop\stuff\software_data_projects_and_other_all\Images\freeimages\FreeImages_comContentLicense\ir-fern-frond-1372220.jpg").resize((300, 300)))
    window.img4 = ImageTk.PhotoImage(Image.open(r"C:\Users\hencis\Desktop\stuff\software_data_projects_and_other_all\Images\freeimages\FreeImages_comContentLicense\on-the-fern-1409420.jpg").resize((100, 100))) 
    window.img5 = ImageTk.PhotoImage(Image.open(r"C:\Users\hencis\Desktop\stuff\software_data_projects_and_other_all\Images\freeimages\FreeImages_comContentLicense\the-road-through-the-woods-1449194.jpg").resize((250, 250))) 
    window.img6 = ImageTk.PhotoImage(Image.open(r"C:\Users\hencis\Desktop\stuff\software_data_projects_and_other_all\Images\freeimages\FreeImages_comContentLicense\shore-1385226.jpg").resize((150, 150))) 
    window.img7 = ImageTk.PhotoImage(Image.open(r"C:\Users\hencis\Desktop\stuff\software_data_projects_and_other_all\Images\freeimages\FreeImages_comContentLicense\bottoms-up-1363459.jpg").resize((450, 450))) 
    img_list = [window.img1,window.img2,window.img3,window.img4,window.img5,window.img6,window.img7]

    #window.img1 = ImageTk.PhotoImage(Image.open(r"C:\Users\hencis\Desktop\stuff\software_data_projects_and_other_all\Images\freeimages\FreeImages_comContentLicense\new-zealand-ferns-1178495.jpg").resize((800, 800)))
    #img1 = img1.resize((400, 400))
    #window.img1 = ImageTk.PhotoImage(img1)
    '''
    list = [1, 3, 5, 7, 9] 
    # getting length of list 
    length = len(list) 
    
    # Iterating the index 
    # same as 'for i in range(len(list))' 
    for i in range(length): 
        print(list[i]) 
    '''
    statusBar = tk.Label(text="Image [" + str(img_number_imgViewerApp+1) + "] of " + str(len(img_list)), bd=2, 
    relief=tk.RIDGE, anchor=tk.W
    )

    label4 = tk.Label(image=window.img2)
    label4.grid(row=0,column=0,columnspan=3)
    
    button_back = tk.Button(text="<",command=lambda: back(img_number_imgViewerApp))
    button_exit = tk.Button(text="Exit",command=window.quit)
    button_forward = tk.Button(text=">",command=lambda: forward(img_number_imgViewerApp))

    button_back.grid(row=1,column=0)
    button_exit.grid(row=1,column=1)
    button_forward.grid(row=1,column=2,pady=5)
    statusBar.grid(row=2,column=0,columnspan=3,sticky=tk.W+tk.E)

def forward(img_number):
    global label4
    global button_forward
    global img_list
    global img_number_imgViewerApp
    global statusBar

    img_number_imgViewerApp = img_number

    if(img_number_imgViewerApp == 6):
        button_forward = tk.Button(text=">",command=lambda: forward(img_number_imgViewerApp), state=tk.DISABLED)   
    elif(img_number_imgViewerApp < 6 and img_number_imgViewerApp >= 0):
        #img_number_imgViewerApp = img_number + 1

        label4.grid_forget()
        
        img_number_imgViewerApp = img_number + 1
        label4 = tk.Label(image=img_list[img_number_imgViewerApp])
        label4.grid(row=0,column=0,columnspan=3)

        print("len(img_list): ",len(img_list))

        #complete update
        button_forward = tk.Button(text=">",command=lambda: forward(img_number_imgViewerApp))
        button_forward.grid(row=1,column=2)

        statusBar = tk.Label(text="Image [" + str(img_number+2) + "] of " + str(len(img_list)), bd=2, 
        relief=tk.RIDGE, anchor=tk.W
        )
        statusBar.grid(row=2,column=0,columnspan=3,sticky=tk.W+tk.E)
        
        #print(globals())
        
def back(img_number):
    global label4
    global button_back
    global img_list
    global img_number_imgViewerApp
    global statusBar

    img_number_imgViewerApp = img_number

    if(img_number_imgViewerApp == 0):
        button_back = tk.Button(text="<",command=lambda: back(img_number_imgViewerApp), state=tk.DISABLED)   
    elif(img_number_imgViewerApp > 0 and img_number_imgViewerApp <= 6):
        
        label4.grid_forget()
        
        #if(img_number<)
        img_number_imgViewerApp = img_number - 1
        label4 = tk.Label(image=img_list[img_number_imgViewerApp])
        label4.grid(row=0,column=0,columnspan=3)

        print("len(img_list): ",len(img_list))
        
        #complete update
        button_back = tk.Button(text="<",command=lambda: back(img_number_imgViewerApp))
        button_back.grid(row=1,column=0)
        
        statusBar = tk.Label(text="Image [" + str(img_number) + "] of " + str(len(img_list)), bd=2, 
        relief=tk.RIDGE, anchor=tk.W
        )
        statusBar.grid(row=2,column=0,columnspan=3,sticky=tk.W+tk.E)
        
        #print(globals())
    
def initial_program():
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
    command=button1_click,padx=50, pady=50, fg="blue", bg="red", borderwidth=10)
    #command=button1_click,padx=50, pady=50).grid(row=3, column=4)
    #tutorial: button1 = Button(root,text="button1", state=DISABLED)

    entry = tk.Entry(fg="yellow", bg="blue", width=50, borderwidth=10)
    entry.insert(0, "Placeholder - Enter something...")

    button1.pack()
    label1.pack()
    label2.pack()
    label3.pack()
    entry.pack()

def button1_click():
    label_button1 = tk.Label(text="label_button1: " + entry.get())
    label_button1.pack()

def calculator():
    #https://www.iconfinder.com/icondesigner
    window.iconbitmap(r'c:\Users\hencis\Desktop\stuff\software_data_projects_and_other_all\Icons\iconfinder_website\iconfinder_Python_logo_282803.ico')
    
    global calc_button_multiply
    global calc_button_divide
    global calc_button_subtract
    global calc_button_raiseToThePowerOf

    calculator_entry = tk.Entry(fg="white", bg="black", borderwidth=5)
    calculator_entry.insert(0, "Calculator - enter something...")
    calc_button0 = tk.Button(text="0",command=lambda: button_calc_number(0),padx=20, pady=20, fg="black", bg="white", borderwidth=3)
    calc_button1 = tk.Button(text="1",command=lambda: button_calc_number(1),padx=20, pady=20, fg="black", bg="white", borderwidth=3)
    calc_button2 = tk.Button(text="2",command=lambda: button_calc_number(2),padx=20, pady=20, fg="black", bg="white", borderwidth=3)
    calc_button3 = tk.Button(text="3",command=lambda: button_calc_number(3),padx=20, pady=20, fg="black", bg="white", borderwidth=3)
    calc_button4 = tk.Button(text="4",command=lambda: button_calc_number(4),padx=20, pady=20, fg="black", bg="white", borderwidth=3)
    calc_button5 = tk.Button(text="5",command=lambda: button_calc_number(5),padx=20, pady=20, fg="black", bg="white", borderwidth=3)
    calc_button6 = tk.Button(text="6",command=lambda: button_calc_number(6),padx=20, pady=20, fg="black", bg="white", borderwidth=3)
    calc_button7 = tk.Button(text="7",command=lambda: button_calc_number(7),padx=20, pady=20, fg="black", bg="white", borderwidth=3)
    calc_button8 = tk.Button(text="8",command=lambda: button_calc_number(8),padx=20, pady=20, fg="black", bg="white", borderwidth=3)
    calc_button9 = tk.Button(text="9",command=lambda: button_calc_number(9),padx=20, pady=20, fg="black", bg="white", borderwidth=3)
    calc_button_add = tk.Button(text="+",command= button_calc_add,padx=20, pady=20, fg="black", bg="white", borderwidth=3)
    calc_button_equal = tk.Button(text="=",command=button_calc_equal,padx=20, pady=20, fg="black", bg="white", borderwidth=3)
    calc_button_clear = tk.Button(text="Clear",command=button_calc_clear,padx=20, pady=20, fg="black", bg="white", borderwidth=3)
    calc_button_multiply = tk.Button(text="*",command=calc_button_multiply,padx=20, pady=20, fg="black", bg="white", borderwidth=3)
    calc_button_divide = tk.Button(text="/",command=calc_button_divide,padx=20, pady=20, fg="black", bg="white", borderwidth=3)
    calc_button_subtract = tk.Button(text="-",command=calc_button_subtract,padx=20, pady=20, fg="black", bg="white", borderwidth=3)
    calc_button_raiseToThePowerOf = tk.Button(text="x^y",command=calc_button_raiseToThePowerOf,padx=20, pady=20, fg="black", bg="white", borderwidth=3)
    button_quit = tk.Button(text="Exit program",command=window.quit,padx=20, pady=20, fg="black", bg="white", borderwidth=3)
 
    calculator_entry.grid(row=0,column=0,padx=10,pady=10,columnspan=3)
    calc_button0.grid(row=4,column=0)
    calc_button1.grid(row=1,column=0)
    calc_button2.grid(row=1,column=1)
    calc_button3.grid(row=1,column=2) 
    calc_button4.grid(row=2,column=0)
    calc_button5.grid(row=2,column=1)
    calc_button6.grid(row=2,column=2)
    calc_button7.grid(row=3,column=0)
    calc_button8.grid(row=3,column=1)
    calc_button9.grid(row=3,column=2)
    calc_button_add.grid(row=4,column=1,columnspan=2)
    calc_button_multiply.grid(row=1,column=3)
    calc_button_divide.grid(row=2,column=3)
    calc_button_subtract.grid(row=3,column=3)
    calc_button_equal.grid(row=6,column=0,columnspan=3)
    calc_button_clear.grid(row=5,column=0,columnspan=3)
    calc_button_raiseToThePowerOf.grid(row=7,column=0,columnspan=3)
    button_quit.grid(row=0,column=10,rowspan=3)

def button_calc_number(number):
    # calculator_entry.delete(0,tk.END)
    current = calculator_entry.get()
    if (not current.isnumeric()):
        calculator_entry.delete(0, tk.END)   
        calculator_entry.insert(0,number) 
    elif(current.isnumeric()):
        calculator_entry.delete(0, tk.END)  
        calculator_entry.insert(0,str(current) + str(number))

def button_calc_clear():
    calculator_entry.delete(0, tk.END)

def button_calc_add():
    global math_action
    math_action = "add"
    global calc_variable1
    if(calculator_entry.get().isnumeric()):
        calc_variable1 = calculator_entry.get()
        calculator_entry.delete(0, tk.END)

def calc_button_multiply():
    global math_action
    math_action = "multiply"
    global calc_variable1
    if(calculator_entry.get().isnumeric()):
        calc_variable1 = calculator_entry.get()
        calculator_entry.delete(0, tk.END)

def calc_button_divide():
    global math_action
    math_action = "divide"
    global calc_variable1
    if(calculator_entry.get().isnumeric()):
        calc_variable1 = calculator_entry.get()
        calculator_entry.delete(0, tk.END)

def calc_button_subtract():
    global math_action
    math_action = "subtract"
    global calc_variable1
    if(calculator_entry.get().isnumeric()):
        calc_variable1 = calculator_entry.get()
        calculator_entry.delete(0, tk.END)

def calc_button_raiseToThePowerOf():
    global math_action
    math_action = "powerOf"
    global calc_variable1
    if(calculator_entry.get().isnumeric()):
        calc_variable1 = calculator_entry.get()
        calculator_entry.delete(0, tk.END)

def button_calc_equal():
    global math_action 
    if(math_action=="add"):
        calc_variable2 = calculator_entry.get()
        calculator_entry.delete(0, tk.END)
        print("type(calc_variable1): ",type(calc_variable1)) 
        print("calc_variable1: ",calc_variable1) 
        print("type(calc_variable2): ",type(calc_variable2)) 
        print("calc_variable2: ",calc_variable2) 
        calculator_entry.insert(0,float(calc_variable1) + float(calc_variable2))
    elif(math_action=="multiply"):
        calc_variable2 = calculator_entry.get()
        calculator_entry.delete(0, tk.END)
        print("type(calc_variable1): ",type(calc_variable1)) 
        print("calc_variable1: ",calc_variable1) 
        print("type(calc_variable2): ",type(calc_variable2)) 
        print("calc_variable2: ",calc_variable2) 
        calculator_entry.insert(0,float(calc_variable1) * float(calc_variable2))
    elif(math_action=="divide"):
        calc_variable2 = calculator_entry.get()
        calculator_entry.delete(0, tk.END)
        print("type(calc_variable1): ",type(calc_variable1)) 
        print("calc_variable1: ",calc_variable1) 
        print("type(calc_variable2): ",type(calc_variable2)) 
        print("calc_variable2: ",calc_variable2) 
        calculator_entry.insert(0,float(calc_variable1) / float(calc_variable2))
    elif(math_action=="subtract"):
        calc_variable2 = calculator_entry.get()
        calculator_entry.delete(0, tk.END)
        print("type(calc_variable1): ",type(calc_variable1)) 
        print("calc_variable1: ",calc_variable1) 
        print("type(calc_variable2): ",type(calc_variable2)) 
        print("calc_variable2: ",calc_variable2) 
        calculator_entry.insert(0,float(calc_variable1) - float(calc_variable2))
    elif(math_action=="powerOf"):
        calc_variable2 = calculator_entry.get()
        calculator_entry.delete(0, tk.END)
        print("type(calc_variable1): ",type(calc_variable1)) 
        print("calc_variable1: ",calc_variable1) 
        print("type(calc_variable2): ",type(calc_variable2)) 
        print("calc_variable2: ",calc_variable2) 
        calculator_entry.insert(0,float(calc_variable1) ** float(calc_variable2))

#calculator()
#images()
imageViewer()

'''
window.mainloop() tells Python to run the Tkinter event loop.
This method listens for events, such as button clicks or keypresses,
and blocks any code that comes after it from running until the window it’s
called on is closed. Go ahead and close the window you’ve created,
and you’ll see a new prompt displayed in the shell.
'''
window.mainloop()
#tutorial: root.mainloop()
