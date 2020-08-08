#Python program to demonstrate mutable and imutable data types
#declaring global data variable for storing
campuses_info = {}
campuses_data = ['College_ID','DOE']
admins_info = {}
admins_data = ['Admin_ID','Role','College','Election Year']
dept_info = {}
dept_data = ['Dept_ID','HOD','College']
prog_info = {}
prog_data = ['Prog_ID','Duration','Department']
cou_info = {}
cou_data = ['Course_ID','Duration','Programme_Name']
std_info = {}
std_data = ['Student_ID','DOB','Programme_Name','Address']
#function to add details 
def add_Details(message):
  print("\n\tAdding Details:")
  print("...............................\n")
  if message=="CAMPUSES":
    num_campuses = int(input("Please enter number of campus:"))
    if num_campuses <= 0:
      print("\nplease input valid Number\n\n")
      return
    print ("you entered %s Campuses" %num_campuses)
    for i in range(0,num_campuses):
      campus_name = input("Name : ")
      campuses_info[campus_name] = {}
      for entry in campuses_data:
        campuses_info[campus_name][entry] = input(entry+" : ")
    print(message+" Details added sucessfully!\n\n")
  elif message=="ADMINISTRATOR":
    num_admins = int(input("Please enter number of ADMINISTRATOR:"))
    if num_admins <= 0:
      print("\nplease input valid Number\n\n")
      return
    print ("you entered %s ADMINISTRATOR" %num_admins)
    for i in range(0,num_admins):
      admins_name = input("Name : ")
      admins_info[admins_name] = {}
      for entry in admins_data:
        admins_info[admins_name][entry] = input(entry+" : ")
    print(message+" Details added sucessfully!\n\n")
  elif message=="DEPARTMENT":
    num_dept = int(input("Please enter number of DEPARTMENT:"))
    if num_dept <= 0:
      print("\nplease input valid Number\n\n")
      return
    print ("you entered %s DEPARTMENT" %num_dept)
    for i in range(0,num_dept):
      dept_name = input("Department Name : ")
      dept_info[dept_name] = {}
      for entry in dept_data:
        dept_info[dept_name][entry] = input(entry+" : ")
    print(message+" Details added sucessfully!\n\n")
  elif message=="PROGRAMMES":
    num_prog = int(input("Please enter number of PROGRAMMES:"))
    if num_prog <= 0:
      print("\nplease input valid Number\n\n")
      return
    print ("you entered %s PROGRAMMES" %num_prog)
    for i in range(0,num_prog):
      prog_name = input("PROGRAMMES Name : ")
      prog_info[prog_name] = {}
      for entry in prog_data:
        prog_info[prog_name][entry] = input(entry+" : ")
    print(message+" Details added sucessfully!\n\n")
  elif message=="COURSE":
    num_cou = int(input("Please enter number of COURSE:"))
    if num_cou <= 0:
      print("\nplease input valid Number\n\n")
      return
    print ("you entered %s COURSE" %num_cou)
    for i in range(0,num_cou):
      cou_name = input("COURSE Name : ")
      cou_info[cou_name] = {}
      for entry in cou_data:
        cou_info[cou_name][entry] = input(entry+" : ")
    print(message+" Details added sucessfully!\n\n")
  elif message=="STUDENTS":
    num_std = int(input("Please enter number of STUDENTS:"))
    if num_std <= 0:
      print("\nplease input valid Number\n\n")
      return
    print ("you entered %s STUDENTS" %num_std)
    for i in range(0,num_std):
      std_name = input("STUDENT Name : ")
      std_info[std_name] = {}
      for entry in std_data:
        std_info[std_name][entry] = input(entry+" : ")
    print(message+" Details added sucessfully!\n\n")
  
#function to show details 
def show_Details(message):
  print("\n\nYour Request Details for "+ message+" :")
  print("...............................")
  if message=="CAMPUSES":
    for c_id, c_info in campuses_info.items():
      print("\nCampus Name: ", c_id)
      for key in c_info:
        print(key + ': ', c_info[key])
      print("...............................")
  elif message=="ADMINISTRATOR":
    for c_id, c_info in admins_info.items():
      print("Full Name: ", c_id)
      for key in c_info:
        print(key + ': ', c_info[key])
      print("...............................")
  elif message=="DEPARTMENT":
    for c_id, c_info in dept_info.items():
      print("Department Name: ", c_id)
      for key in c_info:
        print(key + ': ', c_info[key])
      print("...............................")
  elif message=="PROGRAMMES":
    for c_id, c_info in prog_info.items():
      print("PROGRAMME Name: ", c_id)
      for key in c_info:
        print(key + ': ', c_info[key])
      print("...............................")
  elif message=="COURSE":
    for c_id, c_info in cou_info.items():
      print("COURSE Name: ", c_id)
      for key in c_info:
        print(key + ': ', c_info[key])
      print("...............................")
  elif message=="STUDENTS":
    for c_id, c_info in std_info.items():
      print("STUDENT Name: ", c_id)
      for key in c_info:
        print(key + ': ', c_info[key])
      print("...............................")
#function to display particular sector message
def show_sector(message):
  print("\t "+message+" DETAILS")
  print("------------------------------------------------------")
  print("\t1.Add\n\t2.Display\n")
  option = input("\tChoose options: \n=>\t")
  if option == "1" or option == "add" or option== "Add":
    add_Details(message)
  elif option == "2" or option == "display" or option== "Display":
    show_Details(message)
  else:
    print("Wrong Input, please try again!!\n\n")
#Main function starts from here
print("____Program to Store University Details____")
start=1
while start != 0:
  print("\n\n\n********************************************************")
  print("\tWelcome to CHRIST UNIVERSITY (DEEMED TO BE UNIVERSITY)\n_______________________________________________________\n\t\t\tLAXMAN\tKHATRI\t2048014 ")
  print("********************************************************")
  print("\t1.Campuses\n\t2.Administrators\n\t3.Department\n\t4.Programmes\n\t5.Course\n\t6.Students")
  print("------------------------------------------------------")
  choice = input("\tWhat Sector Details you want to store? Type N when you are finished: \n=>\t")
  print("+++++++++++++++++++++++++++++++++++++++++++++++++++++")
  if choice == "1" or choice == "Campuses" or choice == "campuses": 
    show_sector("CAMPUSES")
  elif choice == "2" or choice == "Administrators" or choice == "administrators": 
    show_sector("ADMINISTRATOR")
  elif choice == "3" or choice == "Department" or choice == "department": 
    show_sector("DEPARTMENT") 
  elif choice == "4" or choice == "Programmes" or choice == "programmes": 
    show_sector("PROGRAMMES")
  elif choice == "5" or choice == "Course" or choice == "course": 
    show_sector("COURSE")
  elif choice == "6" or choice == "Students" or choice == "students": 
    show_sector("STUDENTS")
  elif choice == "N" or choice == "n":
    print("Have a great Day, Sir/Ma'am!\n\n")
    break
  else:
    print("Please Try again!")
    print("==========================================================\n")
