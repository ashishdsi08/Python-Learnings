
class Employee:  
     
    reversedSentence ="" 
    
    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
       


    def ReverseSentence(self, sentence):
        result = ""
        try:
            if sentence is None:
                self.reversedSentence = ""       
            
            myList = sentence.split(" ")        
            #c = myList[10000] 
            for num in range(len(myList)-1,-1,-1):
                result = result + myList[num] 

                if num != 0:
                    result = result + " "        
        except:
            self.reversedSentence  ="Exception Has occured !!! Please Provide correct input"
        self.reversedSentence = result
        return self.reversedSentence

class EmployeeWihoutConstructor:
    name =""
    salary =""

    def __init__(self):
        pass

    def PrintDetails(self):
        print(self.name,self.salary)





class Parent:
    def __init__(self, name, typeofParent, tasks) -> None:
        self.name = name
        self.typeofParent = typeofParent
        self.tasks = tasks

    def PrintDetails(self):
        print(self.name,self.typeofParent)


    def AddPrefrence(self):
        self.Prefernce = "Veg"

class Child(Parent):
    def __init__(self, name, typeofParent, tasks, standard) -> None:        
        super().__init__(name, typeofParent, tasks)
        self.standard = standard


    def AddPrefrence(self):
        super().AddPrefrence()
        self.Prefernce += " Nov- Veg"
        print(self.standard)


    


























































if __name__== "__main__":    
    """empObj1 = Employee("Amit", 100000)
    

    empObj2 = EmployeeWihoutConstructor()
    empObj2.PrintDetails()
    empObj2.name = "Amit"
    empObj2.salary = 1234
    empObj2.PrintDetails()"""
    """empObj2 = Employee("Amit", 100000)
    empObj3 = Employee("Amit", 100000)
    empObj4 = Employee("Amit", 100000)
    empObj5 = Employee("Amit", 100000)


    print(empObj1.name)
    print(empObj1.salary)
    print(empObj1.ReverseSentence("his is my first senctence as an object"))
    print(empObj1.reversedSentence)"""

    print("Object created")


    #parentObj = Parent("Ashish","Father", ['Get Groceries','Pick Up and Drop'])
    #parentObj.PrintDetails()

    
    childObj = Child("Ashish","Child", ['study','play'],"1st standard")
    childObj.PrintDetails()
    childObj.AddPrefrence()
    print(childObj.Prefernce)






