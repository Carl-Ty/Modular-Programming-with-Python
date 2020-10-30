cur_user = None
login_hook = None


def valid_login_pairs(dictionary={'John Doe': "secret"}):
    """

    :param dictionary: valid username password pairs
    :type dictionary: dict
    :return: dictionary
    :rtype: dict
    """
    return dictionary


def set_login_hook(hook):
    """
    Connect a function to retrieve the username at login
    :param hook:
    :type hook: function
    :return: None
    :rtype: None
    """
    global login_hook # 3 hours before I thought to make this global
    login_hook = hook


def login(username, password):
    if is_password_correct(username, password):
        cur_user = username
        if login_hook != None: # now that it is global it is used
            login_hook(username)
        return True
    else:
        return False


def is_password_correct(test_username, test_password):
    return valid_login_pairs().get(test_username, None) == test_password


def logout():
    cur_user = None


def login_report(username, password):
    """
    Report success or failure of a user login

    :param username:
    :type username: str
    :param password:
    :type password: str
    :return: None
    :rtype: None
    """
    if login(username, password):
        print(f"{username} logged in.")
    else:
        print(f"{username} failed to login.")


def main():
    login_pair = "John Doe", "secret"
    login_report(*login_pair)


if __name__ == '__main__':
    main()
