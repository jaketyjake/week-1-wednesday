#even or odd?
number = int(input("Enter a whole number :"))

def even_odd(number):
    if number % 2 == 0:
        print("It's even!")
    else:
        print("It's odd!!")
even_odd(number)