from tkinter import *
from tkinter import ttk
from tkinter import messagebox


class App(Tk):
    def __init__(self, *args, **kwargs):
        Tk.__init__(self, *args, **kwargs)

        container = Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (StartPage, AgreePage, Calculator):  #####for loop

            frame = F(container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky=NSEW)
        self.show_frame(StartPage)

    def show_frame(self, page):
        frame = self.frames[page]
        frame.tkraise()


class StartPage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        name_l = Label(self, text='Attendence-PRO', font=('arial', 20, 'bold'), fg='light steelblue3')
        name_l.grid(row=0, column=0, sticky=NW, ipady=30)
        calculator_b = ttk.Button(self, text='Attendence Calculator', width=20,
                                  command=lambda: controller.show_frame(AgreePage))
        calculator_b.grid(row=1, column=0, ipady=2, ipadx=10, sticky=N, )
        predictor_b = ttk.Button(self, text='Attendence Predictor', width=20)
        predictor_b.grid(row=2, column=0, ipady=2, ipadx=10, sticky=N, pady=10)
        exit_b = ttk.Button(self, text='Exit', width=20, command=exit)
        exit_b.grid(row=3, column=0, ipady=2, ipadx=10, sticky=N, pady=0)


class AgreePage(Frame):
    def __init__(self, parent, controller):
        Frame.__init__(self, parent)

        term_l = Label(self, text='Terms And Condition', font=('arial ', 14, 'bold'), pady=20)
        term_l.grid(row=1, column=0, sticky=NSEW)
        war_l = Label(self, text='''1. Calculated Attendence values are
approximate values.
2. Actual Attendence may vary according
to calculation scheme.
3. Attendence is calculated using simple
average and percent methods.
''', pady=50)
        back_b = Button(self, text='< Back ', fg='red', command=lambda: controller.show_frame(StartPage))
        back_b.grid(row=0, column=0, sticky=NW)
        agree_b = Button(self, text='Agree > ', bg='green', fg='mint cream',
                         command=lambda: controller.show_frame(Calculator))
        agree_b.grid(row=2, column=0, sticky=S)
        war_l.grid(row=2, column=0)


class Calculator(Frame):

    def __init__(self, parent, controller):
        Frame.__init__(self, parent)
        back_b = Button(self, text='< Back ', fg='red', command=lambda: controller.show_frame(AgreePage))
        back_b.grid(row=0, column=0, sticky=NW)
        tot_lect = IntVar()
        attended_lect = IntVar()
        weekly_att_list = []
        e1 = InputBox(self).grid()

        print(type(self.e1))

        def result(self):
            if (tot_lect.get() == 0):
                messagebox.showinfo('Error', 'Entrys Not Filled')
            else:
                att_per = (attended_lect.get() / tot_lect.get()) * 100
                weekly_att_list.append(att_per)
                print(weekly_att_list)

        ##                att_per =  (attended_lect.get()/ tot_lect.get())*100
        ##                messagebox.showinfo('RESULT', ('Your Attendence is %d Percent' %att_per))
        ##
        def nextweek(self, parent, controller):

            att_per = (attended_lect.get() / tot_lect.get()) * 100
            weekly_att_list.append(att_per)

            print(type(self))
            print(type(parent))
            print(type(controller))
            print(weekly_att_list)

        ##        week = IntVar()
        ##
        ##
        ##        week_e = ttk.Entry(self, textvariable = week ).grid(row=2, column=0, sticky = W)
        ##        week_l = Label (self, text = '1. Week : ', font = ('arial', 10, 'bold')).grid(row=1, column=0, sticky = W)
        ##        tot_lect_e = Entry(self, textvariable = tot_lect ).grid(row=4, column=0, sticky = W)
        ##
        ##        tot_lect_l = Label (self, text = '2. Total Lecture conducted : ', font = ('arial', 10, 'bold')).grid(row=3, column=0, sticky = W)
        ##        attended_lect_e = Entry(self, textvariable = attended_lect ).grid(row=6, column=0, sticky = W)
        ##        attended_lect_l = Label (self, text = '3. Total Lecture Attended : ', font = ('arial', 10, 'bold')).grid(row=5, column=0, sticky = W)
        ##
        ##        nextweek_b = Button(self, text='Next Week', command = lambda:nextweek(self, parent ,controller)).grid(row=7, column=0)
        ##
        ##        calculate_b = Button(self, text=' Calculate', command= lambda :result(self)).grid(row=8, column=0)
        ##
        globals().update(locals())


class InputBox(Entry):
    def __init__(self, *args, **kwargs):
        Entry.__init__(self, *args, **kwargs)
        a = self.delete(0, END)


class buttons(Button):
    def __init__(self, *args, **kwargs):
        Button.__init__(self, *args, **kwargs)


class labels(Label):
    def __init__(self, *args, **kwargs):
        Label.__init__(self, *args, **kwargs)


app = App()
app.title('Attendence-PRO')
app.geometry('225x350+100+100')
app.mainloop()
