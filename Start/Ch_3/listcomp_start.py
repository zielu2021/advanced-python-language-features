# Example file for Advanced Python: Language Features by Joe Marini
# Demonstrate how to use list comprehensions


# define two lists of numbers
evens = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
odds = [1, 3, 5, 7, 9, 11, 13, 15, 17, 19]

# TODO: Perform a mapping and filter function on a list
even_squared = list(map(lambda e:e**2,
                        filter(lambda e:e>4 and e<16, evens)))
print(even_squared)

# TODO: Derive a new list of numbers frm a given list
even_squared_comp = [n**2 for n in evens if n > 4 and n < 14]
print(even_squared_comp)

odd_squared_comp = [n**2 for n in odds if n > 3 and n < 17]
print(odd_squared_comp)
# TODO: Limit the items operated on with a predicate condition
