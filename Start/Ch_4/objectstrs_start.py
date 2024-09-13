# Example file for Advanced Python: Language Features by Joe Marini
# customize string representations of objects


class Person():
    def __init__(self):
        self.fname = "Joe"
        self.lname = "Marini"
        self.age = 25

    # TODO: use __repr__ to create a string useful for debugging
    def __repr__(self) -> str:
        return f"<Person Class - {self.fname}, lname: {self.lname}, age :{self.age} >"
    # TODO: use str for a more human-readable string
    def __str__(self) -> str:
        return f"Person {self.fname} is {self.age}"
    
    def __bytes__(self):
        val = f"Person: {self.lname}"
        return bytes(val.encode("utf-32"))

# create a new Person object
cls1 = Person()

# use different Python functions to convert it to a string
print(repr(cls1))
print(str(cls1))
print(f"Formatted: {cls1}")
print(bytes(cls1))
