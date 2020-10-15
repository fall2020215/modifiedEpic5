""" 
request_friend.py file has:
class Pending_Friend: store information of a request such as Request_name, Pending_name
"""
class Pending_Friend:
    def __init__(self, request_name, pending_name):
        self.__request_name= request_name
        self.__pending_name = pending_name      

    def get_request_name(self):
        return self.__request_name

    def get_pending_name(self):
        return self.__pending_name



