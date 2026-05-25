class flight():
    def __init__(self,capacity):
        self.capacity=capacity
        self.passengers=[]

    def add_passengers(self,name):
        if not self.open_seats():
            return False
        self.passengers.append(name)
        return True
    
    def open_seats(self):
        return self.capacity-len(self.passengers)
f1=flight(4)

people=["Akbar","Birbal","Modi","Putin"]
for person in people:
    if f1.add_passengers(person):
        print(f"Added {person} to flight successfully.")
    else:
        print(f"No available seats for {person}")
