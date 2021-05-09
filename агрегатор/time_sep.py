import bs4, requests
from igrm import *
from dtf import *
from vg import *

def sep_time():  
    dtf_dt = dtf_date_time()
    dtf_d = []
    dtf_t = []

    vg_dt = vg_date_time()
    vg_d = []
    vg_t = []
    
    igrm_dt = igrm_date_time()
    igrm_d = []
    igrm_t = []

    for item in dtf_dt:
        item = str(item)
        item = item[0:-3]
        item = item.split("|")
        dtf_d.append(item[0])
        dtf_t.append(item[1])

    for item in vg_dt:
        item = str(item)
        item = item.split("|")
        vg_d.append(item[0])
        vg_t.append(item[1])
    
    for item in igrm_dt:
        item = str(item)
        item = item.split("|")
        igrm_d.append(item[0])
        igrm_t.append(item[1])
    
    del dtf_d[10:]
    del dtf_t[10:]
    del vg_d[10:]
    del vg_t[10:]
    del igrm_d[10:]
    del igrm_t[10:] 