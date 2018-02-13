import ChainsawDB.utils.database as db
import ChainsawDB.utils.valid as valid


def main_menu():
    menu = """
    1: show jugglers
    2: add juggler
    3: edit juggler
    4: quit
    """
    return menu


def edit_menu():
    menu = """
    1: edit name
    2: edit country
    3: edit catches
    4: delete juggler
    5: cancel
    """
    return menu


def show_menu(menu=None):
    if menu:
        print(menu)
    else:
        print(main_menu())


def get_option(maximum=4):
    choice = input("What option would you like to take? ")
    while True:
        if valid.int_input(choice):
            choice = int(choice)
            if 1 <= choice <= maximum:
                return choice
        choice = input("Please enter a valid number:")


def main_menu_action(action):
    if action == 1:
        show_jugglers()
    elif action == 2:
        add_juggler()
    elif action == 3:
        edit_juggler()
    elif action == 4:
        quit_program()


def edit_menu_action(action, juggler):
    if action == 1:
        db.edit_name(juggler)
    elif action == 2:
        db.edit_country(juggler)
    elif action == 3:
        db.edit_catches(juggler)
    elif action == 4:
        db.delete_juggler(juggler)


def show_jugglers():
    db.get_jugglers()


def add_juggler():
    db.add_juggler()


def edit_juggler():
    juggler = db.edit_juggler()
    show_menu(edit_menu())
    opt = get_option(5)
    edit_menu_action(opt, juggler)


def quit_program():
    pass
