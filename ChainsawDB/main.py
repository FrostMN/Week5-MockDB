import ChainsawDB.utils.database as sql
import ChainsawDB.utils.logging as log
import ChainsawDB.utils.ui as ui


def main():
    sql.init_db()
    run = True

    while run:
        ui.show_menu()
        action = ui.get_option(4)
        ui.main_menu_action(action)
        if action == 4:
            run = False


if __name__ == '__main__':
    log.start()
    main()
