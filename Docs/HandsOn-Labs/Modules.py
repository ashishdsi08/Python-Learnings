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

employeeObj = demoModule.Employee("Ashish",10000)
result = employeeObj.ReverseSentence("Reverse this sendtence")

print(result)

