#Jarod Pierre Murton
#Functions Revision exercise
#2/12/2014

def Valid_Odd(Number):
    if Number % 2 == 1:
    
        Display_Symbol(Number)
    else:
        print("This is not an odd number")
   

def Display_Symbol(Number):
    asterix = "*"
    centre = Number
    while Number > 0:
        print("{0:^{1}}".format(asterix * Number,centre))
        Number -= 2
#Main Program

Number = int(input("Please input an odd number: "))
Validation = Valid_Odd(Number)

