age=int(input("Enter your age: "))

if age > 0 and age < 13:
    print("Child")
elif age >= 13 and age < 18:
    print("Teenager")
elif age >= 18 and age < 65:
    print("Adult")
elif age >= 65:
    print("Elder")
else:
    print("Provide right age")