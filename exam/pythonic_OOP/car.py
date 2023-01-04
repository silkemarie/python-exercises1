class Car:
    def __init__(self, make, model, year, reason):
        self.make = make
        self.model = model
        self.year = year
        self.reason = reason

    def __str__(self):
        return f"{self.year} {self.make} {self.model}: {self.reason}"

my_car = Car("Mitsubishi", "Lancer Evo", 2016, "Because I think the bumper is super cute")
print(my_car)




