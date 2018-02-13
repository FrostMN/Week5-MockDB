import ChainsawDB.utils.logging as log
import ChainsawDB.utils.valid as valid
# import HelloSQLite.utils.ui as ui
from ChainsawDB.utils.schema import schema
import sqlite3
import os

db_path = "hello.db"


def init_db():
    dbp = db_path
    if not os.path.isfile(dbp):
        log.write("creating db")
        sqlite3.connect(dbp)

        log.write("loading schema")
        for qry in schema:
            execute_query(qry)

    else:
        log.write("db exists")


def execute_query(query, params=()):
    dbp = db_path
    if len(params) > 0:
        with sqlite3.connect(dbp) as db:
            cur = db.cursor()
            try:
                cur.execute(query, params)
                db.commit()
            except sqlite3.Error as e:
                log.write(e)
                db.rollback()
    else:
        with sqlite3.connect(dbp) as db:
            cur = db.cursor()
            try:
                cur.execute(query)
                db.commit()
            except sqlite3.Error as e:
                log.write(e)
                db.rollback()


def get_query_response(query, params=()):
    dbp = db_path
    if len(params) > 0:
        with sqlite3.connect(dbp) as db:
            cur = db.cursor()
            try:
                rs = cur.execute(query, params)
                db.commit()
                rows = rs.fetchall()
                if len(rows) == 1:
                    return rows[0]
                elif len(rows) > 1:
                    return rows
            except sqlite3.Error as e:
                log.write(e)
                db.rollback()
    else:
        with sqlite3.connect(dbp) as db:
            cur = db.cursor()
            try:
                rs = cur.execute(query)
                db.commit()
                rows = rs.fetchall()
                if len(rows) == 1:
                    return rows[0]
                elif len(rows) > 1:
                    return rows
            except sqlite3.Error as e:
                log.write(e)
                db.rollback()


# TODO: make a formatting method
def get_jugglers():
    qry = "SELECT * FROM jugglers ORDER BY catches DESC"
    rs = get_query_response(qry)
    print_jugglers(rs)


def add_juggler():
    name = input("What is the name of the juggler? ")
    country = input("What country is the juggler from?")
    catches = input("How many times did the juggler catch? ")
    while not valid.int_input(catches):
        print("please enter a valid interger: ")
        catches = input("How many times did the juggler catch? ")
    catches = int(catches)
    params = (name, country, catches)
    qry = "INSERT INTO jugglers (name, country, catches) VALUES (?, ?, ?)"
    execute_query(qry, params)


def edit_juggler(jugglers=None):
    if not jugglers:
        jugglers = search_juggler()
    if isinstance(jugglers, list):
        print_jugglers(jugglers)
        return select_juggler(jugglers)
    else:
        print_jugglers(jugglers)
        print("jugglers in db edit jugglers - else")
        print(jugglers)
        j = jugglers

        print(j)

        return j


def search_juggler():
    name = ("%" + input("enter the name of the juggler: ").lower() + "%", )

    qry = "SELECT * FROM jugglers WHERE LOWER( name ) LIKE ?"
    rs = get_query_response(qry, name)

    return rs


def print_jugglers(jugglers):
    if isinstance(jugglers, list):
        ctr = 1
        print("+{}+{}+{}+{}+".format("-" * 6, "-" * 20, "-" * 20, "-" * 20))
        print("|{}|{}|{}|{}|".format("#".center(6), "Name".center(20), "Country".center(20), "Catches".center(20)))
        print("+{}+{}+{}+{}+".format("-" * 6, "-" * 20, "-" * 20, "-" * 20))
        for juggler in jugglers:
            # print(juggler)
            print("|{}|{}|{}|{}|".format(str(ctr).center(6), str(juggler[0]).center(20), str(juggler[1]).center(20), str(juggler[2]).center(20)))
            print("+{}+{}+{}+{}+".format("-" * 6, "-" * 20, "-" * 20, "-" * 20))
            ctr += 1
    else:
        print("+{}+{}+{}+".format("-" * 20, "-" * 20, "-" * 20))
        print("|{}|{}|{}|".format("Name".center(20), "Country".center(20), "Catches".center(20)))
        print("+{}+{}+{}+".format("-" * 20, "-" * 20, "-" * 20))
        print("|{}|{}|{}|".format(str(jugglers[0]).center(20), str(jugglers[1]).center(20), str(jugglers[2]).center(20)))
        print("+{}+{}+{}+".format("-" * 20, "-" * 20, "-" * 20))


def select_juggler(jugglers):
    valid_choice = False
    while not valid_choice:
        choice = input("Pick a juggler by number: (1 - {}) ".format(len(jugglers)))
        if valid.int_input(choice):
            choice = int(choice)
            if 1 <= choice <= len(jugglers):
                valid_choice = True
                return edit_juggler(jugglers[choice - 1])
            print("please make a valid choice")


def edit_name(juggler):
    name = input("Please enter the new name: ")

    qry = "UPDATE jugglers SET name=? WHERE name=?"
    params = (name, format(juggler[0]))
    execute_query(qry, params)


def edit_country(juggler):
    country = input("Please enter the new country: ")

    qry = "UPDATE jugglers SET country=? WHERE name=?"
    params = (country, format(juggler[0]))
    execute_query(qry, params)


def edit_catches(juggler):
    catches = "abc"

    while isinstance(catches, str):
        catches = input("Please enter the new number of catches: ")
        if valid.int_input(catches):
            catches = int(catches)

    qry = "UPDATE jugglers SET catches=? WHERE name=?"
    params = (catches, format(juggler[0]))
    execute_query(qry, params)


def delete_juggler(juggler):
    print("delete: {}".format(juggler[0]))
    qry = "DELETE FROM jugglers WHERE name = ?"
    print(qry)
    params = (format(juggler[0], ))
    print(params)
    execute_query(qry, params)
