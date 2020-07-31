from  tkinter import *

list1 = []
class calculator(Tk):
    def __init__(self):
        super().__init__()
        self.title("Calculator")
        self.geometry('200x200+200+200')
        self.frame_op = Frame().pack(side='bottom')
        v=IntVar()
        self.entry = Entry( self, bd=10, relief = SUNKEN, textvariable=v)
        self.entry.pack( side = TOP, ipadx=360, ipady=10, fill='x')
        self.add_button = Button(self.frame_op , text='+', command=add).pack(side=LEFT, anchor='n', ipadx=40, ipady=10)
        self.equal_button = Button(self.frame_op , text='=', command= equal).pack(side='bottom' ,anchor='n', ipadx=20, ipady=10)
        self.clear_button = Button(self.frame_op , text='C', command= clear).pack(side=LEFT, anchor='n', ipadx=20, ipady=10)
        globals().update(locals())
        
        
            
def equal():
    list1.append(v.get())
    self.entry.delete(0,END)
    self.entry.insert(END,(list1[0], '+' ,list1[1]))
    list1.clear()


def clear():
            list1.clear()
            self.entry.delete(0,END)

        
def add():
        list1.append(v.get())
        self.entry.delete(0,END)

    



    



        

cal1 = calculator()

        
