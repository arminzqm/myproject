from random import randint
secrtNumber=randint(1,21)

print('i am thinking a number between 1 to 20')

for guessTimes in range(1,7):

    guessed_number=int(input('take a guess: '))

    if secrtNumber > guessed_number:
        print('your guess is too low')
    elif secrtNumber < guessed_number:
        print('your guess is too high')
    else:
        break

if guessed_number == secrtNumber:
    print('good job, bingo in '+str(guessTimes)+' guesses')
else:
    print ('i am thinking of number '+str(secrtNumber))
