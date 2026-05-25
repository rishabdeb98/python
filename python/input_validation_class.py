class Temperature:
    def __init__(self,celsius):
        if celsius <-273.15:
            raise ValueError("Temperature below absolute zero is not allowed.")
        self.celsius=celsius

t1=Temperature(-274.15)
print(t1.celsius)