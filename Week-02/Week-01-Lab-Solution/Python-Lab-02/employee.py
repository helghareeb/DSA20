# بسم الله الرحمن الرحيم

from person import Person

class Employee(Person):
    
    def __init__(self, name, car, email, distance_to_work, *args, **kwargs):
        super().__init__(name, *args, **kwargs)
        self.id = None
        self.car = car
        self.email = email
        self.health_rate = 100
        self.salary = 2000
        self.distance_to_work = distance_to_work

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary):
        assert salary >= 1000
        self.__salary = salary

    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email):
        assert '@' in email
        assert '.' in email
        assert len(email) > 7
        self.__email = email

    @property
    def health_rate(self):
        return self.__health_rate

    @health_rate.setter
    def health_rate(self, rate):
        assert  0 <= rate <= 100
        self.__health_rate = rate

    def work(self, hours):
        if hours == 8:
            return Person.moods[0]
        elif hours > 8:
            return Person.moods[1]
        elif hours < 8:
            return Person.moods[2]
        

    def drive(self, distance, velocity):
        #TODO calculate velocity
        self.car.run(distance, velocity)

    def refuel(self, gas_amount = 100):
        self.car.fuel_rate += gas_amount

    def send_mail(self, to, subject, msg, receiver_name):
        with open('email', 'w') as f:
            f.write(f'''From: {self.email}
            To: {to}

            Hi, {receiver_name}
            This is an email template
            thanks
            ''')
    def __repr__(self):
        return f'Employee Name: {self.name}'