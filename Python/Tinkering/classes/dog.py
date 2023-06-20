class Dog:
    """A simple attempt to model a dog."""

    def __init__(self, name, age):
        """Initialize name and age attributes"""
        self.name = name
        self.age = age

    def sit(self):
        """Simulate a dog sitting in response to a command"""
        print(f"{self.name} is now sitting.")

    def roll_over(self):
        """Simulate rolling over in response to a command"""
        print(f"{self.name} rolled over!")

def test_class_attribute(my_object):
    print("\n")
    print(f"My dog's name is {my_object.name}.")
    print(f"My dog is {my_object.age} years old.")
    my_object.sit()
    my_object.roll_over()

your_dog = Dog("Lucy", 3)
my_dog = Dog("Willie", 6)

test_class_attribute(my_dog)
test_class_attribute(your_dog)

