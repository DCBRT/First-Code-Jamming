#required parameter function and keyword parameter function
# def my_function(data):
# 	print(data)


# value = input("Enter a data: ")
# my_function(value)

#default parameter function
# def printinfo(name, age=24):
# 	print("Name: {}, Age: {}".format(name, age))

# name = input("Enter your name: ")
# age = input("Enter your age:")
# printinfo(name, age=age)
# printinfo(name)
# printinfo(age) # name=12, age= 24
# printinfo(age=age) # raise error

#variable length arguaments function
def printinfo(*args,**kwargs):

	for i in args:
		print(i)
	print("Name: {}".format(kwargs.get('name')))



printinfo(24, "python",name="shital")
