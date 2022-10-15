# بسم الله الرحمن الرحيم

class Person:

    moods = ('Happy', 'Tired', 'Lazy')

    def __init__(self, name, *args, **kwargs):
        self.name = name
        self.money = 0
        self.mood = None
        # self.health_rate = None
    
    def sleep(self, hours):
        if hours == 7:
            return moods[0]
        elif hours < 7:
            return moods[1]
        elif hours > 7:
            return moods[2]

    def eat(self, meals):
        assert meals in [1,2,3]
        if meals == 3:
            self.health_rate = 100
        elif meals == 2:
            self.health_rate = 0.75
        elif meals == 1:
            self.health_rate = 0.5

    def buy(self, *items):
        no_items = len(items)
        self.money = self.money - ( 10 * no_items )
