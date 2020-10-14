""" 
settings.py file has:
class Settings: store information of Controls/settings
"""

class Settings:
    def __init__(self, user, email_notif, sms_notif, targeted_ads, language):
        self.__user = user
        self.__email_notif = email_notif
        self.__sms_notif = sms_notif
        self.__targeted_ads = targeted_ads
        self.__language = language

    def get_user(self):
        return self.__user

    def get_email_notif(self):
        return self.__email_notif

    def get_sms_notif(self):
        return self.__sms_notif

    def get_targeted_ads(self):
        return self.__targeted_ads

    def get_language(self):
        return self.__language