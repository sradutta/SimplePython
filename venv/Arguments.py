"""
The user_info function shows the use of positional arguments
"""
def user_info(name, age, city):
    print("{} is {} years old and lives in {}".format(name,age,city))


user_info("Sra", 40, "Boonton")

"""
user_info2 shows the use of default arguments; 
or what is known as key-word arguments
"""
def user_info2(name, age=0, city="NYC"):
    print("{} is {} years old and is from {}".format(name,age,city))

user_info2("Sra")
user_info2(age=56, name='Kadeem')

# This function shows the use of *args
def add(*args):
    print("The sum is {}".format(sum(args)))

add(2, 3, 5)

#This function shows thse use of **kwards
def application(**kwargs):
    print(kwargs)

application(name="Sra", age=2, city = 'NYC')

#This function shows the use of all types of arguments
def jobapplication(fname, lname, type, *args, **kwargs):
    print("{} {} has applied for a {} position. ".format(fname,lname,type))
    print(args, kwargs)

jobapplication("Sra", "Dutta", "remote", 'sradutta@gmail.com', 'QA/Data Engineering', date="May 2022")