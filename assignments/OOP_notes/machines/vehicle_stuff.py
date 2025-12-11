class Vehicle:
    vehicle_counter = 0
    
    def __init__(self, body_type, make):
        self.vehicle_body = body_type
        self.vehicle_make = make
        Vehicle.vehicle_counter += 1
        
    def get_vehicle_count(self):
        return Vehicle.vehicle_counter
    
    