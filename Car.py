from Vehicle import Vehicle


class Car(Vehicle):

    def move_left(self, kms):
        self.kms = kms
        super().move_left(self.kms)
        print(f" Car Moved left {self.kms} kms..")

    def move_right(self, kms):
        self.kms = kms
        print(f" Car Moved right {self.kms} kms..")

    def move_front(self, kms):
        self.kms = kms
        print(f"Car Moved front {self.kms} kms..")

    def move_back(self, kms):
        self.kms = kms
        print(f"Car Moved back {self.kms} kms..")


c1 = Car(4)

print(Car.kms)
c1.move_left(15)
c1.fly_low(25)

# print()
