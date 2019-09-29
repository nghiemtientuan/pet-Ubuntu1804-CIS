import sys
import os
section_path = os.path.dirname(os.path.realpath(__file__)) + '/section'
sys.path.append(section_path)

try:
    from Tkinter import *
    from ttk import *
except ImportError:  # Python 3
    from tkinter import *
    from tkinter.ttk import *
import time
from general import *

TILTE_APP = 'Ubuntu benchmark'

class App(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.progress = Progressbar(parent, orient = HORIZONTAL, length = 400, mode = 'determinate')
        self.TittleApp(parent)
        self.CreateUI()
        self.LoadTable()
        self.grid(sticky = (N, S, W, E))
        parent.grid_rowconfigure(0, weight = 1)
        parent.grid_columnconfigure(0, weight = 1)

    def bar(self, parent):
        self.progress['value'] = 20
        parent.update_idletasks()
        time.sleep(0.1)

        self.progress['value'] = 40
        parent.update_idletasks()
        time.sleep(0.1)

        self.progress['value'] = 100
        parent.update_idletasks()

    def TittleApp(self, parent):
        self.label = Label(parent, text=TILTE_APP, width=20, font=("bold", 20))
        self.label.place(x=100, y=20)

        self.var1 = IntVar()
        Checkbutton(parent, text="fix bugs", variable=self.var1).place(x=150, y=65)

        self.buttonRun = Button(parent, text='Run', width=20, command=lambda: self.bar(parent))
        self.buttonRun.place(x=100,y=100)
        self.progress.place(x=100,y=150)

    def CreateUI(self):
        tv = Treeview(self)
        tv['columns'] = ('time', 'status')
        tv.heading("#0", text = 'Name', anchor = 'w')
        tv.column("#0", anchor = "w", width = 500)
        tv.heading('time', text = 'Time')
        tv.column('time', anchor = 'center', width = 150)
        tv.heading('status', text = 'Status')
        tv.column('status', anchor = 'center', width = 150)
        tv.grid(pady=(200, 0), sticky = (N, S, W, E))
        self.treeview = tv
        self.grid_rowconfigure(0, weight = 1)
        self.grid_columnconfigure(0, weight = 1)

    def LoadTable(self):
        self.treeview.insert('', 'end', text = "First", values = ('10:10', 'Ok'))

def main():
    root = Tk()
    root.title(TILTE_APP)
    App(root)
    root.mainloop()

if __name__ == '__main__':
    main()