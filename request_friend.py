""" 
student.py file has:
class Student: store information of a student such as first name, last name, password, ....
"""
class Request_Friend:
    def __init__(self, request_name, pending_name):
        self.__request_name= request_name
        self.__pending_name = pending_name      

    def get_request_name(self):
        return self.__request_name

    def get_pending_name(self):
        return self.__pending_name



