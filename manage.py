
"""
manage.py file has:
class Manage: manages I/O file 
"""

import student as s
import csv
import os.path
import check
import job as j
import settings as stg
import profiles as pro
from datetime import datetime

FILENAME = "student_data.csv"
FILENAME_JOB = "job_data.csv"
FILENAME_STG = "settings.csv"
FILENAME_PRO = "profiles.csv"

class Manage:
    def __init__(self):
        
        #create a list of student Object
        #self__list_student will store object of Student class
        self.__list_student = []
        self.__list_job = []
        self.__list_settings = []
        self.__list_profiles = []

        #add title for the student_data.csv
        if not os.path.isfile(FILENAME):
            with open(FILENAME,"w") as file:
                writer_csv = csv.writer(file)
                writer_csv.writerow(("User_Name","Password","First_Name","Last_Name"))

        #add data from student_data.csv to __self.__list_student
        with open(FILENAME,"r") as file:
            reader_csv = csv.reader(file)
            for row in reader_csv:
                if row != []:
                    self.__list_student.append(s.Student(row[0], row[1], row[2], row[3]))


        #add title for the job_data.csv
        if not os.path.isfile(FILENAME_JOB):
            with open(FILENAME_JOB,"w") as file:
                writer_csv = csv.writer(file)
                writer_csv.writerow(("Title","Description","Employer","Location","Salary","Post_Name"))

        #add data from job_data to __self.__list_job
        with open(FILENAME_JOB,"r") as file:
            reader_csv = csv.reader(file)
            for row in reader_csv:
                if row != []:
                    self.__list_job.append(j.Job(row[0], row[1], row[2], row[3], row[4], row[5]))
                    
        #add title for the settings.csv
        if not os.path.isfile(FILENAME_STG):
            with open(FILENAME_STG,"w") as file:
                writer_csv = csv.writer(file)
                writer_csv.writerow(("user", "email_notif","sms_notif","targeted_ads","language"))

        #add data from settings.csv to __self.__list_settings
        with open(FILENAME_STG,"r") as file:
            reader_csv = csv.reader(file)
            for row in reader_csv:
                if row != []:
                    self.__list_settings.append(stg.Settings(row[0], row[1], row[2], row[3], row[4]))
  
        #add title for the profiles.csv
        if not os.path.isfile(FILENAME_PRO):
            with open(FILENAME_PRO,"w") as file:
                writer_csv = csv.writer(file)
                writer_csv.writerow(("user", "title","major","university","bio", "experience", "education"))

        #add data from profiles.csv
        with open(FILENAME_PRO,"r") as file:
            reader_csv = csv.reader(file)
            for row in reader_csv:
                if row != []:
                    self.__list_profiles.append(pro.Profiles(row[0], row[1], row[2], row[3], row[4], row[5], row[6]))
    
    def get_list(self):
        return self.__list_student

    
    def get_length(self):
        return len(self.__list_student)

            
    # add a new object student with given first, last name and password to student_data.csv file 
    def add_student(self, student):
        for element in self.__list_student:
            if element.get_user_name() == student.get_user_name():
                print("\nThere is an account with the same username")
                print("Try again!")
                return None #It is easier for pytest
       
        if len(self.__list_student) < 6:
            self.__list_student.append(student)
            user_name = student.get_user_name()
            print("\nCongratulate",student.get_name(), "\nYou signed up and logged in successfully!")

            #need to add a new student to student_data.csv
            with open(FILENAME,"a") as file:
                writer_csv = csv.writer(file)
                writer_csv.writerow((student.get_user_name(),student.get_password(),student.get_first(),student.get_last()))  

            #create settings associated with this user
            with open(FILENAME_STG, "a") as file_stg:
                writer_csv = csv.writer(file_stg)
                writer_csv.writerow((user_name, "on", "on", "on", "English")) #all features on and language set to english when account is created

            return user_name 
            
        else:
            print("All permitted accounts have been created, please come back later")
            return None #It is easier for pytest

    #return name of user that log in successfully
    def log_in(self):
        #create a new object of Manage class
        manage = Manage()
        
        #when the student_data.csv file doesn't have any user's record
        if len(manage.get_list()) == 1:
            print("\nDon't have any account in System")
            print("You have to sign up for a new account!\n")
            return None 
        

        #create an object of class Name_Password
        p = check.Name_Password()

        #promp from the user for user name
        user_name = input("Enter username: ")
        
        #if the user name exists in student_data.csv file
        while not p.name_check(user_name):
            print("Please try again: ")
            user_name = input("Enter user name again: ")

        #if the user's password is right
        #assume that: the user will log in successfully, try unlimited
        password = input ("Enter a password: ")
        while not p.password_check(user_name,password):
            password = input ("Incorrect password, please try again: ")
        
        
        print("\nYou have successfully logged in\n")

        return user_name #return user name

    # promp name and password from user, and then use add_student() to add student's infortion to student_data.csv file
    def new_account(self):

        #create a new object of Manage class
        manage = Manage()

        #promp from the user for first and last name
        user_name = input("Enter username: ")
        password = input ("Enter a password: ")
        first = input("Enter first name: ")
        last = input("Enter last name: ")

        #create a new object of class Password_account
        p = check.Password_account()

        #if the user's password has requirement about letter, number, ....
        while not(p.min_character(password)) or not(p.max_character(password)) or not(p.capital_letter(password)) or not(p.digit(password)) or not(p.non_alpha(password)):
            password = input ("Please enter a password again: ")

        #create a new object of student class and add the object the student_data.csv file
        student = s.Student(user_name, password, first, last)
        return manage.add_student(student)



    def find_people(self, first, last):
        #create a new object of Manage class
        manage = Manage()

        name = first + " " + last
        #check if the user's friend in the InCollege system
        for element in manage.__list_student:
            if element.get_name() == name:
                print("\nThey are a part of the InCollege system")
                return element.get_user_name()
        
        print("\nThey are not yet a part of the InCollege system yet")
        return None




    def add_job(self, job, n):
        if len(self.__list_job) >= 5:
            print("You cannot post more job! Limit 5!")
            return None

        else:
            self.__list_job.append(job)
            print("You posted a job in InCollege System")
            with open(FILENAME_JOB,"a") as file:
                writer_csv = csv.writer(file)
                writer_csv.writerow((job.get_title(),job.get_description(),job.get_employer(),job.get_location(),job.get_salary(),job.get_post_name())) 

            return(job.get_post_name())# We can return a tupe here for many purpose later


    def new_job(self, post_name):
        manage = Manage()
        
        title = input("Enter Title: ")
        description = input("Enter Description: ")
        employer = input("Enter Emplyer: ")
        location = input("Enter Location: ")
        salary = input("Salary: ")

        p = check.Input_Value()
        #check right value of salary
        while not p.isNumber(salary) or float(salary) <= 0:
            print("\nThe salary should be a positive number. Try again!")
            salary = input("Salary: ")

        job = j.Job(title,description,employer,location,salary, post_name)
        return manage.add_job(job,post_name) # return user's name who posted a job,  We can return a tupe here
        
    # user = the user that is logged in and their settings
    # field = the setting trying to check so type exactly one of these ("email_notif", "sms_notif", "targeted_ads", or "language")    
    # state = whether is on/off or e/s
    def check_settings(self, user, field, state):
        manage = Manage()
        #find the settings object associated with that user
        for element in manage.__list_settings:
            if element.get_user() == user:
                if field == "email_notif":
                    return element.get_email_notif()
                elif field == "sms_notif":
                    return element.get_sms_notif()
                elif field == "targeted_ads":
                    return element.get_targeted_ads()
                elif field == "language":
                    return element.get_language()
                else: 
                    print("This field in the Guest Controls/Settings do not exist")
                    return "DNE"
        
        #shouldn't ever return the user's username bc settings are only made when users are, so will need to check if it returns the user's username
        print("This user DNE")
        return element.get_user()

    def createProfile(self, name):                  #Creates Profiles
        title = input("Enter Title: ")
        major = input("Enter Major: ")
        major = major.title()
        university = input("Enter University: ")
        university = university.title()
        bio = input("About Yourself: ")
        expCheck = input("Do you have any experience you would like to add? (Yes/No)  ")
        experience = ""
        while expCheck.upper()!="YES" and expCheck.upper()!="NO":
            expCheck=input("Invalid Input. Try Again: ")
        if expCheck.upper() == "YES":
            for x in range(3):
                expTitle = input("Job Title: ")
                expEmployer = input("Employer: ")
                expDateSt = input("Date Started MM/DD/YYYY: ")
                while(valiDate(expDateSt)==False):
                    expDateSt = input("Date not valid. Try Again: ")
                expDateEnd = input("Date Ended MM/DD/YYYY: ")
                while(valiDate(expDateEnd)==False or compareDates(expDateSt, expDateEnd)==False):
                    if(valiDate(expDateEnd)==False):
                        expDateEnd = input("Date not valid. Try Again: ")
                    elif(compareDates(expDateSt, expDateEnd)==False):
                        expDateEnd = input("Date is before start date. Try Again: ")

                expLocation = input("Job Location: ")
                expDesc = input("Job Description: ")
                experience = experience + "(" + expTitle + "," + expEmployer + "," + expDateSt + "," + expDateEnd + "," + expLocation + "," + expDesc + ")"
                if(x<2):
                    another = input("Do you have more experience to add? (Yes/No)  ")
                    while another.upper()!="YES" and another.upper()!="NO":
                        another=input("Invalid Input. Try Again: ")
                if another.upper()=="NO":
                    break
        school = input("\nEducation - Enter School Name: ")
        degree = input("Enter Degree: ")
        years = input("Enter Years Attended: ")
        education = "[" + school + "," + degree + "," + years + "]" 

        print("\nYou have created a profile in the InCollege System!")
        with open(FILENAME_PRO, "a") as file_pro:
            writer_csv = csv.writer(file_pro)
            writer_csv.writerow((name, title, major, university, bio, experience, education))


    def viewProfile(self, name):
        with open(FILENAME_PRO,"r") as file:
            reader_csv = csv.reader(file)
            for row in reader_csv:
                if row != [] and row[0] == name:
                    print()
                    for element in self.__list_student:
                        if element.get_user_name() == name:
                            print(element.get_name())
                    print("Title: " + row[1])
                    print("Major: " + row[2])
                    print("University Name: " + row[3])
                    print("About me: " + row[4])
                    experience = row[5]
                    list_experience = experience.split(")")
                    list_experience.pop()
                    print()
                    for element in list_experience:
                        sub_element = element[1:]
                        list_sub_experience = sub_element.split(",")
                        print("Title: " + list_sub_experience[0])
                        print("Job Description: " + list_sub_experience[5])
                        print("Place of work: " + list_sub_experience[4])
                        print("Start date: " + list_sub_experience[2])
                        print("End date: " + list_sub_experience[3])
                        print("Employer: " + list_sub_experience[1])
                        print()
                    print("Education information")
                    education = row[6]
                    len_education = len(education) - 1
                    sub_education = education[1:len_education]
                    
                    list_sub_education = sub_education.split(",")
                    print("University: " + list_sub_education[0])
                    print("Major: " + list_sub_education[1])
                    print("Years so far: " + list_sub_education[2])
                    return name
                
                
        print()
        print("You did not create a profile!")
        return name

        

def valiDate(date_text):
    try:
        datetime.strptime(date_text, '%m/%d/%Y')
        return True
    except ValueError:
        return False

def compareDates(date1, date2):
    d1 = datetime.strptime(date1, '%m/%d/%Y')
    d2 = datetime.strptime(date2, '%m/%d/%Y')
    return d1<d2



    

                    




   

    

        
        
