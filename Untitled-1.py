import os
print(" Hello  Welcome")
print("-------------------")
print("""
1:Date
2:Cal
3:Exit
4:File""")
input_User=input('input: ')
if  int(input_User)==1:
    os.system("date")
if int(input_User)==2:
    os.system("cal")
if int (input_User)==3:
    os.system("exit")
if int (input_User)==4:
    print("""            1: To create a file
            2: To write the file
            3: To display content""")
    peee=input()
    if int(peee)==1:
        pee=input("Enter File Name")
        os.system(">{}".format(pee))
    if int(peee)==2:
        pee=input("Enter File Name")
        os.system("cat >{}".format(pee))
    if int(peee)==3:
        pee=input("Enter File Name")
        os.system("cat {}".format(pee))
    else:
        print("error")
else:
    print("error")