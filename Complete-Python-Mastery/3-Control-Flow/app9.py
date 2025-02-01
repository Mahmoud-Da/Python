for number in range(3):
    print("Attempt")

# Attempt
# Attempt
# Attempt

successful = True

for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break

# Attempt
# Successful


successful = False
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and Failed")

# Attempt
# Attempt
# Attempt
# Attempted 3 times and Failed

successful = True
for number in range(3):
    print("Attempt")
    if successful:
        print("Successful")
        break
else:
    print("Attempted 3 times and Failed")

# Attempt
# Successful
