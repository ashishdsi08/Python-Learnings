class Employee:
    
    EmployeeCount = 0

    def __init__(self,id,Name,Salary,Leaves) :
        self.id = id
        self.name=Name
        self.salary=Salary
        self.leaves=Leaves
        self.EmployeeCount = self.EmployeeCount + 1
        self.OrgName = "Radical Technologies"
        Employee.EmployeeCount = Employee.EmployeeCount + 1
        

    def applyleaves(self,startdate,enddate):
        pass

    def reviewwithmanager(self):
        pass



class EmployeeManager(Employee):
    
    

    def __init__(self,id,Name,Salary,Leaves):
        super().__init__(id,Name,Salary,Leaves)
        self.EmployeesReporting = []
        self.EmployeesReportingDict = {}
        

    def AddEmployee(self,employee:Employee):

        if employee not in self.EmployeesReporting:
            self.EmployeesReporting.append(employee)
        else:
            print("Employee is already reporting to me in the list !!!")

        if employee.id not in self.EmployeesReportingDict.keys():
            self.EmployeesReportingDict[employee.id] = employee
        else:
            print("Employee is already reporting to me!!!")
        

    def DelEmployee(self,employee:Employee):
        if employee in self.EmployeesReporting:
            self.EmployeesReporting.remove(employee)
        else:
            print("Employee is not reporting to me !!!")

        if employee.id in self.EmployeesReportingDict.keys():
            self.EmployeesReportingDict.pop(employee.id)
        else:
            print("Employee is not reporting to me  !!!")

    def EmployeeWithMaxSalary(self):
        maxEmployeeWithSal = 0
        employyeId =-1
        for employee in self.EmployeesReporting:
            if employee.salary >maxEmployeeWithSal:
                maxEmployeeWithSal = employee.salary
                employyeId = employee.id
        print("Employee with Max Salary is having Id : ", employyeId )
        print("Employee's Max Salary is  : ", maxEmployeeWithSal )
        return self.EmployeesReportingDict[employyeId]       
            

if __name__ == "__main__" :

    emp1 = Employee(1,"Ashish",10000,10)
    emp2 = Employee(2,"Tejas",20000,12)
    emp3 = Employee(3,"Amit",30000,5)
    emp4 = Employee(4,"Bhaskar",40000,15)
    emp5 = Employee(5,"Ashish",50000,12)
    emp5.applyleaves()
    

    empManager = EmployeeManager(6,"Aman",60000,20)


    print(emp1.EmployeeCount)
    print(Employee.EmployeeCount)
    


    empManager.AddEmployee(emp1)
    empManager.AddEmployee(emp2)
    empManager.AddEmployee(emp3)
    empManager.AddEmployee(emp4)
    empManager.AddEmployee(emp5)

    empManager.applyleaves()
    empManager.reviewwithmanager()

    for employee in empManager.EmployeesReporting:
        print("Employee with name :", employee.name )

    empManager.EmployeeWithMaxSalary()

    print(empManager.EmployeesReporting)

        






