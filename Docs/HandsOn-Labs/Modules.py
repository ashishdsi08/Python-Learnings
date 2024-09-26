"""
What is a Module?
Consider a module to be the same as a code library.

A file containing a set of functions you want to include in your application.


Create a Module
To create a module just save the code you want in a file with the file extension .py:


Use a Module
Now we can use the module we just created, by using the import statement:

"""
import oops_classes as demoModule
from Employee import Employee,EmployeeManager
#from Employee import *
#import Employee as demoEmployees

#employeeObj = demoModule.Employee("Ashish",10000)
#result = employeeObj.ReverseSentence("Reverse this sendtence")

#print(result)

emp1 = Employee(1,"Ashish",10000,10)
emp2 = Employee(2,"Tejas",20000,12)
emp3 = Employee(3,"Amit",30000,5)
emp4 = Employee(4,"Bhaskar",40000,15)
emp5 = Employee(5,"Ashish",50000,12)

empManager = EmployeeManager(6,"Aman",60000,20)



empManager.AddEmployee(emp1)
empManager.AddEmployee(emp2)
empManager.AddEmployee(emp3)
empManager.AddEmployee(emp4)
empManager.AddEmployee(emp5)

empManager.EmployeeWithMaxSalary()

print(empManager.EmployeesReporting)


"""
for i in range(5):
    emp = Employee(i+1,"Ashish",50000,12)
    empManager.AddEmployee(emp1)
"""







