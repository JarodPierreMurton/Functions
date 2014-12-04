#Jarod Pierre Murton
#Development Excercise Currency Converter
#4/12/14

#pounds to euros
def pounds_euros():
    amount = int(input("Please enter the amount you would like to convert: "))
    total = amount * 1.229
    print("€{0}".format(total))

#pounds to dollars
def pounds_dollars():
    amount = int(input("Please enter the amount you would like to convert: "))
    total = amount * 1.601
    print("${0}".format(total))

#euros to pounds
def euros_pounds():
    amount = int(input("Please enter the amount you would like to convert: "))
    total = amount * 1.302
    print("£{0}".format(total))

#euros to dollars 
def euros_dollars():
    amount = int(input("Please enter the amount you would like to convert: "))
    total = amount * 0.814
    print("${0}".format(total))

#dollars to pounds
def dollars_pounds():
    amount = int(input("Please enter the amount you would like to convert: "))
    total = amount * 0.625
    print("£{0}".format(total))

#dollars to euros
def dollars_euros():
    amount = int(input("Please enter the amount you would like to convert: "))
    total = amount * 0.768
    print("€{0}".format(total))



#Main Program
print("Option 1: £ --> €")
print("Option 2: £ --> $")
print("Option 3: € --> £")
print("Option 4: € --> $")
print("Option 5: $ --> £")
print("Option 6: $ --> €")

typeOfconversion = input("Please select the currency you would like to convert: ")

if typeOfconversion == "1":
    typeOfconversion = pounds_euros()
    
elif typeOfconversion == "2":
    typeOfconversion = pounds_dollars()
    
elif typeOfconversion == "3":
    typeOfconversion = euros_pounds()
    
elif typeOfconversion == "4":
    typeOfconversion = euros_dollars()
    
elif typeOfconversion == "5":
    typeOfconversion = dollars_pounds()
    
elif typeOfconversion == "6":
    typeOfconversion = dollars_euros()

else:
    print("This is not one of the options available")
