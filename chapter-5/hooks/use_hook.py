import login_module


def my_login_hook(username):
    """
    If there are messages for the user return them
    :param username:
    :type username: str
    :return: None
    :rtype: None
    """
    if user_has_messages(username):
        show_messages(username)


def user_has_messages(name):
    """
    Stub for testing
    :param name:
    :type name: str
    :return: True
    :rtype: Boolean
    """
    return True


def show_messages(name):
    """

    :param name:
    :type name: str
    :return: None
    :rtype: None
    """
    print(f"Yup a message for {name}")

# Set hook to retrieve messages upon login
login_module.set_login_hook(my_login_hook)
# Test login and hook
login_module.login_report( "John Doe", "secret")
