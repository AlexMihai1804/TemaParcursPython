from employee import Employee
from manager import Manager


def main():
    emp1 = Employee("Zara", 2000)
    emp2 = Employee("Manni", 5000)
    # am creat 2 obiecte de tip Employee
    mgr1 = Manager("John", 50000, "HR")
    mgr2 = Manager("Jane", 60000, "IT")
    mgr3 = Manager("Jack", 70000, "Finance")
    mgr4 = Manager("Jill", 80000, "Marketing")
    mgr5 = Manager("Jen", 90000, "Sales")
    # am creat 5 obiecte de tip Manager
    emp1.display_employee()
    emp2.display_employee()
    # am afisat datele despre cei 2 angajati
    mgr1.display_employee()
    mgr2.display_employee()
    mgr3.display_employee()
    mgr4.display_employee()
    mgr5.display_employee()
    # am afisat datele despre cei 5 manageri
    print(f"Total employee {Employee.empCount}")  # afisam numarul de angajati
    print(f"Total manager {Manager.mgrCount}")  # afisam numarul de manageri


if __name__ == '__main__':
    main()
