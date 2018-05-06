# brady maxwell 177245IVCM
# intro to python course
# home work 3 text Editor

from tkinter import *
from tkinter import filedialog
from tkinter import messagebox

root = Tk()
root.title("BEM Editor")
text=Text(root, font=("roboto", 12))
text.grid()
text.configure(bg='black',fg='white') # change colors of grid
def closeEditor():
    # todo later creat pop up to confirm close with save or close and discard
    root.quit()

def saveFile():
    global text # contents of the grid text
    fileName=filedialog.asksaveasfile(mode='w',defaultextension=".txt") # get name of file, later add options
    content=text.get("1.0",'end-1c') # from first character to last - 1 to avoid newline
    fileName.write(content) # write the content to the file
    fileName.close

def openFile():
    global text # contents of the grid text
    fileName = filedialog.askopenfilename(filetypes=[("Text files", "*.txt")])
    f = open(fileName, "r") # open the file
    fileContents = f.read()  # read in content of file
    text.delete(1.0, END) # clear the grid text
    text.insert(1.0, fileContents) # insert text into grid text from file


def askHelp():
    messagebox.showinfo("About", "BEM Editor V. 0.01 beta created by BEM at bem dot bem\n 24-04-2018")

# create menubar
menubar = Menu(root)
menubar.config(bg="black", fg="green")
# create File pulldown menu, and add it to the menu bar
filemenu = Menu(menubar, tearoff=0)
filemenu.add_command(label="Save to File", command=saveFile)
filemenu.add_command(label="Open a File", command=openFile)
filemenu.add_command(label="Close", command=closeEditor)
menubar.add_cascade(label="File", menu=filemenu)
# create Help pulldown menu, and add it to the menu bar
helpmenu = Menu(menubar, tearoff=0)
helpmenu.add_command(label="About", command=askHelp)
menubar.add_cascade(label="Help", menu=helpmenu)

root.config(menu=menubar)
root.mainloop()
