from pathlib import Path

Path("C:\\Program Files\\Microsoft")
Path(r"C:\Program Files\Microsoft")
Path("/usr/local/bin")
Path()
Path("ecommerce/__init__.py")
Path() / Path("ecommerce")
Path() / "ecommerce"
Path() / "ecommerce" / "__init__.py"
Path.home()


path = Path("ecommerce/__init__.py")


path.exists()
path.is_file()
path.is_dir()

print(path.name)
# __init__.py

print(path.stem)
# __init__

print(path.suffix)
# .py

print(path.parent)
# ecommerce

path = path.with_name("file.txt")
print(path)
# ecommerce/file.txt

print(path.absolute())
# /Python/ecommerce/file.txt


path = path.with_suffix(".py")
print(path)
# ecommerce/file.py
