from db_code import get_data, delete_data
from send_code import *
import datetime
import time


def date_check():
    d_and_t = str(datetime.datetime.today()).split()
    d = tuple(map(int, d_and_t[0].split("-")))
    a = get_data(d)
    return a


def time_check(res):
    date_and_time_today = str(datetime.datetime.today()).split()
    date_now = str(map(int, date_and_time_today[0].split("-")))
    time_now = date_and_time_today[1][:8]
    for i in res:
        if i[1] >= time_now or i[0] < date_now:
            # if i[4] != "no":
            #     mess(i[4], i[2], i[3])
            if i[5] != "no":
                push(i[2], i[3])
            if i[6] != "no":
                ...


r = date_check()
time_check(r)
