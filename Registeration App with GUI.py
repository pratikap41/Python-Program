from tkinter import *
list1 = []

def reg(mvariables):
    print(name(name.get()))
  
def registeration_window():
    reg_window = first_window()
    reg_window.title('REGISTERATION')
    reg_window.geometry('320x250+200+200')
    reg_window.entry()
    reg_window.label2()
    Register = Button(reg_window, text = 'REGISTER', fg='green', bd=8, relief=RAISED, anchor=N, command=reg).grid(row=4, columnspan=2, sticky='nsew')
 
    
    


class first_window(Tk):
    def __init__(self):
        super().__init__()
        self.title("WELCOME")
        self.geometry('275x144+400+400')
        globals().update(locals())
    
    def button(self, **width ):
        reg_but = Button(text='Register', relief=RAISED, bd=5, **width, fg='green', command=registeration_window).grid(row=1, column=0, sticky=N)
        info_but = Button(text = 'Information', relief=RAISED, bd=5, **width, fg='black').grid(row=2, column=0 )
        globals().update(locals())
    
    def label(self):
        greet_label  =  Label(text='WELCOME TO HOTEL TAJ', font=('arial',15,'bold'), relief=GROOVE, bd= 10, fg='orange').grid( row=0, column=0)
        globals().update(locals())
    
    def entry(self):
        name = StringVar()
     
        name_entry = Entry(self, textvariable=name).grid(row=1, column=1, ipadx=20)
        last_entry = Entry(self).grid(row=2, column=1, ipadx=20)
        room_entry = Entry(self).grid(row=3, column=1, ipadx=20)

        a = name.get()
        globals().update(locals())
    
    def label2(self):
        reg_label = Label(self, text = " REGISTRATION" , relief = SUNKEN, font = ('arial',15,'bold'), bg = 'powder blue', fg ='red').grid(row=0, columnspan=2, sticky='nsew')
        name_label = Label(self, text='First Name : ' ).grid(row=1, column=0, sticky=E, ipadx=30, ipady=20)
        last_label = Label(self, text='Last Name : ').grid(row=2, column=0, sticky=E, ipadx=30, ipady=20)
        room_label= Label(self, text='Room Number : ').grid(row=3, column=0, sticky=E, ipadx=30, ipady=20)
        
        
window = first_window()
window.button(width=20, bg="powder blue" )
window.label()


