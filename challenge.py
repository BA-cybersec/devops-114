name = input("What is your name?")
age = input("What is your age?")
birth_month = input("what is your birth month?")
birth_day = input("what is your birth day?")
a = 12 - int(birth_month)
b = 31 - int(birth_day)
c = 2022 - int(age)

print("your date of birth is " + str(b) + str(a) + str(c))