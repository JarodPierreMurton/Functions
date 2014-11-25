#Jarod Pierre Murton
#functions
#18/11/14


#basic pay

def calculate_basic_pay(hours, pay):
    total = hours * pay
    return total

#overtime

def calculate_overtime_pay(hours, pay):
    total = (hours - 40) * (pay * 1.5) + (pay * 40)
    return total

#total pay

def calculate_total_pay(hours, pay):
    if hours <= 40:
        total = calculate_basic_pay(hours, pay)
        print(total)
    else:
        total = calculate_overtime_pay(hours, pay)
        print(total)

#main program


hours = int(input("Please input the hours you work: "))
pay = int(input("Please input the wages you receive: ")) 

calculate_total_pay(hours,pay)
