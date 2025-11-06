amount = int(input('Enter the amount: '))
val_amount = input('Enter the name of the currency: Ruble, Dollar, Euro, Yuan \n')
if val_amount == 'Ruble':
    val_transfer = input('Enter the name of the currency to transfer: Dollar, Euro, Yuan \n')
    if val_transfer == 'Dollar':
        summa = amount * 0.012289
        print(amount, 'RUB =', summa, 'USD')
    elif val_transfer == 'Euro':
        summa = amount * 0.010665
        print(amount, 'RUB =', summa, 'EUR')
    elif val_transfer == 'Yuan':
        summa = amount * 0.087971
        print(amount, 'RUB =', summa, 'CNY')
    else:
        print('Invalid input')
elif val_amount == 'Dollar':
    val_transfer = input('Enter the name of the currency: Ruble, Euro, Yuan \n')
    if val_transfer == 'Ruble':
        summa = amount * 81.38
        print(amount, 'USD =', summa, 'RUB')
    elif val_transfer == 'Euro':
        summa = amount * 0.867
        print(amount, 'USD =', summa, 'EUR')
    elif val_transfer == 'Yuan':
        summa = amount * 7.12
        print(amount, 'USD =', summa, 'CNY')
    else:
        print('Invalid input')
elif val_amount == 'Euro':
    val_transfer = input('Enter the name of the currency: Ruble, Dollar, Yuan \n')
    if val_transfer == 'Ruble':
        summa = amount * 93.76
        print(amount, 'EUR =', summa, 'RUB')
    elif val_transfer == 'Dollar':
        summa = amount * 1.15
        print(amount, 'EUR =', summa, 'USD')
    elif val_transfer == 'Yuan':
        summa = amount * 8.21
        print(amount, 'EUR =', summa, 'CNY')
    else:
        print('Invalid input')
elif val_amount == 'Yuan':
    val_transfer = input('Enter the name of the currency: Ruble, Dollar, Euro \n')
    if val_transfer == 'Ruble':
        summa = amount * 11.37
        print(amount, 'CNY =', summa, 'RUB')
    elif val_transfer == 'Dollar':
        summa = amount * 0.1405
        print(amount, 'CNY =', summa, 'USD')
    elif val_transfer == 'Euro':
        summa = amount * 0.1219
        print(amount, 'CNY =', summa, 'EUR')
    else:
        print('Invalid input')
else:
    print('Invalid input')