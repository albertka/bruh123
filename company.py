
"""
File: company.py
Name:

Company employee simulation to learn how to use classes in Python
Concepts covered: Classes

Base:       Company (hire, fire, show employess), Employee
Extensions:     Add employee.company, format showEmployees better
"""

class Company:
    def __init__(self, name):
       self.name = name
       self.employeelist = []
    
    def hire(self, employee):
       self.employeelist.append(employee)
        
    def fire(self, employee):
       self.employeelist.remove(employee)
    
    def showEmployees(self):
       for employee in self.employeelist:
           print (employee.name)
        
class Employee:
    def __init__(self, name):
       self.name = name
        

def test():
    #Initilize objects
    Google = Company("Google")
    Johhny = Employee("Johhny")
    Olivia = Employee("Olivia")
    
    #Testing classes
    assert Google.name == "Google"
    assert Johhny.name == "Johhny"
    Google.hire(Johhny)
    Google.showEmployees()
    assert Google.employeelist[0]==Johhny
    Google.hire(Olivia)
    Google.showEmployees()
    assert Google.employeelist[0]==Johhny
    assert Google.employeelist[1]==Olivia
    Google.fire(Johhny)
    Google.showEmployees()
    assert Google.employeelist[0]==Olivia
    Google.fire(Olivia)
    Google.showEmployees()
    assert len(Google.employeelist) == 0
    

if __name__ == "__main__":
    test()
    print("Program success!")
