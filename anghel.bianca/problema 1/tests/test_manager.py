from employee import Employee
from employee import Manager
import pytest


@pytest.fixture(autouse=True)  # e o functie care se apeleaza inainte si dupa fiecare test si face count = 0
def reseteaza_numar_angajati_si_manageri():
    Employee.empCount = 0
    Manager.mgrCount = 0
    yield
    Employee.empCount = 0
    Manager.mgrCount = 0


def test1():
    mngr = Manager("Ion Popescu", 5000, "HR")  # crearea unui obiect de tip Manager
    assert mngr.name == "Ion Popescu"  # verificam daca numele este cel corect
    assert mngr.salary == 5000  # verificam daca salariul este cel corect
    assert mngr.tasks == {}  # verificam daca lista de task-uri este goala
    assert mngr.department == "F07HR"  # verificam daca departamentul este cel corect
    assert Employee.empCount == 1  # verificam daca numarul de angajati este 1
    assert Manager.mgrCount == 1  # verificam daca numarul de manageri este 1


def test2():
    mngr = Manager("Ion Popescu", 5000, "HR")  # crearea unui obiect de tip Manager
    mngr2 = Manager("Vasile Ionescu", 4500, "IT")  # crearea unui obiect de tip Manager
    assert mngr.empCount == 2  # verificam daca numarul de angajati este 2
    assert mngr.mgrCount == 2  # verificam daca numarul de manageri este 2


def test3():
    mngr = Manager("Ion Popescu", 5000, "HR")  # crearea unui obiect de tip Manager
    mngr2 = Manager("Vasile Ionescu", 4500, "IT")  # crearea unui obiect de tip Manager
    mngr3 = Manager("George Popa", 4000, "Finance")  # crearea unui obiect de tip Manager
    emp = Employee("Mihai Pop", 4700)  # crearea unui obiect de tip Employee
    assert mngr.empCount == 4  # verificam daca numarul de angajati este 4
    assert mngr.mgrCount == 3  # verificam daca numarul de manageri este 3


def test4():
    mngr = Manager("Ion Popescu", 5000, "HR")  # crearea unui obiect de tip Manager
    mngr.update_salary(6000)  # apelarea metodei update_salary
    assert mngr.salary == 6000  # verificam daca salariul a fost actualizat


def test5():
    mngr = Manager("Ion Popescu", 5000, "HR")  # crearea unui obiect de tip Manager
    mngr.modify_task("Task1")  # apelarea metodei modify_task
    mngr.modify_task("Task2", "In progress")  # apelarea metodei modify_task
    mngr.modify_task("Task3", "Done")  # apelarea metodei modify_task
    assert mngr.tasks == {"Task1": "New", "Task2": "In progress", "Task3": "Done"}  # verificam daca lista de task-uri este corecta
