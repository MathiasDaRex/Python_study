# exception = 	events detected during the execution
#				that interrupt the flow of a program

# for this we use try/catch blocks
# we put every "dangerous" code in a try block
# every time you recive user input, can be considered dangerous

try:
    numerator = int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e: # we can display the exception type with "as e", than print it
    print(e)
    print("You can't devide by 0! idiot")
except ValueError as e:
    print(e)
    print("Pls enter only round numbers!")
except Exception as e:
    print(e)
    print("Something went wrong :(")
# first catch the specific exceptions, then for the more common
# last the any other
else : # no exception occured
    print(result)
finally: # this ALWAYS runs, whether or not we catched an exception
    # that's a good opportunity to close open files if you opened them
    print("This will always execute")