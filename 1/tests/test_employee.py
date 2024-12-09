import pytest # Importam pytest
from employee import Employee # Importam clasa Employee din fisierul employee.py

@pytest.fixture(autouse=True) # Fixture care se apeleaza automat inainte de fiecare test
def reseteaza_numarul_angajati(): # Functie care reseteaza numarul de angajati
    Employee.empCount = 0

def test_creare_angajat(): # cream un test pentru crearea unui angajat
    emp = Employee("John Doe", 50000)
    assert emp.name == "John Doe"
    assert emp.salary == 50000
    assert emp.tasks == {}
    assert Employee.empCount == 1

def test_creare_multiple_angajati(): # cream un test pentru crearea a mai multi angajati
    emp1 = Employee("Alice", 60000)
    emp2 = Employee("Bob", 55000)
    assert Employee.empCount == 2

def test_actualizare_salariu(): # cream un test pentru actualizarea salariului
    emp = Employee("Charlie", 70000)
    emp.update_salary(75000)
    assert emp.salary == 75000

def test_modificare_task(): # cream un test pentru modificarea task-urilor
    emp = Employee("Diana", 65000)
    emp.modify_task("Task1")
    emp.modify_task("Task2", "In Progress")
    assert emp.tasks == {"Task1": "New", "Task2": "In Progress"}

def test_afisare_numar_angajati(capsys): # cream un test pentru afisarea numarului de angajati
    emp1 = Employee("Eve", 80000)
    emp2 = Employee("Frank", 82000)
    emp1.display_emp_count()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Total number of employee(s) is 2"

def test_afisare_angajat(capsys): # cream un test pentru afisarea unui angajat
    emp = Employee("Grace", 90000)
    emp.display_employee()
    captured = capsys.readouterr()
    assert captured.out.strip() == "Name :  Grace , Salary:  90000"

def test_afisare_taskuri(capsys): # cream un test pentru afisarea task-urilor
    emp = Employee("Heidi", 75000)
    emp.modify_task("Task1", "Completed")
    emp.modify_task("Task2", "New")
    emp.display_task("New")
    captured = capsys.readouterr()
    expected_output = "Taskuri cu statusul New\nTask2"
    assert captured.out.strip() == expected_output

def test_modificare_task_fara_status(): # cream un test pentru modificarea unui task fara status
    emp = Employee("Judy", 70000)
    emp.modify_task("Task3")
    assert emp.tasks == {"Task3": "New"}

def test_modificare_task_status_nevalid(): # cream un test pentru modificarea unui task cu un status nevalid
    emp = Employee("Kevin", 72000)
    emp.modify_task("Task4", "InvalidStatus")
    assert emp.tasks == {"Task4": "InvalidStatus"}

def test_afisare_taskuri_fara_taskuri(capsys): # cream un test pentru afisarea task-urilor fara task-uri
    emp = Employee("Laura", 68000)
    emp.modify_task("Task5", "Completed")
    emp.display_task("In Progress")
    captured = capsys.readouterr()
    expected_output = "Taskuri cu statusul In Progress"
    assert captured.out.strip() == expected_output

def test_multiple_taskuri_acelasi_status(capsys): # cream un test pentru task-uri multiple cu acelasi status
    emp = Employee("Mallory", 75000)
    emp.modify_task("Task6", "In Progress")
    emp.modify_task("Task7", "In Progress")
    emp.modify_task("Task8", "Completed")
    emp.display_task("In Progress")
    captured = capsys.readouterr()
    expected_output = "Taskuri cu statusul In Progress\nTask6\nTask7"
    assert captured.out.strip() == expected_output
