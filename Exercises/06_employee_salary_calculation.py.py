#• Write code that receives the hours worked
#by an employee and calculates the employee's salary.
#• We consider the number of hours worked
#more than 160 hours in a month as overtime.
#• The maximum overtime hour is 40 hours
#• Overtime pay is half the salary for regular hours.
#• The salary for each hour worked is one hundred thousand tomans.
#Mina Hemmati
x=int(input("Enter the employee's time worked: "))
salary=0
overtime=0
total=0
if x<=160:
    salary=x*100
elif x>160:
    salary=160*100
    overtime=x-160
    if overtime<=40:
        overtime=overtime*50
    elif overtime>40:
        overtime=40*50

total=salary+overtime
print("The salary is ",total)
    
    
    
