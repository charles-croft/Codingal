from abc import ABC, abstractmethod
class abstract(ABC):
    def print(self, x):
        print("Value:", x)
    @abstractmethod
    def task(self):
        print("Parent class task")
class subclass(abstract):
    def task(self):
        print("Subclass task")
object1 = subclass()
object1.task()
object1.print(20)