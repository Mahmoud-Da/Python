import sys

print(sys.argv)
# $ python3 app16.py -a -b -c
# ['app16.py', '-a', '-b', '-c']

if len(sys.argv) == 1:
    print("USAGE: python3 app-py <password>")
else:
    password = sys.argv[1]
    print("Password", password)

# $ python3 app16.py
# USAGE: python3 app-py <password>

# $ python3 app16.py 1234
# Password 1234
