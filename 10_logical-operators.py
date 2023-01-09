# logical operators (and, or, not) = used to check if two 
# or more conditional statements are true or false

temp = float(input("Please enter the temperature (c°): "))

if (temp >= 0 and temp <=30):
    print("The temperature is good")
    print("Go outside")
elif temp < 0 or temp > 30:
    print("The temperature is bad today")
    print("Stay inside")
    
# we can flip it with the not operator

#if not(temp >= 0 and temp <=30):
#    print("The temperature is bad today")
#    print("Stay inside")

#elif not(temp < 0 or temp > 30):
#    print("The temperature is good")
#    print("Go outside")
    