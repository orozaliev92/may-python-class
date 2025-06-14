
sum=0
list1 = []

while sum < 100:
    number = int(input("Enter your number: "))
    sum += number
    list1.append(number)
else:
    print("Number is more than 100")

    print(list1)
