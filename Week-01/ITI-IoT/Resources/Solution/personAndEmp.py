import ccar
class Person:
    def __init__(self,name,money,mood,healthRate):
        self.name=name
        self.money=money
        self.mood=mood
        self.healthRate=healthRate
    @property
    def mood(self):
        return self.__mood
    @mood.setter
    def mood(self, mood):
        moods=("happy","tired","lazy")
        if mood in moods:
                self.__mood = mood
    @property
    def healthRate(self):
        return self.__healthRate
    @healthRate.setter
    def healthRate(self, healthRate):
        if( 0 <= healthRate and healthRate <= 100):
            self.__healthRate=healthRate
        else:
            print("enter between 0:100")

    def sleep(self,hours):
        if (hours==7):
            self.mood = "happy"
        elif (hours<7):
            self.mood = "tired"
        else:
            self.mood = "lazy"
    def eat(self,NumMeals):
        if (NumMeals==3):
            self.healthRate = 100
        elif (NumMeals==2):
            self.healthRate = 75
        elif (NumMeals==1):
            self.healthRate = 50
        else:
            print("enter 3 ,2 or 1")
    def buy(self, numOfItems):
        self.money-=(10*numOfItems)

class Employee(Person):
    id1=0
    def __init__(self,name,money,mood,healthRate,car,email,salary,distanceToWork):
        super(Employee, self).__init__(name,money,mood,healthRate)
        self.car = car
        self.email = email
        self.salary = salary
        self.distanceToWork = distanceToWork
    @classmethod
    def makeId(cls):
        cls.id1+=1
        print(cls.id1)
    @property
    def car(self):
        return self.__car
    @car.setter
    def car(self,car1):
        if isinstance(car1,ccar.ccar):
            self.__car=car1
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, salary):
        if (salary >= 1000) :
            self.__salary = salary
        else:
            print("salary must be more than 1000")
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email):
        import re
        if re.match("^[A-Za-z0-9\.\+_-]+@[A-Za-z0-9\._-]+\.[a-zA-Z]*$",email):
            self.__email = email
        else:
            print("email not valid")
    def work(self,hour):
        if (hour==8):
            self.mood = "happy"
        elif (hour>8):
            self.mood = "tired"
        else:
            self.mood = "lazy"
    def drive(self,distance,Velocity):
        self.car.run(Velocity,distance)
    def Refuel(self,gasAmount):
        if (gasAmount==100):
            self.ccar.FuelRate=gasAmount
        else:
            print("you should add 100 ")
    def Send_email(self,to,subject,msg,recevied_name):
        file=open("SendEmail.txt","w")
        file.write("from: "+subject)
        file.write("\nTo: "+to)
        file.write("\nHi, "+recevied_name)
        file.write("\n"+msg)
        file.close()
