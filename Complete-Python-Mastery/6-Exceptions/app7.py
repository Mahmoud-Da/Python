from timeit import timeit


def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)


code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)
"""

print("first code= ", timeit(code1, number=10000))

# Age cannot be 0 or less.
# Age cannot be 0 or less.
# Age cannot be 0 or less.
# Age cannot be 0 or less.
# Age cannot be 0 or less.
# Age cannot be 0 or less.
# first code=  0.06886674999987008

code1 = """
def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


try:
    calculate_xfactor(-1)
except ValueError as error:
    pass
"""

print("first code= ", timeit(code1, number=10000))

# first code=  0.002173792000121466


code2 = """
def calculate_xfactor(age):
    if age <= 0:
        return None
    return 10 / age


xfactor = calculate_xfactor(-1)
if xfactor == None:
   pass
"""

print("Second code= ", timeit(code2, number=10000))

# Second code=  0.0007847910001146374
