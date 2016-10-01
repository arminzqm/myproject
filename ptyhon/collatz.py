import sys
def collatz(number):
    if number%2 == 0:
        print('number is: '+str(number)+'. Return '+str(number//2))
        return number//2
    else:
        print('number is: '+str(number)+'. Return '+str(number*3+1))
        return number*3+1


takenTime=0
try:
	n=int(input('please input one number: '))
except ValueError:
	print('should input a number.')
	sys.exit()
inp=n

while n != 1:
	n=collatz(n)
	takenTime +=1
print('input number is: '+str(inp)+', after '+str(takenTime)+' operation, the result become 1')
sys.exit()

    
