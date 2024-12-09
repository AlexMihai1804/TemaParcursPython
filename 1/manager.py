from employee import Employee  # import clasa Employee din fisierul employee.py


class Manager(Employee):  # clasa Manager mosteneste clasa Employee
    mgrCount = 0  # variabila statica care contorizeaza numarul de manageri

    def __init__(self, name, salary, department):  # constructorul clasei Manager
        Employee.__init__(self, name, salary)  # apelam constructorul clasei parinte
        self.department = 'F07' + department  # adaugam prefixul 'F07' la numele departamentului
        Manager.mgrCount += 1  # incrementam numarul de manageri

    def display_employee(self):  # metoda care afiseaza datele despre manager
        print("Department: ", self.department)  # afisam departamentul
