# Multi Clipboard
# Version 0.1
# Author: Anand Shridhar

import pyperclip, shelve
from tkinter import *

class SaveLoadButton:
    def __init__(self, master, name, shelve_index):
        self.button = Button(master, text=name)
        self.button.pack()
        self.shelve_index = shelve_index
        self.button.bind('<Button-1>', self.save)
        self.button.bind('<Button-3>', self.load)
        self.button.bind('<Enter>', self.status_show)
        self.button.bind('<Leave>', self.status_hide)
              
    def save(self, event):
        clip_dict = shelve.open('mcb')
        clip_dict[str(self.shelve_index)] = pyperclip.paste()
        clip_dict.close()
        
    def load(self, event):
        clip_dict = shelve.open('mcb')
        self.button.config(relief=SUNKEN)
        self.button.after(100, lambda: self.button.config(relief = RAISED))
        try:
            pyperclip.copy(clip_dict[str(self.shelve_index)])
        except:
            pass
        finally:
            clip_dict.close()
    
    def status_show(self, event):
        global status_msg
        clip_dict=shelve.open('mcb')
        try: 
            status_string = clip_dict[str(self.shelve_index)]
            status_msg.set(status_string[:15].replace("\n", " ").replace("\r", " ") + '...')
        except:
            status_msg.set("Empty Clipboard")
        finally:
            clip_dict.close()
    
    def status_hide(self, event):
        global status_msg
        status_msg.set("")

root = Tk()
root.title('Anand\'s Clipboard')
save_frame = Frame(root)
save_frame.pack(side=TOP)
status_frame = Frame(root)
status_frame.pack(side=BOTTOM, fill=X)
status_msg = StringVar()
status_text = Label(status_frame, text='', textvariable=status_msg, bd=1, relief='sunken', anchor=W)
status_text.pack(fill=X, side=BOTTOM)
save_array = [SaveLoadButton(save_frame, 'Clipboard-'+str(i+1), i) for i in range(10) ]


root.mainloop()
    
    