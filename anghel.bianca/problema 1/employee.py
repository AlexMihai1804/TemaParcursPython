class Employee:
    """Common base class for all employees"""
    empCount = 0

    def __init__(self, name, salary):
        self.name = name
        self.salary = salary
        self.tasks = {}
        Employee.empCount += 1

    def display_emp_count(self):
        "Displays the number of employees"
        print(f"Total number of employee(s) is {Employee.emp_count}")

    def display_employee(self):
        print("Name : ", self.name, ", Salary: ", self.salary)

    def __del__ (self):
        Employee.empCount -=1


    def update_salary(self, new_salary):
        self.salary = new_salary

##    def add_task(self, task_name):
##        self.tasks[task_name] = "New"   # needs tasks defined before (in __init__)
##
##    def update_tasks(self, task_name, status):
##        self.tasks[task_name] = status
    def modify_task(self, task_name, status="New"):
        self.tasks[task_name]=status

    def display_task(self, status):
        print(f"Taskuri cu statusul {status}")
        for name in self.tasks.keys():
            if self.tasks[name] == status:
                print(name)

class Manager(Employee): # clasa manager care mosteneste clasa Employee
    mgrCount = 0 # variabila de clasa care contorizeaza numarul de manageri
    # e acceasi pentru toate obiectele de tip Manager
    def __init__(self, name, salary, department): # constructorul clasei Manager cu 3 parametri
        Employee.__init__(self, name, salary) # apelarea constructorului clasei parinte
        self.department = 'F07' + department # variabila department este concatenarea stringului 'F07' cu parametrul department
        Manager.mgrCount += 1 # adaugam 1 la numarul de manageri

    def display_employee(self):
        print("Nume:", self.name) # afisam numele managerului

manager1 = Manager("Ion Popescu", 5000, "HR") # crearea primului manager
manager2 = Manager("Vasile Ionescu", 4500, "IT") # crearea celui de-al doilea manager
manager3 = Manager("George Popa", 4000, "Finance") # crearea celui de-al treilea manager
manager4 = Manager("Mihai Pop", 4700, "Logistics") # crearea celui de-al patrulea manager
manager5 = Manager("Andrei Popescu", 5100, "HR") # crearea celui de-al cincilea manager

manager1.display_employee() # apelarea metodei display_employee pentru primul manager
manager2.display_employee() # apelarea metodei display_employee pentru al doilea manager
manager3.display_employee() # apelarea metodei display_employee pentru al treilea manager
manager4.display_employee() # apelarea metodei display_employee pentru al patrulea manager
manager5.display_employee() # apelarea metodei display_employee pentru al cincilea manager

employee1 = Employee("John Doe", 2000) # crearea primului angajat
employee2 = Employee("Jane Doe", 3000) # crearea celui de-al doilea angajat
employee3 = Employee("Gigel", 2500) # crearea celui de-al treilea angajat

employee1.display_employee() # apelarea metodei display_employee pentru primul angajat
employee2.display_employee() # apelarea metodei display_employee pentru al doilea angajat
employee3.display_employee() # apelarea metodei display_employee pentru al treilea angajat

print("TOTAL EMPLOYEE:", Employee.empCount) # afisarea numarului total de angajati
print("TOTAL MANAGER:", Manager.mgrCount) # afisarea numarului total de manageri