# Test program by Jeff Lee
age = input("What is your age? ")
s1 = "You are {0} years old."
s2 = "In 5 years you will be {0} years old."
print(s1.format(age))
print(s2.format(int(age) + 5))
print("And in 100 years yopu will die.")
