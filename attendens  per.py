from tkinter import *
while(1):
        print('''
                1. Attendence Calculator
                2. Attendence predector
                3. exit press -1''')
            
        option = int(input('Enter your choice '))



        if (option == 1):
                
                tot_lec = int(input('total lectuer in the week '))
                i=1
                att_list= []
                print('Enter 00 to calculate')
                while(1):

                    att_lec = int(input('lecture attend in week %d '  %i ))
                    if (att_lec == 00):
                        break
                    else :


                            att_per = (att_lec/ tot_lec )*100

                            print(att_per)
                            att_list.append(att_per)
                            i += 1


                tot_att = sum(att_list)/len(att_list)
                print('Total attendence %f' %tot_att)

        elif(option == 2):
            print('''  
         1. lecture to be attend for 75% attendence
         2. next week attendence prediction from attend lecture
         3. Lecture to be attend for specified attendence percentage \n''')
            option1 = int(input('choose your option'))

            if(option1 == 1):
                tot_lec = int(input('total lectuer in the week '))
                current_att = int(input('Enter cuurent attendence percentage'))

                predict_att = (75*2)- current_att
                print(predict_att)
                
                lect_attended = (predict_att * 33)/100
                if(lect_attended >= 33):
                    print('you cant do it')
                else:
                    bunk_lect = 33 -  lect_attended
                    print('you can bunk %d lectures' %bunk_lect)
                
            if(option1 == 3):
                tot_lec = int(input('total lectuer in the week '))
                current_att = int(input('Enter cuurent attendence percentage'))
                desired_att = int(input('desired attendence percentage'))

                predict_att = (desired_att*2)- current_att
                print(predict_att)
                
                lect_attended = (predict_att * 33)/100
                if(lect_attended >= 33):
                    print('you cant do it in this week')
                else:
                    bunk_lect = 33 -  lect_attended
                    print('you can bunk %d lectures' %bunk_lect)
        elif(option == -1):
            exit()
            
