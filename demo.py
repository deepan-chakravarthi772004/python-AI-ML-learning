class car:
    def __init__(self,carname,no_of_wheel,no_of_airbags,mileage):
        print('this is a constructor')
        self.__no_of_wheel = no_of_wheel
        self.no_of_airbags = no_of_airbags
        self.mileage = mileage
        self.carname = carname

    def __dlt__(self):
        print('this is destructor',self)

    def __str__(self):
        return (self.carname)

    def moveforward (self,speed):
        print('car is moving in the speed of',speed)
    def movebackward (self):
        print('car is moving backward')
#getter
    def get_no_of_wheels(self):
        return self.__no_of_wheel
#setter
    def set_no_of_wheels(self,no_of_wheels):
         self.__no_of_wheel=no_of_wheels


car1 = car('BMW',8,4,19.9)
print(car1.set_no_of_wheels(10))
print(car1.get_no_of_wheels())