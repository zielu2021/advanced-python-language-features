# Example file for Advanced Python: Language Features by Joe Marini
# Demonstrate the use of lambda functions


# TODO: define a function that takes variable arguments
def addition(*args):
    result = 0
    for arg in args:
        result += arg
    return result

# TODO: pass different arguments
print(addition(5, 10,15,20))
print(addition(5, 2, 3, 4))

# TODO: pass an existing list
my_nums = [5, 10,15,20]
print(addition(*my_nums))
