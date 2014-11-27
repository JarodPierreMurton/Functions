# Jarod Pierre Murton
# functions improvement exercise
# times-table tester
import random


    
# Questions

def questions():
    testTable = int(input("Which times-table do you want to be tested on? "))
    return testTable

# Inputted asnwers

def input_answers(testTable):
    for count in range(1,6):
        Num1 = testTable
        Num2 = random.randrange(2,13)
        Ans = Num1 * Num2
        UserAnswer = int(input(str(Num1) + " x " + str(Num2) + " =  "))
        if UserAnswer == Ans:
            print('Well done, you got the correct answer!')
            print()
        else:
            print('Sorry, you got the answer wrong. The correct answer is',Ans)
            print()
              
# main program

print("Times-Table Tester")
print()
questions()
input_answers()
