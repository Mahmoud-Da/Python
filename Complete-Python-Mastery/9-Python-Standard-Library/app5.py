from pathlib import Path
from zipfile import ZipFile

# zip_file = ZipFile("files.zip", "w")

# for path in Path("ecommerce").rglob("***"):
#     zip_file.write(path)

# zip.close()


# with ZipFile("files.zip", "w") as zip_file:
#     for path in Path("ecommerce").rglob("***"):
#         zip_file.write(path)


with ZipFile("files.zip") as zip_file:
    print(zip_file.namelist())

    info = zip_file.getinfo("ecommerce/__init__.py")
    print(info)
    print(info.file_size)
    print(info.compress_size)
    zip_file.extractall("extract")

# ['ecommerce/shopping/',
#  'ecommerce/sales.py',
#  'ecommerce/__init__.py',
#  'ecommerce/__pycache__/',
#  'ecommerce/customer/',
#  'ecommerce/shopping/sales.py',
#  'ecommerce/shopping/__init__.py',
#  'ecommerce/shopping/__pycache__/',
#  'ecommerce/__pycache__/__init__.cpython-313.pyc',
#  'ecommerce/customer/__init__.py',
#  'ecommerce/customer/__pycache__/',
#  'ecommerce/customer/contact.py',
#  'ecommerce/customer/__pycache__/contact.cpython-313.pyc',
#  'ecommerce/customer/__pycache__/__init__.cpython-313.pyc',
#  'ecommerce/shopping/__pycache__/sales.cpython-313.pyc',
#  'ecommerce/shopping/__pycache__/__init__.cpython-313.pyc']


# <ZipInfo filename='ecommerce/__init__.py' filemode='-rw-r--r--' file_size=31>

# 31
# 31
