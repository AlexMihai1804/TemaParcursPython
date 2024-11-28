from employee import Employee
from manager import Manager


def main():
    # y=16 y/3=5
    emp1 = Employee("Zara", 2000)
    emp2 = Employee("Manni", 5000)
    mgr1 = Manager("John", 50000, "HR")
    mgr2 = Manager("Jane", 60000, "IT")
    mgr3 = Manager("Jack", 70000, "Finance")
    mgr4 = Manager("Jill", 80000, "Marketing")
    mgr5 = Manager("Jen", 90000, "Sales")
    emp1.display_employee()
    emp2.display_employee()
    mgr1.display_employee()
    mgr2.display_employee()
    mgr3.display_employee()
    mgr4.display_employee()
    mgr5.display_employee()
    print(f"Total number of employees is {Employee.empCount}")
    print(f"Total number of managers is {Manager.mgrCount}")


if __name__ == '__main__':
    main()
