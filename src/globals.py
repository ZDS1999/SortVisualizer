from enum import Enum

DEBUG = True
RET_FLAG = False


def dprint(content):
    if DEBUG:
        print(content)


class SortWith(Enum):
    BUBBLE = 0
    SELECT = 1
    INSERT = 2
    SHELL  = 3
    MERGE  = 4
    QUICK  = 5
    HEAP   = 6
