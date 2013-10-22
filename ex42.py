## Animal is-a object (yes, sort of confusing) look at the extra credit
class Animal(object):
    pass

## Dog is-a animal-object
class Dog(Animal):

    def __init__(self, name):
        ## class Dog has-a init that takes self and name parameters 
        self.name = name

## cat is-a animal object
class Cat(Animal):

    def __init__(self, name):
        ## Class cat has-a init that takes self and name parameters 
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self, name):
        ## class person has-a init that takes self and name parameters
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

## Employee is-a person object 
class Employee(Person):

    def __init__(self, name, salary):
        ## class employee has-a init that takes self and salaryhmm what is this strange magic?
        super(Employee, self).__init__(name)
        ## defines salary 
        self.salary = salary

## fish is-a object
class Fish(object):
    pass

## salmon is a fish object
class Salmon(Fish):
    pass

## cHalibut is a fish object
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is-a cat
satan = Cat("Satan")

## mary is-a person
mary = Person("Mary")

## mary has a pet satan (is -a cat)
mary.pet = satan

## frank is-a employee and employee has-a frank (an employee)
frank = Employee("Frank", 120000)

## frank has a pet rover (is-a dog)
frank.pet = rover

## flipper is a fish object
flipper = Fish()

## cruise is a salmon object  which is a fish object
crouse = Salmon()

## harry is a halibut which is-a fish object
harry = Halibut()