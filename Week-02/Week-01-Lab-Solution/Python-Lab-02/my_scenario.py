# بسم الله الرحمن الرحيم

from person import Person
from employee import Employee
from office import Office
from car import Car

def correct_case():
    fiat128 = Car('Fiat128')
    fiat128.fuel_rate = 100

    samy = Employee('Samy', fiat128, 'samy@iti.org', 20)
    samy.id = 1001
    samy.salary = 2000
    # samy.health_rate = 100

    iti = Office('ITI')
    iti.employees.append(samy)
    
    print(f'ITI Employees: {iti.employees[0]}')
    print(f'Samy Exists in ITI: {samy in iti.get_all_employees()}')
    s = iti.get_employee(1001)
    if s:
        print(f'ID: 1001 exists')
    print(f'EmpID 1001 == Samy: {s == samy}')

    for hr in range(6, 11):
        late = iti.check_lateness(samy.id, hr)
        if late:
            iti.deduct(samy.id, 10)
        else:
            iti.reward(samy.id, 10)
        print(f'Hour: {hr} - Late: {iti.check_lateness(samy.id, hr)} - Salary: {samy.salary}')

    
if __name__ == '__main__':
    correct_case()

    