import os 

os.system("tput setaf 1")

print("        hello welcome to this terminal user interface__________")

os.system("tput setaf 7")

print("""    Hey welcome to my TUI makes life easy
        ---------------------------------------------------------
      where would you like to go (Local or Remote)?""")

c=input()
os.system("tput setaf 7")
if c== "local":
      print("""
                   ___ MENU___
       1.see date
       2.to check cal
       3 .conf web server
       4.to create a user
       5 .create file
       6.to setup a network
       7.to exit 
       Enter your choice:
         """)
       ch=input()
    
       if int(ch)== 1:
            os.system("date")
       elif int(ch)== 2:
            os.system("cal")
       if int(ch)== 3:
             os.system("date")
       elif int(ch)== 4:
            os.system("cal")
      
       if int(ch)== 5:
            os.system("date")
       elif int(ch)== 6:
           os.system("cal")
      
       if int(ch)== 7:
            os.system("exit")
    


else:
         print("remote")
         print("""
                   ___ MENU___
         1.see date
         2.to check cal
         3.conf web server
         4.to create a user
         5.create file
         6.to setup a network
         7.to exit
         """)




