import abc

class Interface(abc.ABC):
#    @classmethod
#    def __subclasshook__(self, subclass):
#        print("check")
#        return True
    pass

class Container(Interface):
    @abc.abstractmethod
    def __contains__(self, item):
        pass

class Sized(Interface):
    @abc.abstractmethod
    def __len__(self):
        pass

class SizedContainer(Sized, Container):
    pass

class Iterable(Interface):
    @abc.abstractmethod
    def __iter__(self):
        pass

try:
    SizedContainer()
except TypeError as te:
    print(f"SizedContainer() failed: {te}")

try:
    Iterable()
except TypeError as te:
    print(f"Iterable() failed: {te}")
