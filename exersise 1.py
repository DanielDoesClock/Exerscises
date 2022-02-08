"""This code determines which of the 2 numbers is the biggest, and can identify
if they are the same. It will also loop, only finishing when the user puts in
the number '0'
Made by Daniel Fraser
04/02/2022"""


number1 = 1
number2 = 1
while number1 != 0 and number2 != 0:
    number1 = int(input("what is the first number? "))
    number2 = int(input("what is the second number? "))
    if number1 > number2:
        print(number1)
    elif number1 < number2:
        print(number2)
    else:
        print("these are the same")

else:
    print("done")
