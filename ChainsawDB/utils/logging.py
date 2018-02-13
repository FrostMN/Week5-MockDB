import logging
import time
import datetime


logging.basicConfig(filename='ChainsawDB.log', level=logging.INFO)


def write(msg):
    logging.info(msg=msg)


def start():
    date = datetime.datetime.fromtimestamp(time.time()).strftime('%Y-%m-%d %H:%M:%S')
    write("\n\nStarting {} at {}.\n".format("ChainsawDB", date))

