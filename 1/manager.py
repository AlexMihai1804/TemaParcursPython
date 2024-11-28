from employee import Employee


class Manager(Employee):
    mgrCount = 0

    def __init__(self, name, salary, department):
        Employee.__init__(self, name, salary)
        self.department = 'F07' + department
        Manager.mgrCount += 1

    def display_employee(self):
        # x=8 x%3==2
        print("Department: ", self.department)
