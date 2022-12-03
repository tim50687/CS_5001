# dataclass(cls = None, *, init = True, repr = True, eq = True, order = False, unsafehash = False, frozen = False)
# frozen property is immutable
# field (*, default = missing, default_facory = missing, init = True, repr = True, hash = None, compare= True, metadata = None)
# compare - if the property is compared or not

from dataclasses import dataclass, field, asdict, astuple


def get_default_age():
    ages = [11, 11, 11, 11]
    return sum(ages) // len(ages)


@dataclass(order=True, frozen=True, unsafe_hash=True)
class Person:
    name: str
    age: int = field(
        default_factory=get_default_age,
        init=False,
        repr=True,
        hash=False,
        metadata={"format": "year"},
    )
    city: str = field(default="taiwan")


p = Person("tim")
p1 = Person("tim", "taipei")
# p.name = "hhh"
print(
    p.__dataclass_fields__["age"].metadata["format"]
)  # provide all the field that dataclass is managing
print(p1)
print(p)


@dataclass
class Person1:
    name: str
    city: str
    age: int
    # can be obtain by age itself
    is_senior: bool = field(init=False)
    # you don't want to pass in, get the value bt post init

    def __post_init__(self):  # do beforee init
        if self.age >= 60:
            self.is_senior = True
        else:
            self.is_senior = False


x = Person1("tim", "taipei", 25)
print("is_senior")
print(x)

# inheeritance
@dataclass
class Student(Person1):
    grade: int
    subjects: list


# s = Student("tin", "taipei", 20, 10, True, ["math", "chinese"])
# print(s)


@dataclass
class A:
    x: int = 10
    y: int = 20


@dataclass
class B(A):
    z: int = 30
    x: int = 40


b = B()


@dataclass
class Address:
    lat: float
    lng: float
    city: str
    country: str


@dataclass
class Person2:
    name: str
    addr: Address
    age: int


a = Address(22, 83, "ttaipei", "India")
p = Person2("tim", a, 22)
print(p.__dataclass_fields__)
