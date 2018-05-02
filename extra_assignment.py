# convert temp F<->C

temp = float(input("Enter temperature :"))
forc = str(input("Is this temp Farenheit or Celcius? " " type - F or C  :  "))

if forc == 'C':
    print(f"The temperature in Farenheit is {(temp * 1.8 + 32)}")
elif forc == 'c':
    print(f"The temperature in Farenheit is {(temp * 1.8 + 32)}")
elif forc == 'F':
    print(f"The temperature in Celsius is {((temp - 32) * 1.8)}")
elif forc == 'f':
    print(f"The temperature in Celsius is {((temp - 32) * 1.8)}")
else:
    print("try again")

