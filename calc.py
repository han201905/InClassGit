def calc(a,b):
    sum = a + b
    difference = a - b
    multiply = a * b
    division = a / b
    _list = [sum, difference, multiply, division]
    sumOfList = 0
    for x in _list:
        sumOfList += x
    print(sumOfList)


