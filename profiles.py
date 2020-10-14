class Profiles:
    def __init__(self, user, title, major, university, bio, experience, education):
        self.__user = user
        self.__title = title
        self.__major = major
        self.__university = university
        self.__bio = bio
        self.__experience = experience
        self.__education = education

    def get_user(self):
        return self.__user

    def get_title(self):
        return self.__title

    def get_major(self):
        return self.__major

    def get_university(self):
        return self.__university

    def get_bio(self):
        return self.__bio

    def get_experience(self):
        return self.__experience

    def get_education(self):
        return self.__education