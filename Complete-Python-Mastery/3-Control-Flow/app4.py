high_income = True
good_credit = True
# if high_income == True and good_credit == True:
if high_income and good_credit:
    print("Eligible")
# Eligible


high_income = False
good_credit = True
if high_income and good_credit:
    print("Eligible")
else:
    print("not Eligible")
# not Eligible


high_income = False
good_credit = True
if high_income or good_credit:
    print("Eligible")
else:
    print("not Eligible")
# Eligible


is_student = True

if not is_student:
    print("Eligible")
else:
    print("not Eligible")
# not Eligible


high_income = False
good_credit = True
is_student = False

if (high_income or good_credit) and not is_student:
    print("Eligible")
else:
    print("not Eligible")
# Eligible
