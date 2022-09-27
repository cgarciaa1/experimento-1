class User:
    def __init__(self, username, password, tracker):
        self.__username__ = username
        self.__password__ = password
        self.__is_blocked__ = False
        self.__login_tracker__ = tracker

    def get_username(self):
        return self.__username__

    def get_login_tracker(self):
        return self.__login_tracker__

    def authenticate(self, incoming_password):
        return self.__password__ == incoming_password      

    def is_blocked(self):
        return self.__is_blocked__
    
    def block(self):
        self.__is_blocked__= True