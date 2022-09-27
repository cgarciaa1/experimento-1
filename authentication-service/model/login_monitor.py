class LoginMonitor:
    def __init__(self, users, max_secuential_attemps_until_block):
        self.__monitored_users___ = users
        self.__max_secuential_attemps_until_block__ = max_secuential_attemps_until_block

    def authenticate_user(self, username, password):
        for user in self.__monitored_users___:
            if user.get_username() == username:
                user_login_tracker = user.get_login_tracker()
                user_login_tracker.increase_total_login_request()

                # if the current user is block, just return fail
                if user.is_blocked():
                    return False
                
                # in case the authentication fails:
                if not user.authenticate(password):
                    # check if the fail count reach the limit, in that case, the user will be blocked
                    if user_login_tracker.get_fail_count() >= self.__max_secuential_attemps_until_block__:
                        user.block()
                        return False
                    # just in case the fail count is not at the limit, increase the fail count
                    user_login_tracker.increase_fail_count()
                    return False
                    
                # the login was success, if there are any login attemp, just reset it
                user_login_tracker.clear_fail_count()
                return True
            # in case the user does not exists, return false
            return False
                    


