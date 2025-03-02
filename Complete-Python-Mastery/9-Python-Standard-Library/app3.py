from pathlib import Path

path = Path("ecommerce")
# path.exists()
# path.mkdir()
# path.rmdir()
# path.rename("ecommerce2")

print(path.iterdir())
# <map object at 0x102d8fcd0>

for p in path.iterdir():
    print(p)

# ecommerce/shopping
# ecommerce/sales.py
# ecommerce/__init__.py
# ecommerce/__pycache__
# ecommerce/customer

paths = [p for p in path.iterdir()]
print(paths)
# [PosixPath('ecommerce/shopping'),
#  PosixPath('ecommerce/sales.py'),
#  PosixPath('ecommerce/__init__.py'),
#  PosixPath('ecommerce/__pycache__'),
#  PosixPath('ecommerce/customer')]

paths = [p for p in path.iterdir() if p.is_dir()]
print(paths)
# [PosixPath('ecommerce/shopping'),
#  PosixPath('ecommerce/__pycache__'),
#  PosixPath('ecommerce/customer')]

py_files = [p for p in path.glob("*.py")]
print(py_files)
# [PosixPath('ecommerce/sales.py'),
#  PosixPath('ecommerce/__init__.py')]

py_files = [p for p in path.glob("**/*.py")]
print(py_files)
# [PosixPath('ecommerce/sales.py'),
#  PosixPath('ecommerce/__init__.py'),
#  PosixPath('ecommerce/shopping/sales.py'),
#  PosixPath('ecommerce/shopping/__init__.py'),
#  PosixPath('ecommerce/customer/__init__.py'),
#  PosixPath('ecommerce/customer/contact.py')]

py_files = [p for p in path.rglob("*.py")]
print(py_files)
# [PosixPath('ecommerce/sales.py'),
#  PosixPath('ecommerce/__init__.py'),
#  PosixPath('ecommerce/shopping/sales.py'),
#  PosixPath('ecommerce/shopping/__init__.py'),
#  PosixPath('ecommerce/customer/__init__.py'),
#  PosixPath('ecommerce/customer/contact.py')]
