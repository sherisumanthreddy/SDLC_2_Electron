import random


def select_random(list_num):
    """Function"""
    length = len(list_num)
    r_int = random.randrange(0, length)
    return list_num[r_int]
