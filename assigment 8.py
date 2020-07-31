class Employee:
    def __init__(self, name, designation, gender, doj, salary):
        self.name = name
        self.designation = designation
        self.gender = gender
        self.doj = doj
        self.salary = salary

emp_list = []
def registration():
    while(1):
        print('note :- to exit press 0 ')

        name = input('Enter name : ')
        if (name == '0'):
            break
        else:
            designation = input('Enter designation : ')
            gender = input('Enter your Gender :')
            doj = input('Enter Date Of Joining : ')
            salary = input('Enter salary : ')

            name = Employee(name, designation, gender, doj, salary)
            emp_list.append(name)
            print("Registration Done!")
        globals().update(locals())

def stat():
    while(1):
        print("""*******************************************
        
        
        1. Number of employee
        2. Number of female employee
        3. Number of male employee
        4. Assistant manager
        5. Number of employee having salary greater than 10 thosand
        6. Back
        
    
        
        """)
        op2 = int(input('CHOOSE OPTION: '))
        if (op2 == 1):
            print(len(emp_list))

        elif(op2 == 2):
            fe = 0
            for i in emp_list:
                if(i.gender.upper() == 'F' ):
                    fe += 1
                else:
                    None
            print("Number of female employee : ", fe)

        elif(op2 == 3):
            me = 0
            for i in emp_list:
                if (i.gender.upper() == 'M'):
                    me += 1
                else:
                    None
            print("Number of male employee", me)

        elif(op2 == 4):
            for i in emp_list:
                if (i.designation.upper() == 'ASSISTANT MANAGER'):
                    print(i.name, i.designation)
                else:
                    None

        elif(op2 == 5):
            sl = 0
            for i in emp_list:

                if (i.salary >= '10000'):
                    sl += 1
                else:
                    None
            print('Number of employee having salary greater than 10 thousand : ', sl)
        elif(op2 == 6):
            break





while(1):
    print("""**************MENU**************
    
    
    1. Employee Registration
    2. statistics
    3. Employee information
    4. Exit
    
    """)
    op1 = int(input("CHOOSE  OPTION :"))
    if (op1 == 1):
        registration()
    if (op1 == 2):
        stat()
    if (op1 == 3):

        for i in emp_list:
            print(i.name, '\n')

        search = input('Enter name of an employee :')
        for i in emp_list:
            if(i.name.upper() == search.upper()):
                print(i.__dict__)


    if(op1 == 4):
        break
