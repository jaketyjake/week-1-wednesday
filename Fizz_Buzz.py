# divisible by 3= FIZZ, 5 = BUZZ, or both = FIZZ BUZZ?


number = int(input("Enter a whole number : "))

if number % 3 == 0 and number % 5 == 0:
    print("FIZZ BUZZ")
elif number % 5 ==0:
    print("BUZZ")
elif number % 3 == 0:
    print("FIZZ")
else:
    print("FOOEY")