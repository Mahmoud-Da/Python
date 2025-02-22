def calculate_xfactor(age):
    if age <= 0:
        raise ValueError("Age cannot be 0 or less.")
    return 10 / age


calculate_xfactor(-1)

#  File "app6.py", line 7, in <module >
#     calculate_xfactor(-1)
#     ~~~~~~~~~~~~~~~~~ ^ ^ ^ ^
#   File "app6.py", line 3, in calculate_xfactor
#     raise ValueError("Age cannot be 0 or less.")
# ValueError: Age cannot be 0 or less.


try:
    calculate_xfactor(-1)
except ValueError as error:
    print(error)

# Age cannot be 0 or less.
