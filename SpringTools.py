import math
import sys

mmin = 25.4
ptd = 100
gh = .4

def continue_value():
    cont = input("Would you like to continue?\n>")
    if cont == "yes" or cont == "Yes" or cont == "YES":
        print("\n")
    else:
        sys.exit('Program Terminated')

def in_to_mm():
    intomm = float(input("Enter the value you'd like to convert:\n>"))
    print(intomm * mmin)
    continue_value()

def mm_to_in():
    mmtoin = float(input("Enter the value you'd like to convert:\n>"))
    print(mmtoin / mmin)
    continue_value()

def process_calculator():
    pass

def index():
    valueod = float(input("Enter your spring O.D:\n>"))
    wiresz = float(input("Enter your wire size:\n>"))
    indexone = valueod - wiresz
    finalindex = indexone / wiresz
    if 0 <= finalindex <= 5:
        print("Spring has a 5% index.")
    elif 5.0000001 <= finalindex <= 10:
        print("Spring has a 10% index.")
    elif 10.0000001 <= finalindex <= 15:
        print("Spring has a 15% index.")
    elif 15.0000001 <= finalindex <= 20:
        print("Spring has a 20% index.")
    else:
        print("Spring has a index greater than 20%")
    continue_value()

def arbor_grind():
    valueod = float(input("Enter your spring O.D:\n>"))
    wiresz = float(input("Enter your wire size:\n>"))
    indexone = valueod - wiresz
    finalindex = indexone / wiresz
    index_decimal = finalindex / ptd
    fuck_yes = valueod * index_decimal
    grindh = valueod - fuck_yes
    grindw = grindh * gh
    print("Maximum arbor height is: " + str(grindh))
    print("Maximum arbor width is: " + str(grindw))

for answer in input("Program running, would you like to continue?\n>"):
    if answer in "NONono":
        sys.exit('Program Terminated')
    else:
        selection = input("\nAvailible Tools:\nIN to MM\nMM to IN\nCalculate Index\nArbor Calculator\n\nEnter the tool you'd like to use:\n>")

        if selection == "IN to MM" or selection == "in to mm":
            in_to_mm()

        elif selection == "MM to IN" or selection == "mm to in":
            mm_to_in()

        elif selection == "Calculate Index" or selection == "calculate index":
            index()

        elif selection == "Arbor Calculator" or selection == "arbor calculator":
            arbor_grind()