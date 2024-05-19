def user_info(name, age=0, city="enter it"):
    '''this function prints name age city'''
    print("{} is {} years old and lives in {}".format(name, age, city))

user_info("abir", 25, "dhaka")
user_info("life")
user_info("abir", city="dhaka", age=25)

def application(fname, lname,company,email, *args, **kwargs):
    print("{} {} works at {} and his email is {}.".format(fname, lname, company, email))

application("abir","ash","hi@h.com","volo",7500,hire_date="10/10/2020")