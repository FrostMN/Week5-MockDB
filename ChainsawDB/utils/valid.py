def int_input(user_input):
    try:
        int(user_input)
        return True
    except ValueError:
        return False
