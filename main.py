from os import lseek
from tkinter import *
from tkinter.ttk import *
from tkinter.filedialog import askopenfilenames
import time
from resume_parser import resumeparse
lseek
ws = Tk()
ws.title('Resume parser')
ws.geometry('400x200') 

adhar = Label(
    ws, 
    text='Upload Government id in jpg format '
    )
adhar.grid(row=0, column=0, padx=10)


def open_file():
    file_paths = askopenfilenames(title='Choose a file', multiple=True)
    if file_paths is not None:
        for file_path in file_paths:
            print(resumeparse.read_file(file_path))
    else:
        pass



def uploadFiles():
    pb1 = Progressbar(
        ws, 
        orient=HORIZONTAL, 
        length=300, 
        mode='determinate'
        )
    pb1.grid(row=4, columnspan=3, pady=20)
    for i in range(5):
        ws.update_idletasks()
        pb1['value'] += 20
        time.sleep(1)
    pb1.destroy()
    Label(ws, text='File Uploaded Successfully!', foreground='green').grid(row=4, columnspan=3, pady=10)
        
    
    


adharbtn = Button(
    ws, 
    text ='Choose File', 
    command = lambda:open_file()
    ) 
adharbtn.grid(row=0, column=1)

upld = Button(
    ws, 
    text='Upload Files', 
    command=uploadFiles
    )
upld.grid(row=3, columnspan=3, pady=10)



ws.mainloop()