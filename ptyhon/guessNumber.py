from random import randint
expect_number=randint(1,21)
num=-1

def judge(number):
    a=number
    if expect_number > a:
        print('Your guess is too low')
    elif expect_number < a:
        print('Your guess is too high')



print('I am thinking a number between 1 to 20.')
while expect_number != int(num):
    num=input('take a guess:')
    judge(int(num))
print('Good job')
