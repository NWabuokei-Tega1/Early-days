#prints the result of multiplying each item of a list by 2
num = [1,2,3,4,5]
for i in range(len(num)): #the list has 5 items
	num[i] = num[i] * 2
	#1 = 1*2-- 2
	#2 = 2*2-- 4
	print(num[i])
print('---------------------------')
#replaces items at specofic indexes with another list
food = ["eggs", "fish", "meat"]
food[0:2] = ["beans", "rice"]
print(food)
print("----------------------------")
#sum of items in a nested list
print("nested sum")
def nested_sum(a):
	num = 0
	for i in range(len(a)):
		if isinstance (a[i],(list,tuple)):
			for j in range(len(a[i])):
				num += a[i][j]
		else:
			num += a[i]
	print(num)
a = [1,2,3,[1]]
nested_sum(a)
print("---------------------")
#Capitalize each word in the list
def caps_on(w):
	for i, item in enumerate (w):
		if isinstance(item,list):
			w[i] = [it.title() for it in item]
		elif isinstance(item, str):
			w[i] = item.title()
	print(w)
w = ["him","her",["them"]]
caps_on(w)
print("--------------------------")
#Takes a list returns the list without first & last values
# Below code reads input from user using map() function  
a = list(map(int,input("\nEnter the numbers seperated by space : ").strip().split()))[:] 
b = []
b.append(a[1:-1])
print("\nList is - ", b)
print("------------------------------")
#dictionary implementation
#prints keys maped to frequency of values
def num (x):
	y = dict()
	for i in x :		
		if i not in y :
			y[i] = 1
		else:
			y[i] += 1
	print(y)
x = "Hipopotamus" #p & o appears twice, hence we expect to get {p: 2, o:2, h: 1, i:1, t:1, a:1, m:1, u:1, s:1}
x = x.lower()
num(x)
print('-------------------------')
#print x such that the keys& values are in alphabetical order
def word (n):
	print(n)
	d = {}
	for letter in set(n):
		d[i] = n.count(i)
n = "pumped Pumpkins"
n = n.replace(" ", "")
n = num(n)
print('--------------------')
#reverse lookup
#here we identify keys given values
def reverse_lookup(dct,val):
	for i in dct:
		if dct[i] == val:
			key = i
			print("The key with value", val, "is", key)
dct = {'alpha': 1, 'beta': 2}
reverse_lookup(dct,2)
''' TUPLES: they are comma seperated, immutable lists '''
t2 = ('a','b','c',)
print(type(t2)) #tells us the type of data t2 has
t3 = tuple("Agege") #python has an inbuilt function called tuple
print(t3)
#tuples can be sliced but an item with certain index cannot be changed
t4 = tuple("More life")
print(t4[1:4])
#t4[3] = "v"
#print(t4)  #prints an error
#we can replace one of the tuples with another tuple
t4 = ("L", "o", "v", "e",) + t4[1:]
print(t4)
#code to split an email address into username & domain name
address = ("mollymay@gmail.com")
username,domain = address.split('@')
print("The mail address is " + address)
print("The address is " + username + " " + "while the domain name is " + domain)
#efficient way of dividing & getting remainder of 2 numbers
x = divmod (8,3)
print("8 divides 3 gives", x[0], " and has a remainder of ", x[1])
#putting '*' infront of an argument enables the function to gather as much items as possible and print as a tuple
def names(*args):
	for i in args:
		print(args * 3)
names('Jean', 'Logan', 'Dickson', 'Harry', 'Clement')
#putting *infront of a sequence of values passes them into a function as multiple arguments
y = (2,9)
print (divmod(*y))
#function called small that takes any number of arguments and returns their sum
def small(*num):
	for i in num:
		print(sum(i))
small(list(map(int,input("enter numbers seperated by space: "). strip().split()))[:])
#zip function combines the contents of 2 or more variables and prints tuples that contain singular elements of each variable
words = ('eat', 'walk', "do", 'come')
num = [1,2,3,4]
letters = 'a', 'b', 'c', 'd'
for i,j,k in zip(words,num,letters):
	print(i,j,k)
#code to print values in a sequence
y = [('a',9, '/'), ('z',8,':')]
for letter, num, sign in y:
	print(letter, num,sign)
#code that prints strings with their index values
for index , element in enumerate("yoghurt"):
	print(index, element)
#dictionary in tuples
#Generating a dictionary from a list of tuples
t1 = [('mama',1), ('Mozambique',2)]
d = dict(t1)
print(d)
#generating a list of tuples from a dictionary
d = {'mama':1, 'Mozambique':2}
t2 = d.items()
print(t2)
for key, value in t2:
	print(key,value)
#using zip
d = dict(zip('xyz', range(4)))
print(d)
#comparing tuples