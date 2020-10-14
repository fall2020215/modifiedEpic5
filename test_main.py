import pytest
import main
import check as ch
import manage as ma
import student as st
import job as jo
import random
from random import choice
import string
import csv


class TestClass:
    def test_importantLinks(self):             #adds students to test the creation of default setting values
        filename = "settings.csv"
        f = open(filename, "w+")
        f.close()
        manage = ma.Manage()

        filename2 = "student_data.csv"
        f = open(filename2, "w+")
        f.close()
        manage = ma.Manage()
        #########################################

        stud1 = st.Student("TP1", "P@ssword123", "Tracy", "Pham")
        assert manage.add_student(stud1) == stud1.get_user_name()
        lines = list()
        entry = [" ", " ", " ", " ", " "]
        blank = []
        count = 0
        #read current settings and fill 'lines' with info
        with open(filename, 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                if row != blank: #or else there will be stupid amount of white space
                    lines.append(row)
                    count = count + 1
                for field in row: 
                    if (field == "TP1"):
                        entry = [lines[count-1][0], lines[count-1][1], lines[count-1][2], lines[count-1][3], lines[count-1][4]]
                        lines.pop()
                        count = count - 1

        assert (stud1.get_user_name() == entry[0])
        assert ("on" == entry[1])
        assert ("on" == entry[2])
        assert ("on" == entry[3])
        assert ("English" == entry[4])

        ##########################################
        
        stud2 = st.Student("TP2", "P@ssword123", "Thinh", "Phung")
        assert manage.add_student(stud2) == stud2.get_user_name()
        lines = list()
        entry = [" ", " ", " ", " ", " "]
        blank = []
        count = 0
        #read current settings and fill 'lines' with info
        with open(filename, 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                if row != blank: #or else there will be stupid amount of white space
                    lines.append(row)
                    count = count + 1
                for field in row: 
                    if (field == "TP2"):
                        entry = [lines[count-1][0], lines[count-1][1], lines[count-1][2], lines[count-1][3], lines[count-1][4]]
                        lines.pop()
                        count = count - 1

        assert (stud2.get_user_name() == entry[0])
        assert ("on" == entry[1])
        assert ("on" == entry[2])
        assert ("on" == entry[3])
        assert ("English" == entry[4])

        ##########################################
        
        stud3 = st.Student("DP", "P@ssword123", "Daniel", "Polt")
        assert manage.add_student(stud3) == stud3.get_user_name()
        lines = list()
        entry = [" ", " ", " ", " ", " "]
        blank = []
        count = 0
        #read current settings and fill 'lines' with info
        with open(filename, 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                if row != blank: #or else there will be stupid amount of white space
                    lines.append(row)
                    count = count + 1
                for field in row: 
                    if (field == "DP"):
                        entry = [lines[count-1][0], lines[count-1][1], lines[count-1][2], lines[count-1][3], lines[count-1][4]]
                        lines.pop()
                        count = count - 1

        assert (stud3.get_user_name() == entry[0])
        assert ("on" == entry[1])
        assert ("on" == entry[2])
        assert ("on" == entry[3])
        assert ("English" == entry[4])

        ##########################################

        stud4 = st.Student("KP", "P@ssword123", "Kelvin", "Pun")
        assert manage.add_student(stud4) == stud4.get_user_name()
        lines = list()
        entry = [" ", " ", " ", " ", " "]
        blank = []
        count = 0
        #read current settings and fill 'lines' with info
        with open(filename, 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                if row != blank: #or else there will be stupid amount of white space
                    lines.append(row)
                    count = count + 1
                for field in row: 
                    if (field == "KP"):
                        entry = [lines[count-1][0], lines[count-1][1], lines[count-1][2], lines[count-1][3], lines[count-1][4]]
                        lines.pop()
                        count = count - 1

        assert (stud4.get_user_name() == entry[0])
        assert ("on" == entry[1])
        assert ("on" == entry[2])
        assert ("on" == entry[3])
        assert ("English" == entry[4])

        ##########################################
        
        stud5 = st.Student("YQ", "P@ssword123", "Yakira", "Quemba")
        assert manage.add_student(stud5) == stud5.get_user_name()
        lines = list()
        entry = [" ", " ", " ", " ", " "]
        blank = []
        count = 0
        #read current settings and fill 'lines' with info
        with open(filename, 'r') as readFile:
            reader = csv.reader(readFile)
            for row in reader:
                if row != blank: #or else there will be stupid amount of white space
                    lines.append(row)
                    count = count + 1
                for field in row: 
                    if (field == "YQ"):
                        entry = [lines[count-1][0], lines[count-1][1], lines[count-1][2], lines[count-1][3], lines[count-1][4]]
                        lines.pop()
                        count = count - 1

        assert (stud5.get_user_name() == entry[0])
        assert ("on" == entry[1])
        assert ("on" == entry[2])
        assert ("on" == entry[3])
        assert ("English" == entry[4])

    def test_Jobs(self):             #adds jobs so I can test the addition
        filename = "job_data.csv"
        f = open(filename, "w+")
        f.close()
        manage = ma.Manage()
        job1 = jo.Job("Porter", "TransportsItems", "Bridges", "UCA", "10", "TP1")
        assert manage.add_job(job1, "TP1") == job1.get_post_name()
        job2 = jo.Job("Developer", "WritesCode", "USF", "FL", "20", "TP2")
        assert manage.add_job(job2, "TP2") == job2.get_post_name()
        job3 = jo.Job("Tester1", "Tests", "USF", "FL", "20", "DP")
        assert manage.add_job(job3, "DP") == job3.get_post_name()
        job4 = jo.Job("Tester2", "Tests", "USF", "FL", "20", "KP")
        assert manage.add_job(job4, "KP") == job4.get_post_name()
        job5 = jo.Job("SCRUMMaster", "ManagesSCRUM", "USF", "FL", "30", "YQ")
        assert manage.add_job(job5, "YQ") == job5.get_post_name()

    def test_passwordLength(self):
        correct = random.randint(8, 12)
        less = random.randint(0, 7)
        more = random.randint(13, 40)
        stringC = "x" * correct
        assert ch.Password_account.max_character(self, stringC) == True and ch.Password_account.min_character(self,
                                                                                                              stringC) == True
        stringL = "x" * less
        assert ch.Password_account.max_character(self, stringL) == False or ch.Password_account.min_character(self,
                                                                                                              stringL) == False
        stringM = "x" * more
        assert ch.Password_account.max_character(self, stringM) == False or ch.Password_account.min_character(self,
                                                                                                              stringM) == False

    def test_capitalLetter(self):
        length = random.randint(8, 12)
        password = get_random_lowercase_string(length)
        assert ch.Password_account.capital_letter(self, password) == False
        password2 = ''.join(choice((str.upper, str.lower))(c) for c in password)
        assert ch.Password_account.capital_letter(self, password2) == True

    def test_oneDigit(self):
        length = random.randint(8, 12)
        password = get_random_lowercase_string(length)
        numpass = list(password)
        randint = random.randint(0, length - 1)
        numpass[randint] = str(random.randint(0, 9))
        password = ''.join(numpass)
        assert ch.Password_account.digit(self, password) == True

    def test_nonAlpha(self):
        length = random.randint(8, 12)
        password = get_random_lowercase_string(length)
        alphapass = list(password)
        nonAlpha = ["!", "@", "#", "$", "%", "^", "&", "*", "(", ")", "-", "+", "*", "=", "/"]
        randint = random.randint(0, length - 2)
        alphapass[randint] = str(random.choice(nonAlpha))
        alphapass[randint + 1] = str(random.randint(0, 9))
        password = ''.join(alphapass)
        assert ch.Password_account.digit(self, password) == True


def get_random_lowercase_string(length):
    letters = string.ascii_lowercase
    return ''.join(random.choice(letters) for i in range(length))




#This test checks that all the requirements for a valid password are being met
def test_password():
    chk = ch.Password_account()
    assert chk.min_character("onetwoth") == True
    assert chk.min_character("one") == False
    assert chk.max_character("abcedfghjklm") == True
    assert chk.max_character("abcdefghjkrty") == False
    assert chk.capital_letter("Thinh") == True
    assert chk.capital_letter("thinh") == False
    assert chk.digit("hello1") == True
    assert chk.digit("hello") == False
    assert chk.non_alpha("no@") == True
    assert chk.non_alpha("no") == False
