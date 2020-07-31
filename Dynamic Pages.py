from tkinter import *
from tkinter import ttk

class App(Tk):
        def __init__(self, *args, **kwargs):
            Tk.__init__(self, *args, *kwargs)

            container = Frame(self)
            container.pack(side = 'top', fill = 'both', expand = True )
            container.grid_rowconfigure(0, weight = 1)
            container.grid_columnconfigure(0,weight=1)

            self.frames = {}
            for F in (StartPage, PageOne):
                
                frame = F(container , self)
                self.frames[F] = frame
                frame.grid(row =0, column=0, sticky=NSEW)
            self.show_frame(StartPage)
            
        def show_frame(self, page):
            frame = self.frames[page]
            frame.tkraise()
            
    
            
            
class StartPage(Frame):
    def __init__(self, parent, controller): 
        Frame.__init__(self, parent)
        
        label = ttk.Label(self, text = 'startpage')
        label.pack()
        button = ttk.Button(self, text='goto page one', command=lambda:controller.show_frame(PageOne))
        button.pack()

        
class PageOne(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        label = ttk.Label(self, text='page one ')
        label.pack()
        button = Button(self, text='Back to startpage', command=lambda:controller.show_frame(StartPage))
        button.pack()
        
app = App()
app.mainloop()
