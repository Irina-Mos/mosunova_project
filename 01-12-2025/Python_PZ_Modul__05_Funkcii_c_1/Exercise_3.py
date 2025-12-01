def picture(length, direction, symbol):
    if direction == "horizontal":
        print(symbol * length)
    elif direction == "vertical":
        for i in range(0, length):
            print(symbol, end='\n')
    else:
        print('Invalid input')

picture(7, "vertical", "~")