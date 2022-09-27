class LoginTracker:
    def __init__(self):
        self.__total_login_request__ = 0
        self.__fail_count__ = 0

    def get_fail_count(self):
        return self.__fail_count__

    def increase_fail_count(self):
        self.__fail_count__ += 1

    def clear_fail_count(self):
        self.__fail_count__ = 0

    def increase_total_login_request(self):
        self.__total_login_request__  += 1
