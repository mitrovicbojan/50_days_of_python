from machines.vehicle_stuff import Vehicle, Truck, Motorcycle

truck1 = Truck("Big Rig", "Mercedes")
car1 = Vehicle("Sedan", "Chevy")
moto1 = Motorcycle("Sports", "Honda")

for vehicle in [truck1, car1, moto1]:
    vehicle.drive()
    
def preform_tasks(vehicle_object):
    vehicle_object.drive()
    

######
print("#############")
print("Dunder Method")
print("#############")
####
class Employee:
    def __init__(self,name, age):
        self.name = name
        self.age = age
        
    def __str__(self):
        return self.name + " age is " + str(self.age)
    
    def __len__(self):
        return self.age
        
tom = Employee("tom smith", 47)

print(tom)

mylist = [1,2,3,4]
print(mylist)

print(len(tom))