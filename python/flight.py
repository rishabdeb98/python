class Flight():
    def __init__(self,capacity):
        self.capacity=capacity
        self.passengers=[]

    def add_passenger(self,name):
        if not self.open_seats():
            return False
        
        self.passengers.append(name)
        return True 
    
    def open_seats(self):
        return self.capacity-len(self.passengers)
    
f1=Flight(3)

people=["Harry","Ron","Harmione","Ginny"]
for person in people:
    success=f1.add_passenger(person)
    if success:
        print(f"Added {person} to flight succesfully.")
    else:
        print(f"No available seats for {person}")    