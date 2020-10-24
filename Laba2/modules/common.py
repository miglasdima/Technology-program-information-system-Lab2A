import datetime
import sys


def get_current_date():
    """
    :return: DateTime object
    """
    return datetime.datetime


def get_current_platform():
    """
    :return: current platform
    """
    return sys.platform

i = 0
while i <= 100:
    if i % 2 == 0:
        print(i)
    i += 1