
def Fibonacci (n):
	if n < 0:
		print("value is too small")
	elif n == 1:
		return (0)
	elif n == 2:
		return (1)
	else:
		return Fibonacci(n-1) + Fibonacci(n-2)
print(Fibonacci(9))

Fibonacci(9)
print('_--------------------------')

def Ackermann (m,n):
	if m == 0:
		return (n + 1)
	elif m > 0 and n == 0:
		return Ackermann(m-1, 1)
	elif m > 0 and n > 0:
		return Ackermann((m-1), Ackermann (m, n-1))
m = int(input("Enter a value for m: "))
n =  int(input("Enter a value for n: "))
print(Ackermann(m,n))