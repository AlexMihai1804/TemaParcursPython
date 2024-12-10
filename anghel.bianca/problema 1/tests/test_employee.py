import pytest  # importam pytest, folosit pentru a rula testele
from employee import Employee


@pytest.fixture(autouse=True)  # e o functie care se apeleaza inainte si dupa fiecare test si face count = 0
def reseteaza_numarul_angajati():
    Employee.empCount = 0
    yield
    Employee.empCount = 0


def test1():
    emp = Employee("Barbu", 5000)  # crearea unui obiect de tip Employee
    assert emp.name == "Barbu"  # verificam daca numele este cel corect
    assert emp.salary == 5000  # verificam daca salariul este cel corect
    assert emp.tasks == {}  # verificam daca lista de task-uri este goala
    assert Employee.empCount == 1  # verificam daca numarul de angajati este 1


def test2():
    emp = Employee("Barbu", 5000)  # crearea unui obiect de tip Employee
    emp2 = Employee("Ion", 6000)  # crearea unui obiect de tip Employee
    assert emp.empCount == 2  # verificam daca numarul de angajati este 2


def test3():
    emp = Employee("Barbu", 5000)  # crearea unui obiect de tip Employee
    emp2 = Employee("Ion", 6000)  # crearea unui obiect de tip Employee
    emp3 = Employee("Vasile", 7000)  # crearea unui obiect de tip Employee
    assert emp.empCount == 3  # verificam daca numarul de angajati este 3


def test4():
    emp = Employee("Barbu", 5000)  # crearea unui obiect de tip Employee
    emp.update_salary(6000)  # apelarea metodei update_salary
    assert emp.salary == 6000  # verificam daca salariul a fost actualizat


def test5():
    emp = Employee("Barbu", 5000)  # crearea unui obiect de tip Employee
    emp.modify_task("Task1")  # apelarea metodei modify_task
    emp.modify_task("Task2", "In progress")  # apelarea metodei modify_task
    emp.modify_task("Task3", "Done")  # apelarea metodei modify_task
    assert emp.tasks == {"Task1": "New", "Task2": "In progress", "Task3": "Done"}  # verificam daca lista de task-uri este corecta
