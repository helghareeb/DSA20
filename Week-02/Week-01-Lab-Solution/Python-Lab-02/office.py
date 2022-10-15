# بسم الله الرحمن الرحيم

class Office:
    
    employees_num = 0

    @staticmethod
    def change_emps_num(num):
        Office.employees_num = num

    @staticmethod
    def calculate_lateness(target_hour, move_hour, distance, velocity):
        travel_time = distance / velocity
        arrive_hour = move_hour + travel_time
        if arrive_hour <= target_hour:
            return False
        else:
            return True
    
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.employees = []

    def get_all_employees(self):
        return self.employees

    def get_employee(self, emp_id):
        for employee in self.employees:
            if employee.id == emp_id:
                return employee

    def hire(self, employee):
        self.employees.append(employee)

    def fire(self, emp_id):
        idx = None
        for idx, employee in enumerate(self.employees):
            if employee.id == emp_id:
                self.employees.pop(idx)

    def deduct(self, emp_id, deduction):
        for employee in self.employees:
            if employee.id == emp_id:
                employee.salary -= deduction

    def reward(self, emp_id, reward_amount):
        for employee in self.employees:
            if employee.id == emp_id:
                employee.salary += reward_amount

    def check_lateness(self, emp_id, move_hour):
        if Office.calculate_lateness(move_hour=8, target_hour=9, distance=20, velocity=90):
            self.deduct(emp_id, 10)
        else:
            self.reward(emp_id, 10)
