from tkinter import *
from PIL import Image,ImageTk
from tkinter import filedialog
from tkinter.messagebox import showinfo
from tkinter.filedialog import askopenfilename, asksaveasfilename
import os

#funcitons
def new():
    global file
    screen.title("Untitled - Notepad")
    file = None
    text.delete(1.0, END)

def openFile():
    global file
    file = askopenfilename(defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
    if file == "":
        file = None
    else: 
        screen.title(os.path.basename(file) + " - Notepad")
        text.delete(1.0, END)
        f = open(file, "r")
        text.insert(1.0, f.read())
        f.close()

def save():
    global file
    if file == None:
        file = asksaveasfilename(initialfile = 'Untitled.txt', defaultextension=".txt", filetypes=[("All Files", "*.*"), ("Text Documents", "*.txt")])
        if file == "":
            file = None
        else:
            f = open(file, "w")
            f.write(text.get(1.0, END))
            f.close()
            screen.title(os.path.basename(file) + " - Notepad")
            
    else:
        f = open(file, "w")
        f.write(text.get(1.0, END))
        f.close()

def addImage():
    global file
    file = filedialog.askopenfilename(initialdir=os.getcwd(),title="Select Image File",filetypes=(("JPG file","*.jpg"),("PNG file","*.png"),("All file","*.*")))
    img = Image.open(file)
    img = ImageTk.PhotoImage(img)
    l.configure(image=img)
    l.image = img

def exitApp():
    screen.destroy()

def cut():
    text.event_generate(("<<Cut>>"))

def copy():
    text.event_generate(("<<Copy>>"))

def paste():
    text.event_generate(("<<Paste>>"))

def about():
    showinfo("Notepad", "Notepad by Apoorva Chaddha")



if __name__ == '__main__':
    screen = Tk()
    screen.title("Unititled - Notepad")
    #add image
    screen.geometry("644x788")

    #Textarea
    text = Text(screen, font="lucida 13")
    file = None 
    text.pack(expand=True, fill=BOTH)

    #Menubar
    menu = Menu(screen)
    
    #file menu
    FileMenu = Menu(menu, tearoff=0)
    FileMenu.add_command(label="New", command=new)
    FileMenu.add_command(label="Open", command=openFile)
    FileMenu.add_command(label="Save", command=save)
    FileMenu.add_command(label="Add Image", command=addImage)
    FileMenu.add_separator()
    FileMenu.add_command(label="Exit", command=exitApp)
    menu.add_cascade(label="File", menu=FileMenu)
    
    #format menu
    FormatMenu = Menu(menu, tearoff=0)
    FontSubMenu = Menu(FormatMenu, tearoff=0)
    FontSubMenu.add_command(label="Arial", command=lambda: text.config(font="Arial"))
    FontSubMenu.add_command(label="Courier", command=lambda: text.config(font="Courier"))
    FontSubMenu.add_command(label="Times", command=lambda: text.config(font="Times"))
    FormatMenu.add_cascade(label="Font", menu=FontSubMenu)

    SizeSubMenu = Menu(FormatMenu, tearoff=0)
    SizeSubMenu.add_command(label="10", command=lambda: text.config(font=("TkDefaultFont", 10)))
    SizeSubMenu.add_command(label="12", command=lambda: text.config(font=("TkDefaultFont", 12)))
    SizeSubMenu.add_command(label="14", command=lambda: text.config(font=("TkDefaultFont", 14)))
    SizeSubMenu.add_command(label="16", command=lambda: text.config(font=("TkDefaultFont", 16)))
    SizeSubMenu.add_command(label="18", command=lambda: text.config(font=("TkDefaultFont", 18)))
    SizeSubMenu.add_command(label="20", command=lambda: text.config(font=("TkDefaultFont", 20)))
    FormatMenu.add_cascade(label="Font Size", menu=SizeSubMenu)

    menu.add_cascade(label="Format", menu=FormatMenu)
    
    #edit menu
    EditMenu = Menu(menu, tearoff=0)
    EditMenu.add_command(label="Cut", command=cut)
    EditMenu.add_command(label="Copy", command=copy)
    EditMenu.add_command(label="Paste", command=paste)
    menu.add_cascade(label="Edit", menu=EditMenu)

    #help menu
    HelpMenu = Menu(menu, tearoff=0)
    HelpMenu.add_command(label="About", command=about)
    menu.add_cascade(label="Help", menu=HelpMenu)

    #scrollbar
    Scroll = Scrollbar(text)
    Scroll.pack(side=RIGHT, fill=Y)
    Scroll.config(command=text.yview)
    text.config(yscrollcommand=Scroll.set)

    l=Label(screen)
    l.pack()

    screen.config(menu=menu)

    screen.mainloop()
