from pathlib import Path
from time import ctime
import shutil

path = Path("ecommerce/__init__.py")
# path.exists()
# path.rename("init.txt")
# path.unlink()
print(path.stat())
# os.stat_result(st_mode=33188,
#                st_ino=22143237,
#                st_dev=16777233,
#                st_nlink=1,
#                st_uid=501,
#                st_gid=20,
#                st_size=31,
#                st_atime=1740950939,
#                st_mtime=1740950938,
#                st_ctime=1740950938)


print(ctime(path.stat().st_ctime))
# Mon Mar  3 06:28:58 2025

path.read_bytes()

print(path.read_text())
# print("Ecommerce initialized")

with open("ecommerce/__init__.py", "r") as file:
    file.read()

# path.write_text("....")
# path.write_bytes()


source = Path("ecommerce/__init__.py")
target = Path() / "__init__.py"

target.write_text(source.read_text())

shutil.copy(source, target)
