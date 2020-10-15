""" 
accept_friend.py file has:
class Accept_Friend: store information of a request such as Request_name, Accept_name
"""
class Accept_Friend:
    def __init__(self, request_name, accept_name):
        self.__request_name= request_name
        self.__accept_name = accept_name      

    def get_request_name(self):
        return self.__request_name

    def get_pending_name(self):
        return self.__accept_name
