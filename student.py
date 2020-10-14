""" 
student.py file has:
class Student: store information of a student such as first name, last name, password, ....
"""
class Student:
    def __init__(self, user_name, password, first, last):
        self.__user_name = user_name
        self.__password = password
        self.__first = first
        self.__last = last
        self.__name = first + " " + last
        

    def get_user_name(self):
        return self.__user_name

    def get_first(self):
        return self.__first

    def get_last(self):
        return self.__last

    def get_name(self):
        return self.__name

    def get_password(self):
        return self.__password

    def __str__(self):
        return self.__name

