course = "Python Programming"
print(course.upper())
course_capital = course.upper()
print(course_capital)
print(course)

course = "python programming"
print(course.title())

course = "  python programming"
print(course.strip())


course = "python programming  "
print(course.rstrip())

course = "  python programming"
print(course.lstrip())


course = "python programming"
print(course.find("pro"))
print(course.find("p"))
print(course.find("Pro"))


course = "python programming"
print(course.replace("pro", "Pro"))


course = "python programming"
print("pro" in course)


course = "python programming"
print("pro" not in course)
