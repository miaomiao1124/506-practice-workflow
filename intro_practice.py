import pandas as pd
import numpy as np
name='Miaoxuan Zhang'
print(type(name))
age=40
print(type(age))
shopping_list=['milk','fruit','egg','vegetable','bread']
print(type(shopping_list))
patient_info={'name':'Miaoxuan','age':'40','gender':'female'}
print(type(patient_info))

def final_score(exam,assignment):
    if type(exam)!=int or type(assignment)!=int:
        return'Please enter a valid integer'
    else :
        caculation=exam+assignment
    output=caculation
    if caculation>=80:
        print('congratulations, you did it')
    else:
        print('I am sorry, you have to retake the course')
final_score(50,30)
final_score(20,30)
newvar_add_test=50