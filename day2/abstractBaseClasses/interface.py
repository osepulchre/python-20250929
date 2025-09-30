import abc

class Interface(abc.ABC):
    __methods__=["__len__"]
    @classmethod
    def __subclasshook__(cls, subclass):
        print(cls)
        print(subclass)
        print(subclass.__mro__)
        print(cls.__methods__)
        if cls is Interface:
            if all(any(method in B.__dict__ for B in subclass.__mro__) for method in cls.__methods__):
                return True
        return False

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

print(issubclass(Iterable, Interface))
print(issubclass(Sized, Interface))