tip=int(input("Enter your tip: "))

if tip == 15:
    print("Standard")
elif tip == 18:
    print("Good")
elif tip == 20:
    print("Great")
elif tip > 20:
    print("My hero")
else:
    print("Wrong number")