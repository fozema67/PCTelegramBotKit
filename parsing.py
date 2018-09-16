# -*-coding: utf-8-*-

# import csv
import requests
from bs4 import BeautifulSoup

main_url = 'http://www.spbkit.edu.ru/index.php?'
option = 'option=com_timetable'


class pars:
    response = requests.get(main_url + option)
    response.encoding = 'cp1251'
    data = BeautifulSoup(response.text, 'html.parser')

    course1 = data.select('#kursi-1')
    course2 = data.select('#kursi-2')
    course3 = data.select('#kursi-3')
    course4 = data.select('#kursi-4')
    course5 = data.select('#kursi-5')

    # курс 1
    groupe1 = data.select('.timetablediv #groppi-5')
    groupe2 = data.select('.timetablediv #groppi-6')
    groupe3 = data.select('.timetablediv #groppi-7')
    groupe4 = data.select('.timetablediv #groppi-8')
    groupe5 = data.select('.timetablediv #groppi-9')
    groupe6 = data.select('.timetablediv #groppi-10')
    groupe7 = data.select('.timetablediv #groppi-11')
    groupe8 = data.select('.timetablediv #groppi-12')
    groupe9 = data.select('.timetablediv #groppi-13')
    groupe10 = data.select('.timetablediv #groppi-14')
    groupe11 = data.select('.timetablediv #groppi-15')

    # курс 2
    groupe12 = data.select('.timetablediv #groppi-16')
    groupe13 = data.select('.timetablediv #groppi-17')
    groupe14 = data.select('.timetablediv #groppi-18')
    groupe15 = data.select('.timetablediv #groppi-19')
    groupe16 = data.select('.timetablediv #groppi-20')
    groupe17 = data.select('.timetablediv #groppi-21')
    groupe18 = data.select('.timetablediv #groppi-22')

    # курс 3
    groupe19 = data.select('.timetablediv #groppi-23')
    groupe20 = data.select('.timetablediv #groppi-24')
    groupe21 = data.select('.timetablediv #groppi-25')
    groupe22 = data.select('.timetablediv #groppi-26')
    groupe23 = data.select('.timetablediv #groppi-27')
    groupe24 = data.select('.timetablediv #groppi-28')

    data10000 = data.select('.timetablediv #dni-1006')
    monday1171 = data10000[0].getText()

    data10000 = data.select('.timetablediv #dni-1007')
    tuesday1171 = data10000[0].getText()

    data10000 = data.select('.timetablediv #dni-1008')
    wednesday1171 = data10000[0].getText()

    data10000 = data.select('.timetablediv #dni-1009')
    thursday1171 = data10000[0].getText()

    data10000 = data.select('.timetablediv #dni-1010')
    friday1171 = data10000[0].getText()

    data10000 = data.select('.timetablediv #dni-1011')
    saturday1171 = data10000[0].getText()

    data10000 = data.select('.timetablediv #dni-1034')
    monday185 = data10000[0].getText()

    data10000 = data.select('.timetablediv #dni-1035')
    tuesday185 = data10000[0].getText()

    data10000 = data.select('.timetablediv #dni-1036')
    wednesday185 = data10000[0].getText()

    data10000 = data.select('.timetablediv #dni-1037')
    thursday185 = data10000[0].getText()

    data10000 = data.select('.timetablediv #dni-1038')
    friday185 = data10000[0].getText()

    data10000 = data.select('.timetablediv #dni-1039')
    saturday185 = data10000[0].getText()

    # name02 = monday1171[0].getText()

    # понедельник первая группа первый курс
    monday1171 = monday1171.replace("1. 09:00 - 09:45 ", " /n")
    monday1171 = monday1171.replace("2. 09:50 - 10:35 ", " /n")
    monday1171 = monday1171.replace("3. 10:55 - 11:40 ", " /n")
    monday1171 = monday1171.replace("4. 11:45 - 12:30 ", " /n")
    monday1171 = monday1171.replace("5. 13:00 - 13:45 ", " /n")
    monday1171 = monday1171.replace("6. 13:50 - 14:35 ", " /n")
    monday1171 = monday1171.replace("7. 14:45 - 15:30 ", " /n")
    monday1171 = monday1171.replace("8. 15:35 - 16:20 ", " /n")
    monday1171 = monday1171.replace("9. 16:30 - 17:15 ", " /n")
    monday1171 = monday1171.replace("10. 17:20 - 18:05 ", " /n")
    monday1171 = monday1171.replace("11. 18:15 - 19:00 ", " /n")
    monday1171 = monday1171.replace("12. 19:05 - 19:50", " /n")
    monday1171 = monday1171.split("/n")

    for n, i in enumerate(monday1171):
        if i == " ":
            monday1171[n] = "None "

    # вторник первая группа первый курс
    tuesday1171 = tuesday1171.replace("1. 09:00 - 09:45 ", " /n")
    tuesday1171 = tuesday1171.replace("2. 09:50 - 10:35 ", " /n")
    tuesday1171 = tuesday1171.replace("3. 10:55 - 11:40 ", " /n")
    tuesday1171 = tuesday1171.replace("4. 11:45 - 12:30 ", " /n")
    tuesday1171 = tuesday1171.replace("5. 13:00 - 13:45 ", " /n")
    tuesday1171 = tuesday1171.replace("6. 13:50 - 14:35 ", " /n")
    tuesday1171 = tuesday1171.replace("7. 14:45 - 15:30 ", " /n")
    tuesday1171 = tuesday1171.replace("8. 15:35 - 16:20 ", " /n")
    tuesday1171 = tuesday1171.replace("9. 16:30 - 17:15 ", " /n")
    tuesday1171 = tuesday1171.replace("10. 17:20 - 18:05 ", " /n")
    tuesday1171 = tuesday1171.replace("11. 18:15 - 19:00 ", " /n")
    tuesday1171 = tuesday1171.replace("12. 19:05 - 19:50", " /n")
    tuesday1171 = tuesday1171.split("/n")

    for n, i in enumerate(tuesday1171):
        if i == " ":
            tuesday1171[n] = "None "

    # среда первая группа первый курс
    wednesday1171 = wednesday1171.replace("1. 09:00 - 09:45 ", " /n")
    wednesday1171 = wednesday1171.replace("2. 09:50 - 10:35 ", " /n")
    wednesday1171 = wednesday1171.replace("3. 10:55 - 11:40 ", " /n")
    wednesday1171 = wednesday1171.replace("4. 11:45 - 12:30 ", " /n")
    wednesday1171 = wednesday1171.replace("5. 13:00 - 13:45 ", " /n")
    wednesday1171 = wednesday1171.replace("6. 13:50 - 14:35 ", " /n")
    wednesday1171 = wednesday1171.replace("7. 14:45 - 15:30 ", " /n")
    wednesday1171 = wednesday1171.replace("8. 15:35 - 16:20 ", " /n")
    wednesday1171 = wednesday1171.replace("9. 16:30 - 17:15 ", " /n")
    wednesday1171 = wednesday1171.replace("10. 17:20 - 18:05 ", " /n")
    wednesday1171 = wednesday1171.replace("11. 18:15 - 19:00 ", " /n")
    wednesday1171 = wednesday1171.replace("12. 19:05 - 19:50", " /n")
    wednesday1171 = wednesday1171.split("/n")

    for n, i in enumerate(wednesday1171):
        if i == " ":
            wednesday1171[n] = "None "

    # четверг первая группа первый курс
    thursday1171 = thursday1171.replace("1. 09:00 - 09:45 ", " /n")
    thursday1171 = thursday1171.replace("2. 09:50 - 10:35 ", " /n")
    thursday1171 = thursday1171.replace("3. 10:55 - 11:40 ", " /n")
    thursday1171 = thursday1171.replace("4. 11:45 - 12:30 ", " /n")
    thursday1171 = thursday1171.replace("5. 13:00 - 13:45 ", " /n")
    thursday1171 = thursday1171.replace("6. 13:50 - 14:35 ", " /n")
    thursday1171 = thursday1171.replace("7. 14:45 - 15:30 ", " /n")
    thursday1171 = thursday1171.replace("8. 15:35 - 16:20 ", " /n")
    thursday1171 = thursday1171.replace("9. 16:30 - 17:15 ", " /n")
    thursday1171 = thursday1171.replace("10. 17:20 - 18:05 ", " /n")
    thursday1171 = thursday1171.replace("11. 18:15 - 19:00 ", " /n")
    thursday1171 = thursday1171.replace("12. 19:05 - 19:50", " /n")
    thursday1171 = thursday1171.split("/n")

    for n, i in enumerate(thursday1171):
        if i == " ":
            thursday1171[n] = "None "
    # пятница первая группа первый курс
    friday1171 = friday1171.replace("1. 09:00 - 09:45 ", " /n")
    friday1171 = friday1171.replace("2. 09:50 - 10:35 ", " /n")
    friday1171 = friday1171.replace("3. 10:55 - 11:40 ", " /n")
    friday1171 = friday1171.replace("4. 11:45 - 12:30 ", " /n")
    friday1171 = friday1171.replace("6. 13:50 - 14:35 ", " /n")
    friday1171 = friday1171.replace("5. 13:00 - 13:45 ", " /n")
    friday1171 = friday1171.replace("7. 14:45 - 15:30 ", " /n")
    friday1171 = friday1171.replace("8. 15:35 - 16:20 ", " /n")
    friday1171 = friday1171.replace("9. 16:30 - 17:15 ", " /n")
    friday1171 = friday1171.replace("10. 17:20 - 18:05 ", " /n")
    friday1171 = friday1171.replace("11. 18:15 - 19:00 ", " /n")
    friday1171 = friday1171.replace("12. 19:05 - 19:50", " /n")
    friday1171 = friday1171.split("/n")

    for n, i in enumerate(friday1171):
        if i == " ":
            friday1171[n] = "None "

    # суббота первая группа первый курс
    saturday1171 = saturday1171.replace("1. 09:00 - 09:45 ", " /n")
    saturday1171 = saturday1171.replace("2. 09:50 - 10:35 ", " /n")
    saturday1171 = saturday1171.replace("3. 10:55 - 11:40 ", " /n")
    saturday1171 = saturday1171.replace("4. 11:45 - 12:30 ", " /n")
    saturday1171 = saturday1171.replace("6. 13:50 - 14:35 ", " /n")
    saturday1171 = saturday1171.replace("5. 13:00 - 13:45 ", " /n")
    saturday1171 = saturday1171.replace("7. 14:45 - 15:30 ", " /n")
    saturday1171 = saturday1171.replace("8. 15:35 - 16:20 ", " /n")
    saturday1171 = saturday1171.replace("9. 16:30 - 17:15 ", " /n")
    saturday1171 = saturday1171.replace("10. 17:20 - 18:05 ", " /n")
    saturday1171 = saturday1171.replace("11. 18:15 - 19:00 ", " /n")
    saturday1171 = saturday1171.replace("12. 19:05 - 19:50", " /n")
    saturday1171 = saturday1171.split("/n")

    for n, i in enumerate(saturday1171):
        if i == " ":
            saturday1171[n] = "None "

    # понедельник 185 группа
    monday185 = monday185.replace("1. 09:00 - 09:45 ", " /n")
    monday185 = monday185.replace("2. 09:50 - 10:35 ", " /n")
    monday185 = monday185.replace("3. 10:55 - 11:40 ", " /n")
    monday185 = monday185.replace("4. 11:45 - 12:30 ", " /n")
    monday185 = monday185.replace("5. 13:00 - 13:45 ", " /n")
    monday185 = monday185.replace("6. 13:50 - 14:35 ", " /n")
    monday185 = monday185.replace("7. 14:45 - 15:30 ", " /n")
    monday185 = monday185.replace("8. 15:35 - 16:20 ", " /n")
    monday185 = monday185.replace("9. 16:30 - 17:15 ", " /n")
    monday185 = monday185.replace("10. 17:20 - 18:05 ", " /n")
    monday185 = monday185.replace("11. 18:15 - 19:00 ", " /n")
    monday185 = monday185.replace("12. 19:05 - 19:50", " /n")
    monday185 = monday185.split("/n")

    for n, i in enumerate(monday185):
        if i == " ":
            monday185[n] = "None "

    # вторник 185 группа
    tuesday185 = tuesday185.replace("1. 09:00 - 09:45 ", " /n")
    tuesday185 = tuesday185.replace("2. 09:50 - 10:35 ", " /n")
    tuesday185 = tuesday185.replace("3. 10:55 - 11:40 ", " /n")
    tuesday185 = tuesday185.replace("4. 11:45 - 12:30 ", " /n")
    tuesday185 = tuesday185.replace("5. 13:00 - 13:45 ", " /n")
    tuesday185 = tuesday185.replace("6. 13:50 - 14:35 ", " /n")
    tuesday185 = tuesday185.replace("7. 14:45 - 15:30 ", " /n")
    tuesday185 = tuesday185.replace("8. 15:35 - 16:20 ", " /n")
    tuesday185 = tuesday185.replace("9. 16:30 - 17:15 ", " /n")
    tuesday185 = tuesday185.replace("10. 17:20 - 18:05 ", " /n")
    tuesday185 = tuesday185.replace("11. 18:15 - 19:00 ", " /n")
    tuesday185 = tuesday185.replace("12. 19:05 - 19:50", " /n")
    tuesday185 = tuesday185.split("/n")

    for n, i in enumerate(tuesday185):
        if i == " ":
            tuesday185[n] = "None "

    # среда 185 группа
    wednesday185 = wednesday185.replace("1. 09:00 - 09:45 ", " /n")
    wednesday185 = wednesday185.replace("2. 09:50 - 10:35 ", " /n")
    wednesday185 = wednesday185.replace("3. 10:55 - 11:40 ", " /n")
    wednesday185 = wednesday185.replace("4. 11:45 - 12:30 ", " /n")
    wednesday185 = wednesday185.replace("5. 13:00 - 13:45 ", " /n")
    wednesday185 = wednesday185.replace("6. 13:50 - 14:35 ", " /n")
    wednesday185 = wednesday185.replace("7. 14:45 - 15:30 ", " /n")
    wednesday185 = wednesday185.replace("8. 15:35 - 16:20 ", " /n")
    wednesday185 = wednesday185.replace("9. 16:30 - 17:15 ", " /n")
    wednesday185 = wednesday185.replace("10. 17:20 - 18:05 ", " /n")
    wednesday185 = wednesday185.replace("11. 18:15 - 19:00 ", " /n")
    wednesday185 = wednesday185.replace("12. 19:05 - 19:50", " /n")
    wednesday185 = wednesday185.split("/n")

    for n, i in enumerate(wednesday185):
        if i == " ":
            wednesday185[n] = "None "

    # четверг 185 группа
    thursday185 = thursday185.replace("1. 09:00 - 09:45 ", " /n")
    thursday185 = thursday185.replace("2. 09:50 - 10:35 ", " /n")
    thursday185 = thursday185.replace("3. 10:55 - 11:40 ", " /n")
    thursday185 = thursday185.replace("4. 11:45 - 12:30 ", " /n")
    thursday185 = thursday185.replace("5. 13:00 - 13:45 ", " /n")
    thursday185 = thursday185.replace("6. 13:50 - 14:35 ", " /n")
    thursday185 = thursday185.replace("7. 14:45 - 15:30 ", " /n")
    thursday185 = thursday185.replace("8. 15:35 - 16:20 ", " /n")
    thursday185 = thursday185.replace("9. 16:30 - 17:15 ", " /n")
    thursday185 = thursday185.replace("10. 17:20 - 18:05 ", " /n")
    thursday185 = thursday185.replace("11. 18:15 - 19:00 ", " /n")
    thursday185 = thursday185.replace("12. 19:05 - 19:50", " /n")
    thursday185 = thursday185.split("/n")

    for n, i in enumerate(thursday185):
        if i == " ":
            thursday185[n] = "None "

    # пятница 185 группа
    friday185 = friday185.replace("1. 09:00 - 09:45 ", " /n")
    friday185 = friday185.replace("2. 09:50 - 10:35 ", " /n")
    friday185 = friday185.replace("3. 10:55 - 11:40 ", " /n")
    friday185 = friday185.replace("4. 11:45 - 12:30 ", " /n")
    friday185 = friday185.replace("6. 13:50 - 14:35 ", " /n")
    friday185 = friday185.replace("5. 13:00 - 13:45 ", " /n")
    friday185 = friday185.replace("7. 14:45 - 15:30 ", " /n")
    friday185 = friday185.replace("8. 15:35 - 16:20 ", " /n")
    friday185 = friday185.replace("9. 16:30 - 17:15 ", " /n")
    friday185 = friday185.replace("10. 17:20 - 18:05 ", " /n")
    friday185 = friday185.replace("11. 18:15 - 19:00 ", " /n")
    friday185 = friday185.replace("12. 19:05 - 19:50", " /n")
    friday185 = friday185.split("/n")

    for n, i in enumerate(friday185):
        if i == " ":
            friday185[n] = "None "

    # суббота 185 группа
    saturday185 = saturday185.replace("1. 09:00 - 09:45 ", " /n")
    saturday185 = saturday185.replace("2. 09:50 - 10:35 ", " /n")
    saturday185 = saturday185.replace("3. 10:55 - 11:40 ", " /n")
    saturday185 = saturday185.replace("4. 11:45 - 12:30 ", " /n")
    saturday185 = saturday185.replace("6. 13:50 - 14:35 ", " /n")
    saturday185 = saturday185.replace("5. 13:00 - 13:45 ", " /n")
    saturday185 = saturday185.replace("7. 14:45 - 15:30 ", " /n")
    saturday185 = saturday185.replace("8. 15:35 - 16:20 ", " /n")
    saturday185 = saturday185.replace("9. 16:30 - 17:15 ", " /n")
    saturday185 = saturday185.replace("10. 17:20 - 18:05 ", " /n")
    saturday185 = saturday185.replace("11. 18:15 - 19:00 ", " /n")
    saturday185 = saturday185.replace("12. 19:05 - 19:50", " /n")
    saturday185 = saturday185.split("/n")

    for n, i in enumerate(saturday185):
        if i == " ":
            saturday185[n] = "None "

# print(pars.saturday1171)