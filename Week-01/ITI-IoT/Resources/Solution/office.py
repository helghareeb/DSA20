from personAndEmp import Employee
class Office:
    employeesNumber=0
    def __init__(self, name, employees):
        self.name = name
        self.employees = employees
    @property
    def employees(self):
        return self.__employees
    @employees.setter
    def employees(self,employees):
        for i in employees:
            if isinstance(i,Employee):
                self.employeesNumber += 1
    def get_all_employees(self):
        return employeesNumber
    def get_employee(self):
        pass
    def hire(self):
        pass
    def fire(self):
        pass
    def calculate_lateness(self):
        pass
    def deduct(self):
        pass
    def reward(self):
        pass
