from tkinter import *
import time
import datetime
#=====================register function============================================


    
list_name = []
list_last = []
list_room = []
list_mob = []
list_adhar = []
list_fullname = []
    
def registration():
    
            textbox.delete(1.0,END)
            
            if (name.get().isalpha() and last.get().isalpha() and room.get().isdigit() and room.get() < '50' and room.get() > '0'  and mob.get().isdigit() and len(mob.get()) == 10 and adhar.get().isdigit() and len(adhar.get()) == 12 ):
               list_name.append(name.get())
               list_last.append(last.get())
               list_room.append(room.get())
               list_mob.append(mob.get())
               list_adhar.append(adhar.get())
               fullname = name.get().upper() + '   '  + last.get().upper()
               list_fullname.append(fullname)
               listbox.insert(0,fullname)
            else:
                textbox.delete(1.0,END)
                textbox.insert(1.0,'INVALID REGISTRATION')
                textbox.configure(fg='red')
          
            name_entry.delete(0,END)
            last_entry.delete(0,END)
            room_entry.delete(0,END)
            mob_entry.delete(0,END)
            adhar_entry.delete(0,END)
    
            globals().update(locals())
    
def textbox_entry(event):
    textbox.delete(1.0,END)
    x = listbox.get(ACTIVE)
    textbox.configure(fg='black') 
    for i in list_fullname:
        if(i==x):
            ind= list_fullname.index(i)
            textbox.insert(1.0,('''ROOM NUMBER - %s
FIRST NAME  -  %s
LAST NAME   -  %s
MOBILE NUMBER - %s
ADHAR NUMBER  -  %s
''')%(list_room[ind], list_name[ind].upper(), list_last[ind].upper(), list_mob[ind], list_adhar[ind]))



#=====================window setup ==============================================

window = Tk()
window.title("GRAND HYATT ")
window.configure(bg='black')
window.geometry('1080x720+0+0')

#frames
f_header = Frame(window, width=1080, height=100, bd=16, relief=GROOVE, bg='powder blue', cursor='heart')
f_reg = Frame(window, width=600, height=620, bd=10, relief=SUNKEN, bg = "grey70", cursor='cross')
f_info = Frame(window, width=480, height=620, bd=10, relief = RAISED, bg='lavender', cursor='hand2')

f_header.grid(row=0, columnspan=2)
f_reg.grid(row=1, column=0, sticky=W)
f_info.grid(row=1, column=1)

#labels
greet_label = Label(f_header, text="*** WELCOME TO GRAND HYATT ***", font=("arial",45,"bold"), fg='orange')
reg_label = Label(f_reg, text='REGISTRATION ', font=('arial',30,'bold'),bg='light green', fg='red', relief=GROOVE, bd=5)
name_label = Label(f_reg, text='First Name :', font=('arial',20), bg='grey70')
last_label = Label(f_reg, text='Last Name :', font=('arial',20), bg='grey70')
room_label = Label(f_reg, text='Room Number :', font=('arial',20), bg='grey70')
mob_label = Label(f_reg, text='Mobile Number :', font=('arial',20), bg='grey70')
adhar_label = Label(f_reg, text='Adhar Number :', font=('arial',20), bg='grey70')

greet_label.grid(row=0,column=0, sticky='nsew')
name_label.grid(row=1, column=0, sticky=E, ipadx=40, ipady=20)
last_label .grid(row=2, column=0, sticky=E, ipadx=40, ipady=20)
room_label.grid(row=3, column=0, sticky=E, ipadx=40, ipady=20)
mob_label.grid(row=4, column=0, sticky=E, ipadx=40, ipady=20)
adhar_label.grid(row=5, column=0, sticky=E, ipadx=40, ipady=20)
reg_label.grid(row=0, columnspan=2, sticky=NSEW, ipadx=60, ipady=30)



#entry
name = StringVar()
last = StringVar()
room = StringVar()
mob = StringVar()
adhar = StringVar()


name_entry = Entry(f_reg, textvariable=name, font=('arial', 13))
last_entry = Entry(f_reg, textvariable=last, font=('arial', 13))
room_entry = Entry(f_reg, textvariable=room, font=('arial', 13))
mob_entry = Entry(f_reg, textvariable=mob, font=('arial', 13))
adhar_entry = Entry(f_reg, textvariable=adhar, font=('arial', 13))


name_entry.grid(row=1, column=1, ipadx=40, ipady=10)
last_entry.grid(row=2, column=1, ipadx=40, ipady=10)
room_entry.grid(row=3, column=1, ipadx=40, ipady=10)
mob_entry.grid(row=4, column=1, ipadx=40, ipady=10)
adhar_entry.grid(row=5, column=1, ipadx=40, ipady=10)

#button
reg_but = Button(f_reg, text='REGISTER', bd=10, relief=RAISED, font=('arial',15,'bold'), fg='green', cursor='hand2', command=registration)

reg_but.grid(row=6,columnspan=2, ipadx=20, ipady=15, sticky='nsew')

#listbox

listbox = Listbox(f_info, width=53, height=20,  font=('arial', 13))
listbox.grid(row=0,column=0, sticky=N)
listbox.bind('<Button-3>',textbox_entry)


#textbox
textbox = Text(f_info, width=53, height=9,  font=('arial', 13))
textbox.grid(row=1,column=0)







window.mainloop()
