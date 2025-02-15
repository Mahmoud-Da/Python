[1, 2, 3]


browsing_session = []
browsing_session.append(1)
browsing_session.append(2)
browsing_session.append(3)
print(browsing_session)
# [1, 2, 3]
last = browsing_session.pop()
print(last)
# 3

print(browsing_session)
# [1, 2]

print("redirect", browsing_session[-1])
# redirect 2

# Falsy values
0
""
[]

not []
# True


if not browsing_session:
    print("disable the back Button")

# Operation on Stacks
browsing_session.append(1)
browsing_session.pop()
if not browsing_session:
    browsing_session[-1]
