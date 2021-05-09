import bs4, requests
from igrm import *
from dtf import *
from vg import *
from sorting import quicksort
import datetime
import operator

def fresher():

    now = datetime.datetime.now()
    time = now.strftime("%H:%M")
    date = now.strftime("%d.%m.%Y")
    dtf_t = dtf_time()   
    vg_t = vg_time()  
    igrm_t = igrm_time() 

    dtf_d = dtf_date()   
    vg_d = vg_date()  
    igrm_d = igrm_date() 

    t_list1 = []
    t_list2 = []
    tarray = vg_t + igrm_t + dtf_t   
    darray = vg_d + igrm_d + dtf_d

    tarray.append(time)
    darray.append(date)

    dt = dict(zip(tarray, darray))

    sorted_tuples = sorted(dt.items(), key=operator.itemgetter(1))
    s_dt = {k: v for k, v in sorted_tuples}
    cnt = 1


    for key in s_dt:
        if dt[key] == date:
            d1 = dict(list(s_dt.items())[cnt:])
            d2 = dict(list(s_dt.items())[:cnt-1])
            break
        else:
            cnt = cnt + 1

    for item in d1:
        t_list1.append(item)

    for item in d2:
        t_list2.append(item)
    t_list1 = quicksort(t_list1)
    t_list2 = quicksort(t_list2)
    
    arr = t_list2 + t_list1

    return arr