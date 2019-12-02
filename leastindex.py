#arr[i] == i

num =[-5, -3, 2, 3]
'''
#for i in num:
	#print(i)
for i, j in enumerate(num):
	#	print(j)
	if i == j and i < len(num) - 1:
			print(i,j)
'''	
for i in num:
	if i == num.index(i):
		print(i)
		break
	else:
		pass
print('----------------------------')
'''
Good morning! Here's your coding interview problem for today.

This problem was asked by Amazon.

Write a function that takes a natural number as input and returns the number of digits the input has.

Constraint: don't use any loops.
'''
def nat_num(y):
	print(len(list(str(y))))
y = int(input("enter a natural number: "))
nat_num(y)