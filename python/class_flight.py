class Laptop:
    def __init__(self,brand,ram_gb):
        self.brand=brand
        self.ram_gb=ram_gb
#creating an object
s1=Laptop("Lenovo",16)
print(s1.brand) #output:Lenovo
print(s1.ram_gb) #output:16