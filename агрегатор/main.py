#приложение для получения игровых новостей и обзоров со множества  игровых порталов

#используемые игровые порталы:
#1) DTF - https://dtf.ru/
#2) PLAYGROUND - https://www.playground.ru/
#3) MAIL.RU GAMES - https://games.mail.ru/
#4) KANOBU - https://kanobu.ru/
#5) IGROMANIA - https://www.igromania.ru/
#6) XYZ - https://media-xyz.com/ru
#7) STOPGAME - https://stopgame.ru/
#8) VG TIMES - https://vgtimes.ru/
#9) RIOT PIXELS - http://riotpixels.com/
#10) GAMER INFO - https://gamer-info.com/

#тестовый функционал: импорт ссылок на новости индустрии
from progress.bar import IncrementalBar
import time, sys
import bs4, requests
from igrm import *
from dtf import *
from vg import *
from fresh import fresher

checker = ""

#основной модуль
while checker!= "exit":
    checker = str(input("Добро пожаловать! Новости с какого сайта ВЫ хотели бы узнать([D]dtf/[I]igromania/[V]VG times):"+"\n"))

#IGROMANIA
    if checker == "I":

        name_arr = igrm_names()
        link_arr = igrm_links()
        content_arr = igrm_content()
        date_time_arr = igrm_date_time()
        i = 0

        for item in name_arr:
            print(" "+item,"\n",date_time_arr[i],"\n", link_arr[i],"\n", content_arr[i],"\n")
            i = i + 1
#DTF
    if checker == "D":
        name_arr = dtf_names()
        link_arr = dtf_links()
        content_arr = dtf_content()
        date_time_arr = dtf_date_time()
        i = 0

        for item in name_arr:
            print(item,"\n", date_time_arr[i],"\n",link_arr[i],"\n", content_arr[i],"\n")
            i = i + 1
#VG
    if checker == "V":
        name_arr = vg_names()
        link_arr = vg_links()
        date_time_arr = vg_date_time()
        content_arr = vg_content()
        i = 0

        for item in name_arr:
            print(" "+item,"\n", date_time_arr[i],"\n", link_arr[i],"\n", content_arr[i],"\n")
            #print(" "+item,"\n", link_arr[i],"\n")
            i = i + 1
#fresh  
    if checker == "S":
        earr = []
        arr = fresher()
        bar = IncrementalBar('Countdown', max = len(arr)+2)

        v_name = vg_names()
        v_link = vg_links()
        v_time = vg_time()
        v_content = vg_content()

        bar.next()
        time.sleep(1)

        d_name = dtf_names()
        d_link = dtf_links()
        d_content = dtf_content()
        d_time = dtf_time()

        bar.next()
        time.sleep(1)

        i_name = igrm_names()
        i_link = igrm_links()
        i_content = igrm_content()
        i_time = igrm_time()

        bar.next()
        time.sleep(1)

        i = 0
        j = 0
        k = 0 
        o = 0

        while i < 29:

            if arr[i] == d_time[j]:

                str_ = " "+d_name[j]+"\n"+d_time[j]+"\n"+ d_link[j]+"\n"+ d_content[j]+"\n"  
                earr.append(str_)      
                i = i + 1
                j = 0
                k = 0
                o = 0
                bar.next()
                time.sleep(1)
            else:
                j = j + 1

            if arr[i] == i_time[k]:

                str_ = " "+i_name[k]+"\n"+ i_time[k]+"\n"+ i_link[k]+"\n"+ i_content[k]+"\n"  
                earr.append(str_) 
                i= i + 1
                k = 0
                o = 0
                j = 0
                bar.next()
                time.sleep(1)
            else:
                k = k + 1

            if arr[i] == v_time[o]:

                str_ = " "+v_name[o]+"\n"+ v_time[o]+"\n"+ v_link[o]+"\n"+ v_content[o]+"\n"  
                earr.append(str_) 
                i = i + 1
                o = 0
                j = 0
                k = 0
                bar.next()
                time.sleep(1)
            else:
                o = o + 1

        bar.finish()

        for item in earr:
            print(item)

    checker = str(input("Продолжить или выйти(exit/continue):"+"\n"))

    

