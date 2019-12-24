class ccar:
    def __init__(self, name,FuelRate, Velocity):
        self.name = name
        self.FuelRate = FuelRate
        self.Velocity = Velocity
    @property
    def FuelRate(self):
        return self.__FuelRate
    @FuelRate.setter
    def FuelRate(self,FuelRate):
        if(0 <= FuelRate and FuelRate <= 100):
            self.__FuelRate=FuelRate
        else:
            print("it should be between 0:100 ")
    @property
    def Velocity(self):
        return self.__Velocity
    @Velocity.setter
    def Velocity(self,Velocity):
        if(0 <= Velocity and Velocity <= 200):
            self.__Velocity=Velocity
        else:
            print("it should be between 0:200 ")
    def run(self,Velocity,distance):
        self.Velocity=Velocity
        self.FuelRate -=distance
    def stop(self):
        self.Velocity=0
        print("you arrive the destination")
