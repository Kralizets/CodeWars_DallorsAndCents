def format_money(amount):
    strResult = "$" + str(amount)
    index = strResult.find('.')

    if (index == -1):
        return strResult + ".00"
    
    if ((len(strResult) - index) == 2):
        return strResult + "0"

    return strResult

number1 = 3
number2 = 3.22
number3 = 3.4
number4 = 0.51

money1 = format_money(number1)
money2 = format_money(number2)
money3 = format_money(number3)
money4 = format_money(number4)