x= 20
if 0<x and x>10:
	print('tes')
else:
	print('nor')
print('------------')
#recursion
import time
def count_down(x):
	time.sleep(2.4)
	if x <= 0:
		print('mask off')
	else:
		print(x)
		count_down(x-1)

count_down(int(input('starting value for coundown: ')))
print('--------------------')
import time
def favorite_line(a,y):
	time.sleep(1)
	if y <= 0:
		return
	print(a)
	favorite_line(a,y-1)
	
a= 'I want you to be happier'
y= 6
favorite_line(a,y)