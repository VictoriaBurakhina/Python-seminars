# Задача 3.Возьмите задачу о банкомате из семинара 2. Разбейте её
# на отдельные операции — функции. Дополнительно сохраняйте все операции поступления и снятия средств в список.

BANKTAX = 1.015
BANKTAXMIN = 30
BANKTAXMAX = 600
BANKPERCENT = 1.03
COUNTRYTAX = 1.1
RICH = 5000000

logDict = {}


# Меню
def menu():
    print('--' * 20)
    print(f'Вывести сумму на счете -  нажмите  1')
    print(f'Снять со счета - нажмите  2')
    print(f'Положить на счет -  нажмите  3')
    print(f'История операций - нажмите 4')
    print('--' * 20)
    print(f'Для выхода нажмите 0')
    print('--' * 20)


# История операций:
def log(logDict, bool, opCount, cash):
    if bool:
        logDict[opCount] = f'на счет положили {cash}'
    else:
        logDict[opCount] = f'со счета снято {cash}'
    return logDict


# Внос средств на счет:
def putIn(money, opCount):
    while True:
        if opCount % 3 == 0: money = money * BANKPERCENT
        print(f'Сколько хотите положить?(кратно 50)')
        moneyIn = int(input(' ->> '))
        if moneyIn % 50 != 0:
            print(f'Введите сумму кратную 50 ')
            continue
        elif moneyIn % 50 == 0:
            money = money + moneyIn
            opCount += 1
            break
    log(logDict, True, opCount, moneyIn)
    return money, opCount


# Снятие средств со счета:
def takeOut(money, opCount):
    printInvoice(money)
    while True:
        if money > RICH:
            money = money - (money - money / COUNTRYTAX)
        print(f'Сколько хотите снять со счета? ')
        outMoney = float(input(' ->> '))
        if outMoney > money:
            print(f'{printInvoice(money)}, введите сумму корректно')
            continue
        if BANKTAXMAX > outMoney - outMoney / BANKTAX > BANKTAXMIN:
            money = money - (outMoney - outMoney / BANKTAX)
            break
        elif BANKTAXMIN > outMoney - outMoney / BANKTAX:
            money = money - (outMoney - BANKTAXMIN)
            if money < 0:
                print(f'Превышен лимит счета, введите сумму заново')
                continue
            break
        else:
            outMoney = outMoney - BANKTAXMAX
            money = money - outMoney - BANKTAXMIN
            if money < 0:
                print(f'Превышен лимит счета, введите сумму заново')
                continue
            break
    opCount += 1
    log(logDict, False, opCount, outMoney)
    return money, opCount


# История операций:
def printLog(logDict):
    for k, v in logDict.items():
        print(k, v)


# Состояние счета:
def printInvoice(money):
    print(f'На Вашем счету - {round(money, 2)} y.e.')


money = 0
opCount = 0
while True:
    menu()
    button = input(' ->> ')
    if button == '1':
        printInvoice(money)
    elif button == '2':
        money, opCount = takeOut(money, opCount)
    elif button == '3':
        money, opCount = putIn(money, opCount)
    elif button == '4':
        printLog(logDict)
    elif button == '0':
        break
    else:
        print(f'Выберите один вариант из предложенных ')
