import subprocess

# subprocess.call
# subprocess. check_call
# subprocess.check_output
# subprocess.Popen

subprocess.run(["ls"])

# app10.py        app13.py        app16.py        app3.py         app6.py         app9.py         ecommerce       movies.json
# app11.py        app14.py        app17.py        app4.py         app7.py         data.csv        extract         template.html
# app12.py        app15.py        app2.py         app5.py         app8.py         db.sqlite3      files.zip       wrap.txt

subprocess.run(["ls", "-l"])
# total 328
# -rw-r--r--@ 1 mahmouddabbbagh  staff    535 Mar 13 11:36 app10.py
# -rw-r--r--@ 1 mahmouddabbbagh  staff    506 Mar 13 11:49 app11.py
# -rw-r--r--@ 1 mahmouddabbbagh  staff    642 Mar 13 12:05 app12.py
# -rw-r--r--@ 1 mahmouddabbbagh  staff     86 Mar 13 17:17 app13.py
# -rw-r--r--  1 mahmouddabbbagh  staff    683 Mar 13 19:35 app14.py
# -rw-r--r--@ 1 mahmouddabbbagh  staff    748 Mar 13 19:45 app15.py
# -rw-r--r--@ 1 mahmouddabbbagh  staff    326 Mar 13 20:12 app16.py
# -rw-r--r--  1 mahmouddabbbagh  staff    541 Mar 13 20:17 app17.py
# -rw-r--r--@ 1 mahmouddabbbagh  staff    645 Mar  2 21:07 app2.py
# -rw-r--r--@ 1 mahmouddabbbagh  staff   1522 Mar  3 06:28 app3.py
# -rw-r--r--@ 1 mahmouddabbbagh  staff    902 Mar  3 06:49 app4.py
# -rw-r--r--@ 1 mahmouddabbbagh  staff   1289 Mar  3 07:07 app5.py
# -rw-r--r--@ 1 mahmouddabbbagh  staff    579 Mar 13 07:35 app6.py
# -rw-r--r--@ 1 mahmouddabbbagh  staff    641 Mar 13 07:55 app7.py
# -rw-r--r--@ 1 mahmouddabbbagh  staff    860 Mar 13 08:49 app8.py
# -rw-r--r--@ 1 mahmouddabbbagh  staff    233 Mar 13 08:59 app9.py
# -rw-r--r--@ 1 mahmouddabbbagh  staff     55 Mar 13 07:35 data.csv
# -rw-r--r--@ 1 mahmouddabbbagh  staff   8192 Mar 13 08:49 db.sqlite3
# drwxr-xr-x@ 7 mahmouddabbbagh  staff    224 Mar  3 06:28 ecommerce
# drwxr-xr-x@ 3 mahmouddabbbagh  staff     96 Mar  3 07:07 extract
# -rw-r--r--@ 1 mahmouddabbbagh  staff   4315 Mar  3 07:07 files.zip
# -rw-r--r--@ 1 mahmouddabbbagh  staff    102 Mar 13 07:55 movies.json
# -rw-r--r--@ 1 mahmouddabbbagh  staff    268 Mar 13 19:45 template.html
# -rw-r--r--@ 1 mahmouddabbbagh  staff  71005 Mar 13 20:13 wrap.txt

result = subprocess.run(["ls", "-l"])
print(type(result))
# <class 'subprocess.CompletedProcess'>

completed = subprocess.run(["ls", "-l"])
print("args", completed.args)
# ['ls', '-l']

print("returncode", completed.returncode)
# returncode 0

print("stderr", completed.stderr)
# stderr None

print("stdout", completed.stdout)
# stdout None

completed = subprocess.run(["ls", "-l"], capture_output=True)
print("args", completed.args)
# ['ls', '-l']

print("returncode", completed.returncode)
# returncode 0

print("stderr", completed.stderr)
# stderr None

# print("stdout", completed.stdout)
# args ['ls', '-l']
# returncode 0
# stderr b''

print("stdout", completed.stdout)
# stdout b'total 328\

completed = subprocess.run(["ls", "-l"],
                           capture_output=True,
                           text=True)

print("stdout", completed.stdout)
# stdout total 328


completed = subprocess.run(["python3", "other.py"],
                           capture_output=True,
                           text=True)

print("stdout", completed.stdout)
# stdout Here is a complicated script.


completed = subprocess.run(["false"],
                           capture_output=True,
                           text=True)

print("returncode", completed.returncode)
# returncode 1

if completed.returncode != 0:
    print(completed.stderr)


completed = subprocess.run(["false"],
                           capture_output=True,
                           text=True,
                           check=True)
# subprocess.CalledProcessError: Command '['false']' returned non-zero exit status 1.


try:
    completed = subprocess.run(["false"],
                               capture_output=True,
                               text=True,
                               check=True)
except subprocess.CalledProcessError as ex:
    print(ex)
