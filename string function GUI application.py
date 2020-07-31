from  tkinter import *
from tkinter import messagebox

def exit():
    msgbox = messagebox.askquestion('EXIT','Do You Want To Exit ?')
    
    if(msgbox=="yes"):
            win.destroy()

def clear():
    textbox.delete(1.0,END)
    string_entry.delete(0,END)
    substring_entry.delete(0,END)
    extra_entry.delete(0,END)
#########################   LISTBOX FUNCTION   ############################################################################
def listbox_fun(event):
    extra_label.configure(text='    value : ')
    result_but.configure(command=None)
    textbox.delete(1.0,END)
    extra_entry.configure( textvariable=extra, state='disabled')
    substring_label.configure(text='  Enter Your Sub-String : ')
    substring_entry.configure(state='disabled')
    
    x = listbox.get(ACTIVE)
    
    if (x == 'Length'):                                                                                                                                         #length
        result_but.configure(command=length)
    elif(x == 'Isalpha'):                                                                                                                                       #isalpha
        result_but.configure(command=isalpha)
    elif(x == 'Isdigit'):                                                                                                                                         #isdigit
        result_but.configure(command=isdigit)
    elif(x == 'Isalnum'):                                                                                                                                      #isalnum
        result_but.configure(command=isalnum)
    elif(x == 'Isspace'):                                                                                                                                      #isspace
        result_but.configure(command=isspace)
    elif(x == 'Isupper'):                                                                                                                                     #isupper                                                                                                       
        result_but.configure(command=isupper)
    elif(x == 'Islower'):                                                                                                                                      #islower
        result_but.configure(command=islower)
    elif(x == 'Istitle'):                                                                                                                                          #istitle
        result_but.configure(command=istitle)
    elif(x == 'Upper'):                                                                                                                                     #upper
        result_but.configure(command=upper)
    elif(x == 'Lower'):                                                                                                                                     #lower
        result_but.configure(command=lower)
    elif(x == 'Capitalize'):                                                                                                                               #capitalize
        result_but.configure(command=capitalize)
    elif(x == 'Title'):                                                                                                                                          #title
        result_but.configure(command=title)
    elif(x == 'Swapcase'):                                                                                                                              #swapcase
        result_but.configure(command=swapcase)
    elif(x == 'Index'):                                                                                                                                     #index
        result_but.configure(command=index)
        substring_entry.configure(state='normal')
        substring_label.configure(text='Enter Text To Be Searched')
    elif(x == 'Center'):                                                                                                                              #center
        result_but.configure(command=center)
        extra_entry.configure( textvariable=extra1, state='normal')
        substring_entry.configure(state='normal')
        extra_label.configure(text='Length :')
        substring_label.configure(text='Padding Type :')
        
    elif(x == 'Rjust'):                                                                                                                              #Rjust
        result_but.configure(command=rjust)
        extra_entry.configure( textvariable=extra1, state='normal')
        substring_entry.configure(state='normal')
        extra_label.configure(text='Length :')
        substring_label.configure(text='Padding Type :')
        
    elif(x == 'Ljust'):                                                                                                                              #Ljust
        result_but.configure(command=ljust)
        extra_entry.configure( textvariable=extra1, state='normal')
        substring_entry.configure(state='normal')
        extra_label.configure(text='Length :')
        substring_label.configure(text='Padding Type :')

    elif(x == 'Encode'):                                                                                                                        #encode
        result_but.configure(command=encode)
        
    elif(x == 'Decode'):                                                                                                                        #Decode
        result_but.configure(command=decode)
        
    elif(x == 'Strip'):                                                                                                                         #strip
        result_but.configure(command=strip)

    elif(x == 'Lstrip'):                                                                                                                         #Lstrip
        result_but.configure(command=lstrip)    

    elif(x == 'Rstrip'):                                                                                                                         #Rstrip
        result_but.configure(command=rstrip)

    elif(x == 'Ascii'):                                                                                                                         #ascii
        result_but.configure(command=ascii)

    elif(x == 'Character from ascii'):                                                                                                                         #character
        result_but.configure(command=character)
        extra_entry.configure( textvariable=extra1, state='normal')

    elif(x == 'Startswith'):                                                                                                                            #startswith
        result_but.configure(command=startswith)
        substring_entry.configure(  state='normal')
        substring_label.configure(text='Starting Text :')

    elif(x == 'Endswith'):                                                                                                                            #endswith
        result_but.configure(command=endswith)
        substring_entry.configure(  state='normal')
        substring_label.configure(text='Starting Text :')

    elif(x == 'Replace'):                                                                                                                       #replace
        result_but.configure(command=replace)
        substring_entry.configure(  state='normal')
        substring_label.configure(text='String To Be Replace :')
        extra_entry.configure(  state='normal')
        extra_label.configure(text='Replacing String :')

    elif(x == 'Split'):                                                                                                                                     #split
        result_but.configure(command=split)
        substring_entry.configure(  state='normal')
        substring_label.configure(text='Split Point :')
        extra_entry.configure( textvariable=extra1, state='normal')
        extra_label.configure(text='Number Of Splits(-1 for all repeat) :')

    elif(x == 'Count'):                                                                                                                            #count
        result_but.configure(command=count)
        substring_entry.configure(  state='normal')
        substring_label.configure(text='String To Be Count :')
    else:
        None


#########################    BUTTON FUNCTIONs  ############################################################################
def length():                                                                                                                                                   #length
    textbox.delete(1.0,END)
    textbox.insert(1.0, ('Length of string is ', len(string.get())))

def isalpha():                                                                                                                                               #isalpha
     textbox.delete(1.0,END)
     if(string.get().isalpha()):
         textbox.insert(1.0, 'TRUE')
     else:
         textbox.insert(1.0, 'FALSE')
    
def isdigit():                                                                                                                                                  #isdigit
     textbox.delete(1.0,END)
     if(string.get().isdigit()):
         textbox.insert(1.0, 'TRUE')
     else:
         textbox.insert(1.0, 'FALSE')
         
def isalnum():                                                                                                                                              #isalnum
     textbox.delete(1.0,END)
     if(string.get().isalnum()):
         textbox.insert(1.0, 'TRUE')
     else:
         textbox.insert(1.0, 'FALSE')

def isspace():                                                                                                                                              #isspace
     textbox.delete(1.0,END)
     if(string.get().isspace()):
         textbox.insert(1.0, 'TRUE')
     else:
         textbox.insert(1.0, 'FALSE')

def isupper():                                                                                                                                              #isupper
     textbox.delete(1.0,END)
     if(string.get().isupper()):
         textbox.insert(1.0, 'TRUE')
     else:
         textbox.insert(1.0, 'FALSE')

def islower():                                                                                                                                              #islower
     textbox.delete(1.0,END)
     if(string.get().islower()):
         textbox.insert(1.0, 'TRUE')
     else:
         textbox.insert(1.0, 'FALSE')
    
def istitle():                                                                                                                                                    #istitle
     textbox.delete(1.0,END)
     if(string.get().istitle()):
         textbox.insert(1.0, 'TRUE')
     else:
         textbox.insert(1.0, 'FALSE')

def upper():                                                                                                                                                #upper
     textbox.delete(1.0,END)
     textbox.insert(1.0,string.get().upper())
    
def lower():                                                                                                                                                #lower
     textbox.delete(1.0,END)
     textbox.insert(1.0,string.get().lower())

def capitalize():                                                                                                                                        #capitalize
     textbox.delete(1.0,END)
     textbox.insert(1.0,string.get().capitalize())

def title():                                                                                                                                                #title
     textbox.delete(1.0,END)
     textbox.insert(1.0,string.get().title())

def swapcase():                                                                                                                                         #swapcase
     textbox.delete(1.0,END)
     textbox.insert(1.0,string.get().swapcase())

def index():                                                                                                                                                #index
    textbox.delete(1.0,END)
    textbox.insert(1.0,string.get().find(substring.get()))

def center():                                                                                                                                               #center
    textbox.delete(1.0,END)
    centered = string.get().center(extra1.get(), substring.get())
    textbox.insert(1.0,centered)

def rjust():                                                                                                                                               #rjust
    textbox.delete(1.0,END)
    centered = string.get().rjust(extra1.get(), substring.get())
    textbox.insert(1.0,centered)

def ljust():                                                                                                                                               #ljust
    textbox.delete(1.0,END)
    centered = string.get().ljust(extra1.get(), substring.get())
    textbox.insert(1.0,centered)

def encode():                                                                                                                                       #encode
    textbox.delete(1.0,END)
    for i in string.get():
        encoded = (ord(i) + 3)
        textbox.insert(1.0, chr(encoded))

def decode():                                                                                                                                       #decode
    textbox.delete(1.0,END)
    for i in string.get():
        decoded = (ord(i) - 3)
        textbox.insert(1.0, chr(decoded))

def strip():                                                                                                                                                #strip
     textbox.delete(1.0,END)
     textbox.insert(1.0,string.get().strip())

def lstrip():                                                                                                                                                #lstrip
     textbox.delete(1.0,END)
     textbox.insert(1.0,string.get().lstrip())

def rstrip():                                                                                                                                                #rstrip
     textbox.delete(1.0,END)
     textbox.insert(1.0,string.get().rstrip())

def ascii():
    textbox.delete(1.0,END)
    for i in string.get():
        textbox.insert(END, ('%d \n'%ord(i)) )

def character():                                                                                                                                        #character
    textbox.delete(1.0,END)
    textbox.insert(END, chr(extra1.get()) )
    string_entry.insert(END, chr(extra1.get()) )

def startswith():                                                                                                                                        #startswith
    textbox.delete(1.0,END)
    if(string.get().startswith(substring.get())):
        textbox.insert(1.0, 'TRUE')
    else:
        textbox.insert(1.0, 'FALSE')

def endswith():                                                                                                                                        #endswith
    textbox.delete(1.0,END)
    if(string.get().endswith(substring.get())):
        textbox.insert(1.0, 'TRUE')
    else:
        textbox.insert(1.0, 'FALSE')

def replace():
    
    textbox.insert(1.0,string.get().replace(substring.get(), extra.get()))
    

def split():                                                                                                                                             #split
    textbox.delete(1.0,END)
    textbox.insert(1.0,string.get().split(substring.get(), extra1.get()))

def count():
    textbox.delete(1.0,END)
    textbox.insert(1.0,('String %s Is Repeated %d Times'%(substring.get(), string.get().count(substring.get()))))


#########################   WINDOW SETUP ################################################################################
win = Tk()
win.title('String Function')
win.geometry('660x300+100+100')
#frame
top_frame = Frame(win)
listbox_frame = Frame(win)
entry_frame = Frame(win)
result_frame  = Frame(win)

top_frame.grid(row=0, columnspan=2, sticky='nsew')
listbox_frame.grid(row=2, column=0, sticky=NW)
entry_frame.grid(row=1, columnspan=2, sticky=W)    
result_frame.grid(row=2, column=1, sticky=W)


#listbox++================+=+++++++===================================================================================================
listbox = Listbox(listbox_frame, width=40, height=9, font=('arial',10,'bold'), cursor='hand2')
listbox.grid(row=0,column=0, sticky=N)
listbox.bind('<Button-1>', listbox_fun)
scrollbar= Scrollbar(listbox_frame, orient = 'vertical')

listbox.insert(0,'Length')
listbox.insert(1,'Isalpha')
listbox.insert(2,'Isdigit')
listbox.insert(3,'Isalnum')
listbox.insert(4,'Isspace')
listbox.insert(5,'Upper')
listbox.insert(6,'Lower')
listbox.insert(7,'Capitalize')
listbox.insert(8,'Swapcase')
listbox.insert(9,'Title')
listbox.insert(10,'Isupper')
listbox.insert(11,'Islower')
listbox.insert(12,'Istitle')
listbox.insert(13,'Index')
listbox.insert(14,'Center')
listbox.insert(15,'Rjust')
listbox.insert(16,'Ljust')
listbox.insert(17,'Encode')
listbox.insert(18,'Decode')
listbox.insert(19,'Strip')
listbox.insert(20,'Lstrip')
listbox.insert(21,'Rrtrip')
listbox.insert(22,'Ascii')
listbox.insert(23,'Character from ascii')
listbox.insert(24,'Startswith')
listbox.insert(25,'Endswith')
listbox.insert(26,'Replace')
listbox.insert(27,'Split')
listbox.insert(28,'Count')




scrollbar.config( command = listbox.yview)
scrollbar.grid(row=0, column=1, sticky='ns')
listbox.config(yscrollcommand=scrollbar.set)
    
#label++++++++==================++++++++======================++++++===================================================================
topic_label = Label(top_frame, text='******    STRING  FUNCTION   ******' , font=('arial',30,'bold'), relief=SUNKEN, bd=5, bg='powder blue')
string_label = Label(entry_frame, text='  Enter Your String :', font=('arial',10,'bold'))
substring_label = Label(entry_frame, text='  Enter Your Sub-String :', font=('arial',10,'bold'))
extra_label = Label(entry_frame, text='    value : ', font=('arial',10,'bold'))
fun_label = Label(entry_frame, text='Functions')

topic_label.grid(sticky='ew')
string_label.grid(row=0, column=0, ipadx=20, ipady=2, sticky=E)
substring_label.grid(row=0, column=2, ipadx=20, ipady=2, sticky=E)
extra_label.grid(row=1,  column=0, ipadx=20, ipady=2, sticky=E)
fun_label.grid(row=2,column=0, sticky=SW)


#entry
string = StringVar()
substring = StringVar()
extra = StringVar()
extra1 = IntVar()
string_entry = Entry(entry_frame, font=('arial',10,'bold'), textvariable=string, bg='lightsteelblue2')
substring_entry = Entry(entry_frame, state='disabled', font=('arial',10,'bold'), textvariable=substring, bg='thistle1')
extra_entry = Entry(entry_frame, state='disabled', font=('arial',10,'bold'), textvariable=extra, bg='bisque1')

string_entry.grid(row=0, column=1, sticky=W)
substring_entry.grid(row=0, column=3, sticky=W)
extra_entry.grid(row=1, column=1, sticky=W)

#textbox
textbox = Text(result_frame, width =43, height=8)
textbox.grid()

#button
clear_but = Button(entry_frame, text='Clear', cursor='hand2', command = clear)
result_but = Button(result_frame, text='RESULT', fg='green', bd=2, relief=RAISED, font='arial', cursor='hand2', command=None)
exit_but = Button(entry_frame, text='Exit', fg='red', cursor='hand2', command=exit)

clear_but.grid(row=1, column=2, ipadx=20)
result_but.grid(row=1, column=0,  ipadx=20, sticky=EW)
exit_but.grid(row=1,column=3,  ipadx=20)

win.mainloop()

                            
