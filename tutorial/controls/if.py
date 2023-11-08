# if-else
name = input("Enter your name: ")

if name == "Coleman":
    print("Yhup! You're the man.")
else:
    print("Nope! You're not who I'm looking for")


print("/n")


# if-elif-else
x = int(input("Please enter an integer: "))

if x < 0:
    x = 0
    print('Negative changed to zero')
elif x == 0:
    print('Zero')
elif x == 1:
    print('Single')
else:
    print('More')


