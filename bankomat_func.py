amount = 0
TAX = 0.015
WEALTH = 5_000_000
WEALTH_TAX = 0.1
THIRD_TAX = 0.03
MULT = 50
global count 
count = 0

def mult(summ):
    if summ % MULT == 0:
        return True
    else:
        return False


def put(summ):
    global count, amount
    count += 1
    if amount > WEALTH:
        amount *= 1 - WEALTH_TAX
    if mult(summ):
        if count == 3:
            amount += summ * THIRD_TAX
            count = 0
        amount  += summ
        return(f"Вы внесли {summ} и на счету теперь {amount:.2f}")
    else:
        return(f"Вы ввели сумму, не кратную {MULT}")


def take(summ):
    global count, amount
    count += 1
    if amount > WEALTH:
        amount *= 1 - WEALTH_TAX
    if mult(summ):
        if amount > summ * (1 + TAX):
            if count == 3:
                amount += summ * THIRD_TAX
                count = 0
            amount  = amount - summ * (1 + TAX)
            return(f"Вы сняли {summ} и на счету теперь {amount:.2f}")
        else:
            return(f"На счету {amount:.2f}. Недостаточно денег, чтобы снять {summ}")
    else:
        return(f"Вы ввели сумму, не кратную {MULT}")

    

def exit():
    global count, amount
    count = 0
    return(f"На счету {amount:.2f}. Выполняется выход.")


while True:
    choice = int(input('Введите 1 для внесения суммы, 2 для снятия суммы, любую другую клавишу для выхода \t'))

    if choice == 1: 
        summ = int(input('Введите сумму для пополнения \t'))
        print(put(summ))

    elif choice == 2:
        summ = int(input('Введите сумму для снятия \t'))
        print(take(summ))

    else:
        print(exit())
        break
