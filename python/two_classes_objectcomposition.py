class Engine:
    def __init__(self,horsepower):
        self.horsepower=horsepower
class car:
    def __init__(self,brand,engine):
        self.brand=brand
        self.engine=engine
e1=Engine(150)
c1=car("Lamborgini",e1)
print(c1.engine.horsepower)