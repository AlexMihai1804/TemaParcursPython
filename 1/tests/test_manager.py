import pytest
from employee import Employee
from manager import Manager


@pytest.fixture(autouse=True)
def reseteaza_numar_angajati_si_manageri():  # Fixture care se apeleaza automat inainte de fiecare test si reseteaza numarul de angajati si manageri
    Employee.empCount = 0
    Manager.mgrCount = 0


def test_creare_manager(): # cream un test pentru crearea unui manager
    mgr = Manager("Ivan", 120000, "Sales")
    assert mgr.name == "Ivan"
    assert mgr.salary == 120000
    assert mgr.department == "F07Sales"
    assert Employee.empCount == 1
    assert Manager.mgrCount == 1


def test_creare_multiple_manageri(): # cream un test pentru crearea a mai multi manageri
    mgr1 = Manager("Judy", 130000, "HR")
    mgr2 = Manager("Kevin", 125000, "IT")
    assert Employee.empCount == 2
    assert Manager.mgrCount == 2


def test_mostenire_manager(): # cream un test pentru mostenirea clasei Manager din clasa Employee
    mgr = Manager("Laura", 140000, "Marketing")
    assert isinstance(mgr, Employee)
    assert mgr.name == "Laura"
    assert mgr.salary == 140000
    assert mgr.department == "F07Marketing"


def test_afisare_manager(capsys): # cream un test pentru afisarea unui manager
    mgr = Manager("Mallory", 150000, "Finance")
    mgr.display_employee()
    captured = capsys.readouterr()
    expected_output = "Department:  F07Finance"
    assert captured.out.strip() == expected_output


def test_gestionare_taskuri_manager(): # cream un test pentru gestionarea task-urilor de catre un manager
    mgr = Manager("Niaj", 160000, "Operations")
    mgr.modify_task("Revizuire Buget", "In Progress")
    mgr.modify_task("Intalnire Echipa")
    assert mgr.tasks == {"Revizuire Buget": "In Progress", "Intalnire Echipa": "New"}


def test_actualizare_salariu_manager(): # cream un test pentru actualizarea salariului unui manager
    mgr = Manager("Olivia", 170000, "Logistics")
    mgr.update_salary(175000)
    assert mgr.salary == 175000


def test_afisare_manager_fara_angajati(capsys): # cream un test pentru afisarea unui manager fara angajati
    mgr = Manager("Quentin", 190000, "Development")
    assert mgr.tasks == {}
    mgr.display_employee()
    captured = capsys.readouterr()
    expected_output = "Department:  F07Development"
    assert captured.out.strip() == expected_output


def test_manager_update_task(): # cream un test pentru actualizarea unui task de catre un manager
    mgr = Manager("Rachel", 200000, "HR")
    mgr.modify_task("Recruitment Drive", "Scheduled")
    mgr.modify_task("Team Building", "Completed")
    assert mgr.tasks == {"Recruitment Drive": "Scheduled", "Team Building": "Completed"}


def test_manager_multiple_taskuri_acelasi_status(capsys): # cream un test pentru task-uri multiple cu acelasi status de catre un manager
    mgr = Manager("Steve", 210000, "Operations")
    mgr.modify_task("Strategy Meeting", "Planned")
    mgr.modify_task("Budget Planning", "Planned")
    mgr.display_task("Planned")
    captured = capsys.readouterr()
    expected_output = "Taskuri cu statusul Planned\nStrategy Meeting\nBudget Planning"
    assert captured.out.strip() == expected_output
