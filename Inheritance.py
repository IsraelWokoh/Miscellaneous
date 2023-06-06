class Vehicle():
    def __init__(s, owner):
        s.owner
    
    def hello1(s):
        return ('I am a vehicle.')

class Car(Vehicle):
    def __init__(s, reg, wheels, owner):
        s.reg = reg
        s.wheels = wheels
        Vehicle.__init__(s, owner)
    
    def hello2(s):
        return ('I am a car.')
    
if __name__ =='__main__':
    car1 = Car('RA07 ND5', 4, 'Mr Blogs')
    print(car1.hello1())
    print(car1.hello2())
    # Polymorphism: a class takes precedence over another class
        # Overriding: child taking precedence over the parent
    print(Vehicle.owner)
