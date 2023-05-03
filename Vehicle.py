class Vehicle:
    kms = 0

    def __init__(self, wheels):
        self.wheels = wheels

    def start_engine(self):
        print("Engine started successfully..")

    def move_left(self, kms):
        self.kms = kms
        print(f"Moved left {self.kms} kms..")

    def move_right(self, kms):
        self.kms = kms
        print(f"Moved right {self.kms} kms..")

    def move_front(self, kms):
        self.kms = kms
        print(f"Moved front {self.kms} kms..")

    def move_back(self, kms):
        self.kms = kms
        print(f"Moved back {self.kms} kms..")

    def fly_high(self, kms):
        self.kms = kms
        print(f"Flying up {self.kms} kms..")

    def fly_low(self, kms):
        self.kms = kms
        print(f"Flying down {self.kms} kms..")

    def land(self):
        print("Landing ...")


# v1 = Vehicle(2)
# v2 = Vehicle(4)
# print(Vehicle.kms)
#
# v1.start_engine()
# v1.move_front(20)
# v1.move_back(10)
# print(v1.kms)

