import abc
from abc import ABC, abstractmethod


class Parent(ABC):

    def geeks(self):
        print("parent class")


class Child(Parent):
    def geeks(self):
        super().geeks()
        print("child class")


p = Parent()
p.geeks()

c = Child()
c.geeks()

print(__name__)