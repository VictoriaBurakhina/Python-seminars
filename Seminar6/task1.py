#В модуль с проверкой даты добавьте возможность запуска в терминале с передачей даты на проверку.

import calendar

def checkDate():
    text = input('DD.MM.YYYY - >>> ')
    text = text.split('.')
    month = int(text[1])
    days = calendar.monthrange(int(text[2]), int(text[1]))[1] #дней в месяце
    if int(text[0]) <= days and int(text[1])<= 12 :
        print('Нормальная дата')
        return True
    else :
        print('не корректная дата')
        return False

def leapYear(year):
    if calendar.monthrange(year, 2) == 29: return True
    else: return False

if __name__=='__main__':
    checkDate()