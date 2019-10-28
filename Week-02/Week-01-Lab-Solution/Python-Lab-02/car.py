# بسم الله الرحمن الرحيم

class Car:
    
    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.fuel_rate = 0
        self.velocity = 0

    @property
    def velocity(self):
        return self.__velocity

    @velocity.setter
    def velocity(self, velocity):
        assert 0 <= velocity <= 200
        self.__velocity = velocity

    @property
    def fuel_rate(self):
        return self.__fuel_rate

    @fuel_rate.setter
    def fuel_rate(self, fuel):
        assert 0 <= fuel <= 100
        self.__fuel_rate = fuel

    def run(self, distance, velocity):
        original_fuel_rate = self.fuel_rate
        self.velocity = velocity
        self.fuel_rate -= distance if self.fuel_rate >= distance else 0
        if self.fuel_rate:
            stop(distance)
        else:
            stop(original_fuel_rate)
            

    def stop(self, remaining_distance):
        if remaining_distance == 0:
            self.velocity = 0
            print('We arrived safely')
        elif self.fuel_rate == 0:
            self.velocity = 0
            print('We ran out of Fuel and had to Stop!')