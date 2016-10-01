def zeroDivide():
    print('input one number: ')
    input_number=input()
    return 2 / int(input_number)


try:
    result=zeroDivide()
except ZeroDivisionError:
    print('cannot divide zero')
#print(result)
